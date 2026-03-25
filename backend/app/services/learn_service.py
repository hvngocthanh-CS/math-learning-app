"""Learn business logic: grades, chapters, lessons, completion, progression."""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Session, joinedload

from app.models.grade import Grade
from app.models.lesson import Chapter, Lesson, LessonContent
from app.models.progress import StudentProgress, ProgressStatus, QuizAnswer
from app.models.user import User
from app.schemas.learn import (
    GradeResponse,
    ChapterDetailResponse,
    LessonBriefResponse,
    LessonResponse,
    LessonDetailResponse,
    LessonContentResponse,
    LessonCompleteResponse,
)
from app.features.learn.generators import generate_problems


# ─── Grades ──────────────────────────────────────────────────────

def list_grades(db: Session, student_id: UUID) -> List[GradeResponse]:
    """List all grades with lesson counts and completion stats in minimal queries."""
    grades = db.query(Grade).order_by(Grade.number).all()
    if not grades:
        return []

    grade_ids = [g.id for g in grades]

    # Single query: total chapters per grade
    chapter_counts = dict(
        db.query(Chapter.grade_id, func.count(Chapter.id))
        .filter(Chapter.grade_id.in_(grade_ids))
        .group_by(Chapter.grade_id)
        .all()
    )

    # Single query: total lessons per grade
    lesson_counts = dict(
        db.query(Chapter.grade_id, func.count(Lesson.id))
        .join(Lesson, Lesson.chapter_id == Chapter.id)
        .filter(Chapter.grade_id.in_(grade_ids))
        .group_by(Chapter.grade_id)
        .all()
    )

    # Single query: completed lessons per grade for this student
    completed_counts = dict(
        db.query(Chapter.grade_id, func.count(StudentProgress.id))
        .join(Lesson, Lesson.chapter_id == Chapter.id)
        .join(StudentProgress, StudentProgress.lesson_id == Lesson.id)
        .filter(
            Chapter.grade_id.in_(grade_ids),
            StudentProgress.student_id == student_id,
            StudentProgress.status == ProgressStatus.completed,
        )
        .group_by(Chapter.grade_id)
        .all()
    )

    return [
        GradeResponse(
            id=g.id, number=g.number, name=g.name,
            description=g.description, icon_url=g.icon_url,
            total_chapters=chapter_counts.get(g.id, 0),
            total_lessons=lesson_counts.get(g.id, 0),
            completed_lessons=completed_counts.get(g.id, 0),
        )
        for g in grades
    ]


# ─── Chapters with unlock logic ─────────────────────────────────

def get_grade_chapters(db: Session, grade_id: UUID, student_id: UUID) -> List[ChapterDetailResponse]:
    grade = db.query(Grade).filter(Grade.id == grade_id).first()
    if not grade:
        return None  # caller raises 404

    # Single query: all chapters with their lessons eagerly loaded
    chapters = (
        db.query(Chapter)
        .options(joinedload(Chapter.lessons))
        .filter(Chapter.grade_id == grade_id)
        .order_by(Chapter.order)
        .all()
    )

    # Build ordered lesson IDs across all chapters
    all_lessons = []
    for ch in chapters:
        for lesson in sorted(ch.lessons, key=lambda l: l.order):
            all_lessons.append(lesson)
    ordered_ids = [l.id for l in all_lessons]

    # Single query: all progress for these lessons
    progress_map = {}
    if ordered_ids:
        for p in db.query(StudentProgress).filter(
            StudentProgress.student_id == student_id,
            StudentProgress.lesson_id.in_(ordered_ids),
        ).all():
            progress_map[p.lesson_id] = p

    # Build ID→index map for O(1) lookups
    id_index = {lid: i for i, lid in enumerate(ordered_ids)}

    result = []
    for chapter in chapters:
        lessons = sorted(chapter.lessons, key=lambda l: l.order)
        completed_count = 0
        lesson_list = []

        for lesson in lessons:
            progress = progress_map.get(lesson.id)
            lesson_status = _determine_lesson_status(lesson.id, progress, ordered_ids, progress_map, id_index)
            if progress and progress.status == ProgressStatus.completed:
                completed_count += 1

            lesson_list.append(LessonBriefResponse(
                id=lesson.id, title=lesson.title, order=lesson.order,
                description=lesson.description, xp_reward=lesson.xp_reward or 20,
                status=lesson_status,
                stars_earned=progress.stars_earned if progress else 0,
                score=progress.score if progress else 0,
            ))

        result.append(ChapterDetailResponse(
            id=chapter.id, grade_id=chapter.grade_id, title=chapter.title,
            order=chapter.order, description=chapter.description,
            total_lessons=len(lessons), completed_lessons=completed_count,
            lessons=lesson_list,
        ))
    return result


def _determine_lesson_status(lesson_id, progress, ordered_ids, progress_map, id_index=None) -> ProgressStatus:
    """Determine unlock status based on sequential progression."""
    if progress:
        return progress.status
    if id_index:
        idx = id_index.get(lesson_id, -1)
    else:
        idx = ordered_ids.index(lesson_id) if lesson_id in ordered_ids else -1
    if idx == 0:
        return ProgressStatus.in_progress
    if idx > 0:
        prev_progress = progress_map.get(ordered_ids[idx - 1])
        if prev_progress and prev_progress.status == ProgressStatus.completed:
            return ProgressStatus.in_progress
    return ProgressStatus.locked


# ─── Lessons ─────────────────────────────────────────────────────

def get_chapter_lessons(db: Session, chapter_id: UUID, student_id: UUID) -> Optional[List[LessonResponse]]:
    chapter = db.query(Chapter).filter(Chapter.id == chapter_id).first()
    if not chapter:
        return None

    lessons = db.query(Lesson).filter(Lesson.chapter_id == chapter_id).order_by(Lesson.order).all()

    # Single query: all progress for these lessons
    lesson_ids = [l.id for l in lessons]
    progress_map = {}
    if lesson_ids:
        for p in db.query(StudentProgress).filter(
            StudentProgress.student_id == student_id,
            StudentProgress.lesson_id.in_(lesson_ids),
        ).all():
            progress_map[p.lesson_id] = p

    return [
        LessonResponse(
            id=lesson.id, chapter_id=lesson.chapter_id, title=lesson.title,
            order=lesson.order, content_type=lesson.content_type,
            content_url=lesson.content_url, description=lesson.description,
            is_locked=lesson.is_locked,
            status=progress_map[lesson.id].status if lesson.id in progress_map else ProgressStatus.locked,
            score=progress_map[lesson.id].score if lesson.id in progress_map else 0,
            stars_earned=progress_map[lesson.id].stars_earned if lesson.id in progress_map else 0,
        )
        for lesson in lessons
    ]


def get_lesson_detail(db: Session, lesson_id: UUID, student_id: UUID) -> Optional[LessonDetailResponse]:
    # Single query with joins
    lesson = (
        db.query(Lesson)
        .options(joinedload(Lesson.chapter).joinedload(Chapter.grade))
        .filter(Lesson.id == lesson_id)
        .first()
    )
    if not lesson:
        return None

    progress = db.query(StudentProgress).filter(
        StudentProgress.student_id == student_id,
        StudentProgress.lesson_id == lesson.id,
    ).first()

    chapter = lesson.chapter
    grade = chapter.grade if chapter else None

    return LessonDetailResponse(
        id=lesson.id, chapter_id=lesson.chapter_id, title=lesson.title,
        order=lesson.order, content_type=lesson.content_type,
        content_url=lesson.content_url, description=lesson.description,
        is_locked=lesson.is_locked,
        status=progress.status if progress else ProgressStatus.locked,
        score=progress.score if progress else 0,
        stars_earned=progress.stars_earned if progress else 0,
        chapter_title=chapter.title if chapter else None,
        grade_name=grade.name if grade else None,
    )


def get_lesson_content(db: Session, lesson_id: UUID) -> Optional[LessonContentResponse]:
    # Single query with join
    content = (
        db.query(LessonContent)
        .filter(LessonContent.lesson_id == lesson_id)
        .first()
    )
    if not content:
        return None

    if content.problem_config:
        practice = generate_problems(content.problem_config, mode="practice")
        quiz = generate_problems(content.problem_config, mode="quiz")
    else:
        practice = content.practice_problems or []
        quiz = content.quiz_problems or []

    return LessonContentResponse(
        explanation=content.explanation, examples=content.examples or [],
        steps=content.steps or [], fun_fact=content.fun_fact or "",
        practice_problems=practice, quiz_problems=quiz,
    )


# ─── Lesson completion & progression ────────────────────────────

def complete_lesson(db: Session, lesson_id: UUID, quiz_score: int, total_questions: int, user: User, answers=None) -> Optional[LessonCompleteResponse]:
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        return None

    # Calculate rewards
    ratio = quiz_score / total_questions if total_questions > 0 else 0
    stars = 3 if ratio >= 1.0 else 2 if ratio >= 0.8 else 1 if ratio >= 0.6 else 0
    xp_reward = lesson.xp_reward or 20
    xp_earned = stars * xp_reward
    coins_earned = stars * 10
    score_percent = int(ratio * 100)

    # Upsert progress
    progress = db.query(StudentProgress).filter(
        StudentProgress.student_id == user.id,
        StudentProgress.lesson_id == lesson.id,
    ).first()

    if progress:
        progress.attempts = (progress.attempts or 0) + 1
        if score_percent > (progress.best_score or 0):
            progress.best_score = score_percent
            progress.score = score_percent
            progress.stars_earned = stars
        if stars > 0:
            progress.status = ProgressStatus.completed
            progress.completed_at = datetime.utcnow()
    else:
        progress = StudentProgress(
            student_id=user.id, lesson_id=lesson.id,
            status=ProgressStatus.completed if stars > 0 else ProgressStatus.in_progress,
            score=score_percent, stars_earned=stars,
            attempts=1, best_score=score_percent,
            completed_at=datetime.utcnow() if stars > 0 else None,
        )
        db.add(progress)

    # Save per-question answers if provided
    if answers:
        now = datetime.utcnow()
        for ans in answers:
            db.add(QuizAnswer(
                student_id=user.id,
                lesson_id=lesson.id,
                question_text=ans.question_text,
                student_answer=ans.student_answer,
                correct_answer=ans.correct_answer,
                is_correct=ans.is_correct,
                attempted_at=now,
            ))

    # Update user stats
    user.xp = (user.xp or 0) + xp_earned
    user.stars = (user.stars or 0) + stars
    user.coins = (user.coins or 0) + coins_earned
    old_level = user.level or 1
    new_level = (user.xp // 500) + 1
    level_up = new_level > old_level
    if level_up:
        user.level = new_level

    # Unlock next lesson
    next_lesson_id = _unlock_next_lesson(db, lesson, user.id)
    db.commit()

    return LessonCompleteResponse(
        stars_earned=stars, xp_earned=xp_earned, coins_earned=coins_earned,
        next_lesson_id=next_lesson_id, level_up=level_up,
    )


def _unlock_next_lesson(db: Session, current_lesson: Lesson, student_id: UUID) -> Optional[str]:
    """Find and unlock the next lesson (within chapter, then cross-chapter)."""
    next_lesson = db.query(Lesson).filter(
        Lesson.chapter_id == current_lesson.chapter_id,
        Lesson.order == current_lesson.order + 1,
    ).first()

    if not next_lesson:
        chapter = db.query(Chapter).filter(Chapter.id == current_lesson.chapter_id).first()
        if chapter:
            next_chapter = db.query(Chapter).filter(
                Chapter.grade_id == chapter.grade_id,
                Chapter.order == chapter.order + 1,
            ).first()
            if next_chapter:
                next_lesson = db.query(Lesson).filter(
                    Lesson.chapter_id == next_chapter.id,
                ).order_by(Lesson.order).first()

    if not next_lesson:
        return None

    existing = db.query(StudentProgress).filter(
        StudentProgress.student_id == student_id,
        StudentProgress.lesson_id == next_lesson.id,
    ).first()
    if not existing:
        db.add(StudentProgress(
            student_id=student_id, lesson_id=next_lesson.id,
            status=ProgressStatus.in_progress,
            score=0, stars_earned=0, attempts=0, best_score=0,
        ))
    return str(next_lesson.id)
