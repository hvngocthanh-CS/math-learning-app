"""Leaderboard endpoint with period and grade filters."""

from datetime import datetime, timedelta
from enum import Enum as PyEnum

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from app.core.deps import get_db, get_current_user, require_role
from app.models.user import User, UserRole
from app.models.progress import StudentProgress, ProgressStatus
from app.models.lesson import Lesson, Chapter
from app.models.grade import Grade

router = APIRouter(tags=["leaderboard"])


class LeaderboardPeriod(str, PyEnum):
    week = "week"
    month = "month"
    all_time = "all"


class LeaderboardEntry(BaseModel):
    rank: int
    student_id: UUID
    name: str
    avatar_url: Optional[str] = None
    level: int
    xp: int
    stars: int
    streak: int
    coins: int
    lessons_completed: int
    ranking_score: int
    is_current_user: bool = False
    grade_name: Optional[str] = None

    class Config:
        from_attributes = True


class LeaderboardResponse(BaseModel):
    leaderboard: List[LeaderboardEntry]
    current_user_rank: Optional[LeaderboardEntry] = None
    total_students: int = 0


class GradeOption(BaseModel):
    id: UUID
    number: int
    name: str


class LeaderboardFiltersResponse(BaseModel):
    grades: List[GradeOption]


def _compute_ranking_score(xp: int, stars: int, lessons_completed: int, streak: int) -> int:
    """
    Ranking formula:
      XP              — overall effort (1 point per XP)
      Stars × 15      — quality of learning (high quiz scores earn more stars)
      Lessons × 20    — breadth of progress (completing more lessons)
      Streak × 5      — consistency (daily learning habit)
    """
    return xp + (stars * 15) + (lessons_completed * 20) + (streak * 5)


def _get_period_start(period: LeaderboardPeriod) -> Optional[datetime]:
    """Return the start datetime for the given period filter."""
    now = datetime.utcnow()
    if period == LeaderboardPeriod.week:
        # Start of current week (Monday)
        start = now - timedelta(days=now.weekday())
        return start.replace(hour=0, minute=0, second=0, microsecond=0)
    elif period == LeaderboardPeriod.month:
        return now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return None


@router.get("/leaderboard/filters", response_model=LeaderboardFiltersResponse)
def get_leaderboard_filters(
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.student)),
):
    """Return available grade options for the leaderboard filter."""
    grades = db.query(Grade).order_by(Grade.number).all()
    return LeaderboardFiltersResponse(
        grades=[GradeOption(id=g.id, number=g.number, name=g.name) for g in grades]
    )


@router.get("/leaderboard", response_model=LeaderboardResponse)
def get_leaderboard(
    period: LeaderboardPeriod = Query(LeaderboardPeriod.all_time, description="Filter period"),
    grade_id: Optional[UUID] = Query(None, description="Filter by grade ID"),
    db: Session = Depends(get_db),
    user: User = Depends(require_role(UserRole.student)),
):
    """
    Get leaderboard with optional filters.
    - period: week / month / all
    - grade_id: filter by specific grade
    Only students can access this endpoint.
    """
    students = db.query(User).filter(User.role == UserRole.student).all()
    period_start = _get_period_start(period)

    entries = []
    for student in students:
        # Build the base query for completed lessons
        progress_query = db.query(StudentProgress).filter(
            StudentProgress.student_id == student.id,
            StudentProgress.status == ProgressStatus.completed,
        )

        # Apply period filter
        if period_start is not None:
            progress_query = progress_query.filter(
                StudentProgress.completed_at >= period_start
            )

        # Apply grade filter by joining through Lesson -> Chapter -> Grade
        if grade_id is not None:
            progress_query = progress_query.join(
                Lesson, StudentProgress.lesson_id == Lesson.id
            ).join(
                Chapter, Lesson.chapter_id == Chapter.id
            ).filter(
                Chapter.grade_id == grade_id
            )

        # Get filtered progress records
        progress_records = progress_query.all()
        lessons_completed = len(progress_records)

        if period == LeaderboardPeriod.all_time and grade_id is None:
            # Use cumulative user stats for all-time without grade filter
            ranking_score = _compute_ranking_score(
                xp=student.xp,
                stars=student.stars,
                lessons_completed=lessons_completed,
                streak=student.streak,
            )
            stars_display = student.stars
        else:
            # Compute from filtered progress data
            filtered_stars = sum(p.stars_earned for p in progress_records)
            filtered_xp = sum(p.best_score for p in progress_records)
            ranking_score = _compute_ranking_score(
                xp=filtered_xp,
                stars=filtered_stars,
                lessons_completed=lessons_completed,
                streak=student.streak,
            )
            stars_display = filtered_stars

        entries.append({
            "student_id": student.id,
            "name": student.name,
            "avatar_url": student.avatar_url,
            "level": student.level,
            "xp": student.xp,
            "stars": stars_display,
            "streak": student.streak,
            "coins": student.coins,
            "lessons_completed": lessons_completed,
            "ranking_score": ranking_score,
            "is_current_user": student.id == user.id,
        })

    # Sort by ranking_score descending, then by xp, then by name
    entries.sort(key=lambda e: (-e["ranking_score"], -e["xp"], e["name"]))

    # Assign ranks
    current_user_entry = None
    for i, entry in enumerate(entries):
        entry["rank"] = i + 1
        if entry["is_current_user"]:
            current_user_entry = LeaderboardEntry(**entry)

    # Return top 10 for the response (top 3 podium + remaining in list)
    leaderboard = [LeaderboardEntry(**e) for e in entries[:10]]

    return LeaderboardResponse(
        leaderboard=leaderboard,
        current_user_rank=current_user_entry,
        total_students=len(entries),
    )
