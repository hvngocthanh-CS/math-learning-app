"""
Database seeding for MathQuest.

Commands:
  python -m app.seed                  → Safe seed (only add missing data, preserves users)
  python -m app.seed --update         → Update lesson content from seed data (preserves users & progress)
  python -m app.seed --reseed-grade 2 → Delete & reseed a single grade (preserves users & other grades)
  python -m app.seed --reset          → DESTRUCTIVE: drop all tables and reseed everything
"""

import sys
from app.core.database import engine, SessionLocal, Base
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.models.grade import Grade
from app.models.lesson import Chapter, Lesson, ContentType, LessonContent
from app.models.progress import StudentProgress, ProgressStatus
from app.features.learn.seed_data.grade1 import GRADE1_CHAPTERS
from app.features.learn.seed_data.grade2 import GRADE2_CHAPTERS


def _seed_grade(db, grade, chapters_data, grade_num):
    """Seed chapters and lessons for a single grade (skip if already exists)."""
    existing = db.query(Chapter).filter(Chapter.grade_id == grade.id).first()
    if existing:
        print(f"  Grade {grade_num}: already has data, skipping.")
        # Return first lesson for progress seeding
        first = (
            db.query(Lesson)
            .join(Chapter, Lesson.chapter_id == Chapter.id)
            .filter(Chapter.grade_id == grade.id)
            .order_by(Chapter.order, Lesson.order)
            .first()
        )
        return first

    total = 0
    first_lesson = None
    for ch in chapters_data:
        chapter = Chapter(grade_id=grade.id, title=ch["title"], description=ch["description"], order=ch["order"])
        db.add(chapter)
        db.flush()
        for ld in ch["lessons"]:
            lesson = Lesson(
                chapter_id=chapter.id, title=ld["title"], description=ld["description"],
                order=ld["order"], xp_reward=ld.get("xp_reward", 20),
                content_type=ContentType.slide,
                content_url=f"/content/grade{grade_num}/ch{ch['order']}/lesson{ld['order']}",
                is_locked=(ch["order"] != 1 or ld["order"] != 1),
            )
            db.add(lesson)
            db.flush()
            if first_lesson is None:
                first_lesson = lesson
            cd = ld["content"]
            db.add(LessonContent(
                lesson_id=lesson.id, explanation=cd["explanation"],
                examples=cd["examples"], steps=cd["steps"], fun_fact=cd["fun_fact"],
                practice_problems=cd.get("practice_problems"),
                quiz_problems=cd.get("quiz_problems"),
                problem_config=cd.get("problem_config"),
            ))
            total += 1
    db.flush()
    print(f"  Grade {grade_num}: {len(chapters_data)} chapters, {total} lessons created.")
    return first_lesson


def _ensure_demo_users(db):
    """Create demo accounts only if they don't exist."""
    teacher = db.query(User).filter(User.email == "teacher@mathquest.com").first()
    if not teacher:
        teacher = User(email="teacher@mathquest.com", name="Demo Teacher",
                       password_hash=hash_password("password123"), role=UserRole.teacher)
        db.add(teacher)
        print("  Created demo teacher: teacher@mathquest.com / password123")
    else:
        print("  Demo teacher already exists, skipping.")

    student = db.query(User).filter(User.email == "student@mathquest.com").first()
    if not student:
        student = User(email="student@mathquest.com", name="Demo Student",
                       password_hash=hash_password("password123"), role=UserRole.student,
                       level=1, xp=0, stars=0, coins=0, streak=3)
        db.add(student)
        print("  Created demo student: student@mathquest.com / password123")
    else:
        print("  Demo student already exists, skipping.")

    db.flush()
    return student


def _update_content(db, chapters_data, grade_num):
    """Update existing lesson content AND add new chapters/lessons.
    Preserves all user progress for existing lessons."""
    grade = db.query(Grade).filter(Grade.number == grade_num).first()
    if not grade:
        print(f"  Grade {grade_num}: not found, skipping.")
        return

    updated = 0
    added_chapters = 0
    added_lessons = 0

    for ch in chapters_data:
        # Find or create chapter
        chapter = (
            db.query(Chapter)
            .filter(Chapter.grade_id == grade.id, Chapter.order == ch["order"])
            .first()
        )
        if not chapter:
            chapter = Chapter(
                grade_id=grade.id, title=ch["title"],
                description=ch["description"], order=ch["order"],
            )
            db.add(chapter)
            db.flush()
            added_chapters += 1
        else:
            chapter.title = ch["title"]
            chapter.description = ch["description"]

        for ld in ch["lessons"]:
            # Find existing lesson by chapter + order
            lesson = (
                db.query(Lesson)
                .filter(Lesson.chapter_id == chapter.id, Lesson.order == ld["order"])
                .first()
            )

            if lesson:
                # Update existing lesson metadata
                lesson.title = ld["title"]
                lesson.description = ld["description"]
                lesson.xp_reward = ld.get("xp_reward", 20)

                # Update content (progress untouched)
                content = db.query(LessonContent).filter(
                    LessonContent.lesson_id == lesson.id
                ).first()
                if content:
                    cd = ld["content"]
                    content.explanation = cd["explanation"]
                    content.examples = cd["examples"]
                    content.steps = cd["steps"]
                    content.fun_fact = cd["fun_fact"]
                    if "problem_config" in cd:
                        content.problem_config = cd["problem_config"]
                    updated += 1
            else:
                # Add new lesson
                lesson = Lesson(
                    chapter_id=chapter.id, title=ld["title"],
                    description=ld["description"], order=ld["order"],
                    xp_reward=ld.get("xp_reward", 20),
                    content_type=ContentType.slide,
                    content_url=f"/content/grade{grade_num}/ch{ch['order']}/lesson{ld['order']}",
                    is_locked=True,
                )
                db.add(lesson)
                db.flush()
                cd = ld["content"]
                db.add(LessonContent(
                    lesson_id=lesson.id, explanation=cd["explanation"],
                    examples=cd["examples"], steps=cd["steps"],
                    fun_fact=cd["fun_fact"],
                    practice_problems=cd.get("practice_problems"),
                    quiz_problems=cd.get("quiz_problems"),
                    problem_config=cd.get("problem_config"),
                ))
                added_lessons += 1

    db.flush()
    print(f"  Grade {grade_num}: updated {updated} lessons, added {added_chapters} chapters + {added_lessons} new lessons.")


def _reseed_grade(db, grade_num, chapters_data):
    """Delete all chapters/lessons for a grade and reseed from scratch.
    Preserves users and other grades. Removes progress for affected lessons."""
    grade = db.query(Grade).filter(Grade.number == grade_num).first()
    if not grade:
        print(f"  Grade {grade_num}: not found, skipping.")
        return

    # Find all lessons for this grade
    lesson_ids = [
        lid for (lid,) in
        db.query(Lesson.id)
        .join(Chapter, Lesson.chapter_id == Chapter.id)
        .filter(Chapter.grade_id == grade.id)
        .all()
    ]

    if lesson_ids:
        # Delete progress for these lessons
        deleted_progress = db.query(StudentProgress).filter(
            StudentProgress.lesson_id.in_(lesson_ids)
        ).delete(synchronize_session=False)
        # Delete lesson content
        db.query(LessonContent).filter(
            LessonContent.lesson_id.in_(lesson_ids)
        ).delete(synchronize_session=False)
        # Delete lessons
        db.query(Lesson).filter(Lesson.id.in_(lesson_ids)).delete(synchronize_session=False)
        print(f"  Grade {grade_num}: deleted {len(lesson_ids)} old lessons, {deleted_progress} progress records.")

    # Delete chapters
    db.query(Chapter).filter(Chapter.grade_id == grade.id).delete(synchronize_session=False)
    db.flush()

    # Re-seed
    _seed_grade(db, grade, chapters_data, grade_num)


def seed(reset: bool = False, update: bool = False, reseed_grade: int = None):
    """Seed the database. If reset=True, drop all tables first (DESTRUCTIVE)."""

    if reset:
        print("⚠️  RESET MODE: Dropping all tables...")
        Base.metadata.drop_all(bind=engine)

    print("Creating tables (if not exist)...")
    Base.metadata.create_all(bind=engine)

    grade_data = {1: GRADE1_CHAPTERS, 2: GRADE2_CHAPTERS}

    db = SessionLocal()
    try:
        # Grades (idempotent)
        print("Seeding grades...")
        grades = []
        for i in range(1, 6):
            existing = db.query(Grade).filter(Grade.number == i).first()
            if existing:
                grades.append(existing)
            else:
                g = Grade(number=i, name=f"Grade {i}",
                          description=f"Mathematics curriculum for Grade {i} students",
                          icon_url=f"/icons/grade-{i}.png")
                db.add(g)
                db.flush()
                grades.append(g)
        print(f"  {len(grades)} grades ready.")

        if reseed_grade:
            # Reseed a single grade
            if reseed_grade not in grade_data:
                print(f"  No seed data for grade {reseed_grade}.")
            else:
                print(f"Reseeding grade {reseed_grade}...")
                _reseed_grade(db, reseed_grade, grade_data[reseed_grade])
        elif update:
            print("Updating lesson content...")
            for num, chapters in grade_data.items():
                _update_content(db, chapters, num)
        else:
            print("Seeding curriculum...")
            first_lesson = None
            for num, chapters in grade_data.items():
                fl = _seed_grade(db, grades[num - 1], chapters, num)
                if num == 1 and fl:
                    first_lesson = fl

            # Demo users (idempotent)
            print("Seeding demo users...")
            student = _ensure_demo_users(db)

            # Initial progress for demo student (idempotent)
            if first_lesson and student:
                existing_progress = db.query(StudentProgress).filter(
                    StudentProgress.student_id == student.id,
                    StudentProgress.lesson_id == first_lesson.id,
                ).first()
                if not existing_progress:
                    db.add(StudentProgress(
                        student_id=student.id, lesson_id=first_lesson.id,
                        status=ProgressStatus.in_progress, score=0, stars_earned=0, attempts=0, best_score=0,
                    ))
                    print("  Created initial progress for demo student.")

        db.commit()
        print("Seeding complete!")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    is_reset = "--reset" in sys.argv
    is_update = "--update" in sys.argv

    reseed_grade_num = None
    if "--reseed-grade" in sys.argv:
        idx = sys.argv.index("--reseed-grade")
        if idx + 1 < len(sys.argv):
            reseed_grade_num = int(sys.argv[idx + 1])

    if is_reset:
        confirm = input("⚠️  This will DELETE ALL DATA (users, progress, etc). Type 'yes' to confirm: ")
        if confirm.strip().lower() != "yes":
            print("Aborted.")
            sys.exit(0)
    seed(reset=is_reset, update=is_update, reseed_grade=reseed_grade_num)
