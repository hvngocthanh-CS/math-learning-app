"""Progress business logic: student progress summary across grades."""

from typing import List
from uuid import UUID
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.grade import Grade
from app.models.lesson import Chapter, Lesson
from app.models.progress import StudentProgress, ProgressStatus
from app.models.user import User
from app.schemas.progress import GradeProgressResponse, StudentProgressSummary


def get_student_progress(db: Session, user: User) -> StudentProgressSummary:
    grades = db.query(Grade).order_by(Grade.number).all()
    total_completed = 0
    total_stars = 0
    grade_list = []

    for grade in grades:
        total_lessons = (
            db.query(func.count(Lesson.id))
            .join(Chapter, Lesson.chapter_id == Chapter.id)
            .filter(Chapter.grade_id == grade.id).scalar() or 0
        )
        completed = (
            db.query(func.count(StudentProgress.id))
            .join(Lesson, StudentProgress.lesson_id == Lesson.id)
            .join(Chapter, Lesson.chapter_id == Chapter.id)
            .filter(Chapter.grade_id == grade.id,
                    StudentProgress.student_id == user.id,
                    StudentProgress.status == ProgressStatus.completed)
            .scalar() or 0
        )
        earned = (
            db.query(func.coalesce(func.sum(StudentProgress.stars_earned), 0))
            .join(Lesson, StudentProgress.lesson_id == Lesson.id)
            .join(Chapter, Lesson.chapter_id == Chapter.id)
            .filter(Chapter.grade_id == grade.id,
                    StudentProgress.student_id == user.id)
            .scalar() or 0
        )
        total_completed += completed
        total_stars += earned
        grade_list.append(GradeProgressResponse(
            grade_id=grade.id, grade_name=grade.name, grade_number=grade.number,
            total_lessons=total_lessons, completed_lessons=completed,
            total_stars=total_lessons * 3, earned_stars=earned,
        ))

    return StudentProgressSummary(
        total_lessons_completed=total_completed, total_stars_earned=total_stars,
        total_xp=user.xp or 0, current_level=user.level or 1, grades=grade_list,
    )
