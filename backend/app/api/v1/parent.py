"""Parent-specific endpoints: view their child's progress only."""

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

router = APIRouter(prefix="/parent", tags=["parent"])


# ── Schemas ──────────────────────────────────────────────────────

class ChildInfo(BaseModel):
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
    lessons_completed: int
    total_correct: int
    total_incorrect: int
    average_score: float

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


class ParentDashboardResponse(BaseModel):
    child: Optional[ChildInfo] = None
    progress: List[LessonProgressDetail] = []


# ── Helpers ──────────────────────────────────────────────────────

def _get_child_for_parent(db: Session, parent: User) -> Optional[User]:
    """Find the child linked to this parent."""
    child = db.query(User).filter(
        User.parent_id == parent.id,
        User.role == UserRole.student,
    ).first()
    return child


# ── Endpoints ────────────────────────────────────────────────────

@router.get("/dashboard", response_model=ParentDashboardResponse)
def get_parent_dashboard(
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.parent)),
):
    """Get parent dashboard with their child's progress."""
    child = _get_child_for_parent(db, user)
    if not child:
        return ParentDashboardResponse(child=None, progress=[])

    # Compute child stats
    lessons_completed = db.query(func.count(StudentProgress.id)).filter(
        StudentProgress.student_id == child.id,
        StudentProgress.status == ProgressStatus.completed,
    ).scalar() or 0

    avg_score = db.query(func.avg(StudentProgress.best_score)).filter(
        StudentProgress.student_id == child.id,
        StudentProgress.status == ProgressStatus.completed,
    ).scalar()
    average_score = round(float(avg_score), 1) if avg_score else 0.0

    total_correct = db.query(func.count(QuizAnswer.id)).filter(
        QuizAnswer.student_id == child.id,
        QuizAnswer.is_correct == True,
    ).scalar() or 0

    total_incorrect = db.query(func.count(QuizAnswer.id)).filter(
        QuizAnswer.student_id == child.id,
        QuizAnswer.is_correct == False,
    ).scalar() or 0

    child_info = ChildInfo(
        id=child.id,
        name=child.name,
        email=child.email,
        avatar_url=child.avatar_url,
        level=child.level,
        xp=child.xp,
        stars=child.stars,
        coins=child.coins,
        streak=child.streak,
        last_login_date=str(child.last_login_date) if child.last_login_date else None,
        lessons_completed=lessons_completed,
        total_correct=total_correct,
        total_incorrect=total_incorrect,
        average_score=average_score,
    )

    # Get progress records
    progress_records = db.query(StudentProgress).filter(
        StudentProgress.student_id == child.id,
        StudentProgress.status != ProgressStatus.locked,
    ).all()

    progress_list = []
    for p in progress_records:
        lesson = db.query(Lesson).filter(Lesson.id == p.lesson_id).first()
        if not lesson:
            continue

        chapter = db.query(Chapter).filter(Chapter.id == lesson.chapter_id).first()
        grade = db.query(Grade).filter(Grade.id == chapter.grade_id).first() if chapter else None

        # Get latest quiz answers
        quiz_answers = db.query(QuizAnswer).filter(
            QuizAnswer.student_id == child.id,
            QuizAnswer.lesson_id == p.lesson_id,
        ).order_by(QuizAnswer.attempted_at.desc()).all()

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

    return ParentDashboardResponse(child=child_info, progress=progress_list)
