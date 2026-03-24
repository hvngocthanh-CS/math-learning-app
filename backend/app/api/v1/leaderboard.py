"""Leaderboard endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

from app.core.deps import get_db, get_current_user
from app.models.user import User, UserRole
from app.models.progress import StudentProgress, ProgressStatus

router = APIRouter(tags=["leaderboard"])


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

    class Config:
        from_attributes = True


class LeaderboardResponse(BaseModel):
    leaderboard: List[LeaderboardEntry]
    current_user_rank: Optional[LeaderboardEntry] = None


def _compute_ranking_score(xp: int, stars: int, lessons_completed: int, streak: int) -> int:
    """
    Ranking formula:
      XP              — overall effort (1 point per XP)
      Stars × 15      — quality of learning (high quiz scores earn more stars)
      Lessons × 20    — breadth of progress (completing more lessons)
      Streak × 5      — consistency (daily learning habit)
    """
    return xp + (stars * 15) + (lessons_completed * 20) + (streak * 5)


@router.get("/leaderboard", response_model=LeaderboardResponse)
def get_leaderboard(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # Get all students with their completed lesson count
    students = db.query(User).filter(User.role == UserRole.student).all()

    entries = []
    for student in students:
        lessons_completed = (
            db.query(func.count(StudentProgress.id))
            .filter(
                StudentProgress.student_id == student.id,
                StudentProgress.status == ProgressStatus.completed,
            )
            .scalar()
        ) or 0

        ranking_score = _compute_ranking_score(
            xp=student.xp,
            stars=student.stars,
            lessons_completed=lessons_completed,
            streak=student.streak,
        )

        entries.append({
            "student_id": student.id,
            "name": student.name,
            "avatar_url": student.avatar_url,
            "level": student.level,
            "xp": student.xp,
            "stars": student.stars,
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

    leaderboard = [LeaderboardEntry(**e) for e in entries]

    return LeaderboardResponse(
        leaderboard=leaderboard,
        current_user_rank=current_user_entry,
    )
