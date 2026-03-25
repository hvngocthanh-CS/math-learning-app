"""Teacher-specific endpoints: dashboard stats, student progress, ranking."""

from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from app.core.deps import get_db, require_role
from app.models.user import User, UserRole
from app.models.progress import StudentProgress, ProgressStatus, QuizAnswer
from app.models.lesson import Lesson, Chapter
from app.models.grade import Grade

router = APIRouter(prefix="/teacher", tags=["teacher"])


# ── Schemas ──────────────────────────────────────────────────────

class DashboardStats(BaseModel):
    total_students: int
    total_parents: int
    active_today: int
    average_score: float
    total_lessons_completed: int
    average_stars: float


class StudentSummary(BaseModel):
    id: UUID
    name: str
    email: str
    avatar_url: Optional[str] = None
    level: int
    xp: int
    stars: int
    coins: int
    streak: int
    last_login_date: Optional[str] = None
    created_at: Optional[str] = None
    lessons_completed: int
    total_correct: int
    total_incorrect: int
    average_score: float
    parent_name: Optional[str] = None

    class Config:
        from_attributes = True


class QuizAnswerDetail(BaseModel):
    question_text: str
    student_answer: str
    correct_answer: str
    is_correct: bool
    attempted_at: Optional[str] = None


class LessonProgressDetail(BaseModel):
    lesson_id: UUID
    lesson_title: str
    chapter_title: str
    grade_name: str
    status: str
    score: int
    best_score: int
    stars_earned: int
    attempts: int
    completed_at: Optional[str] = None
    quiz_answers: List[QuizAnswerDetail] = []


class StudentDetailResponse(BaseModel):
    student: StudentSummary
    progress: List[LessonProgressDetail]


class RankingEntry(BaseModel):
    rank: int
    student_id: UUID
    name: str
    level: int
    stars: int
    xp: int
    streak: int
    lessons_completed: int
    average_score: float
    total_correct: int
    total_incorrect: int


class RankingResponse(BaseModel):
    rankings: List[RankingEntry]
    total_students: int


# ── Helpers ──────────────────────────────────────────────────────

def _get_student_stats(db: Session, student: User):
    """Get computed stats for a student."""
    lessons_completed = db.query(func.count(StudentProgress.id)).filter(
        StudentProgress.student_id == student.id,
        StudentProgress.status == ProgressStatus.completed,
    ).scalar() or 0

    avg_score_result = db.query(func.avg(StudentProgress.best_score)).filter(
        StudentProgress.student_id == student.id,
        StudentProgress.status == ProgressStatus.completed,
    ).scalar()
    average_score = round(float(avg_score_result), 1) if avg_score_result else 0.0

    total_correct = db.query(func.count(QuizAnswer.id)).filter(
        QuizAnswer.student_id == student.id,
        QuizAnswer.is_correct == True,
    ).scalar() or 0

    total_incorrect = db.query(func.count(QuizAnswer.id)).filter(
        QuizAnswer.student_id == student.id,
        QuizAnswer.is_correct == False,
    ).scalar() or 0

    return lessons_completed, average_score, total_correct, total_incorrect


# ── Endpoints ────────────────────────────────────────────────────

@router.get("/dashboard", response_model=DashboardStats)
def get_teacher_dashboard(
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.teacher)),
):
    """Get real dashboard statistics for teachers."""
    total_students = db.query(func.count(User.id)).filter(User.role == UserRole.student).scalar() or 0
    total_parents = db.query(func.count(User.id)).filter(User.role == UserRole.parent).scalar() or 0

    # Active today: students who logged in today
    today = datetime.utcnow().date()
    active_today = db.query(func.count(User.id)).filter(
        User.role == UserRole.student,
        User.last_login_date == today,
    ).scalar() or 0

    # Average score across all completed lessons
    avg_score = db.query(func.avg(StudentProgress.best_score)).filter(
        StudentProgress.status == ProgressStatus.completed,
    ).scalar()
    average_score = round(float(avg_score), 1) if avg_score else 0.0

    total_lessons_completed = db.query(func.count(StudentProgress.id)).filter(
        StudentProgress.status == ProgressStatus.completed,
    ).scalar() or 0

    # Average stars per student
    avg_stars = db.query(func.avg(User.stars)).filter(User.role == UserRole.student).scalar()
    average_stars = round(float(avg_stars), 1) if avg_stars else 0.0

    return DashboardStats(
        total_students=total_students,
        total_parents=total_parents,
        active_today=active_today,
        average_score=average_score,
        total_lessons_completed=total_lessons_completed,
        average_stars=average_stars,
    )


@router.get("/students", response_model=List[StudentSummary])
def list_students_with_progress(
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.teacher)),
):
    """List all students with their computed progress stats."""
    students = db.query(User).filter(User.role == UserRole.student).order_by(User.created_at.desc()).all()

    result = []
    for s in students:
        lessons_completed, average_score, total_correct, total_incorrect = _get_student_stats(db, s)

        # Get parent name if linked
        parent_name = None
        if s.parent_id:
            parent = db.query(User).filter(User.id == s.parent_id).first()
            if parent:
                parent_name = parent.name

        result.append(StudentSummary(
            id=s.id,
            name=s.name,
            email=s.email,
            avatar_url=s.avatar_url,
            level=s.level,
            xp=s.xp,
            stars=s.stars,
            coins=s.coins,
            streak=s.streak,
            last_login_date=str(s.last_login_date) if s.last_login_date else None,
            created_at=s.created_at.isoformat() if s.created_at else None,
            lessons_completed=lessons_completed,
            total_correct=total_correct,
            total_incorrect=total_incorrect,
            average_score=average_score,
            parent_name=parent_name,
        ))

    return result


@router.get("/students/{student_id}/progress", response_model=StudentDetailResponse)
def get_student_detail(
    student_id: UUID,
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.teacher)),
):
    """Get detailed progress for a specific student, including per-question answers."""
    student = db.query(User).filter(User.id == student_id, User.role == UserRole.student).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    lessons_completed, average_score, total_correct, total_incorrect = _get_student_stats(db, student)

    parent_name = None
    if student.parent_id:
        parent = db.query(User).filter(User.id == student.parent_id).first()
        if parent:
            parent_name = parent.name

    student_summary = StudentSummary(
        id=student.id,
        name=student.name,
        email=student.email,
        avatar_url=student.avatar_url,
        level=student.level,
        xp=student.xp,
        stars=student.stars,
        coins=student.coins,
        streak=student.streak,
        last_login_date=str(student.last_login_date) if student.last_login_date else None,
        created_at=student.created_at.isoformat() if student.created_at else None,
        lessons_completed=lessons_completed,
        total_correct=total_correct,
        total_incorrect=total_incorrect,
        average_score=average_score,
        parent_name=parent_name,
    )

    # Get all progress records with lesson details
    progress_records = db.query(StudentProgress).filter(
        StudentProgress.student_id == student_id,
        StudentProgress.status != ProgressStatus.locked,
    ).all()

    progress_list = []
    for p in progress_records:
        lesson = db.query(Lesson).filter(Lesson.id == p.lesson_id).first()
        if not lesson:
            continue

        chapter = db.query(Chapter).filter(Chapter.id == lesson.chapter_id).first()
        grade = db.query(Grade).filter(Grade.id == chapter.grade_id).first() if chapter else None

        # Get quiz answers for this lesson (most recent attempt)
        quiz_answers = db.query(QuizAnswer).filter(
            QuizAnswer.student_id == student_id,
            QuizAnswer.lesson_id == p.lesson_id,
        ).order_by(QuizAnswer.attempted_at.desc()).all()

        # Group by attempt (same attempted_at timestamp)
        latest_answers = []
        if quiz_answers:
            latest_time = quiz_answers[0].attempted_at
            latest_answers = [
                QuizAnswerDetail(
                    question_text=a.question_text,
                    student_answer=a.student_answer,
                    correct_answer=a.correct_answer,
                    is_correct=a.is_correct,
                    attempted_at=a.attempted_at.isoformat() if a.attempted_at else None,
                )
                for a in quiz_answers
                if a.attempted_at == latest_time
            ]

        progress_list.append(LessonProgressDetail(
            lesson_id=p.lesson_id,
            lesson_title=lesson.title,
            chapter_title=chapter.title if chapter else "Unknown",
            grade_name=grade.name if grade else "Unknown",
            status=p.status.value,
            score=p.score or 0,
            best_score=p.best_score or 0,
            stars_earned=p.stars_earned or 0,
            attempts=p.attempts or 0,
            completed_at=p.completed_at.isoformat() if p.completed_at else None,
            quiz_answers=latest_answers,
        ))

    return StudentDetailResponse(student=student_summary, progress=progress_list)


@router.get("/ranking", response_model=RankingResponse)
def get_teacher_ranking(
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.teacher)),
):
    """Get ranking of all students for teacher view."""
    students = db.query(User).filter(User.role == UserRole.student).all()

    entries = []
    for s in students:
        lessons_completed, average_score, total_correct, total_incorrect = _get_student_stats(db, s)

        ranking_score = s.xp + (s.stars * 15) + (lessons_completed * 20) + (s.streak * 5)

        entries.append({
            "student_id": s.id,
            "name": s.name,
            "level": s.level,
            "stars": s.stars,
            "xp": s.xp,
            "streak": s.streak,
            "lessons_completed": lessons_completed,
            "average_score": average_score,
            "total_correct": total_correct,
            "total_incorrect": total_incorrect,
            "ranking_score": ranking_score,
        })

    entries.sort(key=lambda e: (-e["ranking_score"], -e["xp"], e["name"]))

    rankings = []
    for i, e in enumerate(entries):
        rankings.append(RankingEntry(rank=i + 1, **e))

    return RankingResponse(rankings=rankings, total_students=len(entries))
