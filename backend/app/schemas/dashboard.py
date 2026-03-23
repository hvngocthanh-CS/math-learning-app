from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import date
from app.models.progress import MissionType


class DailyMissionResponse(BaseModel):
    id: UUID
    title: str
    target_value: int
    current_value: int
    mission_type: MissionType
    date: date
    is_completed: bool

    class Config:
        from_attributes = True


class UserBriefDashboard(BaseModel):
    id: UUID
    name: str
    avatar_url: Optional[str] = None
    level: int
    xp: int
    stars: int
    coins: int
    streak: int

    class Config:
        from_attributes = True


class RecommendedLesson(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    content_type: str
    chapter_title: Optional[str] = None
    grade_name: Optional[str] = None

    class Config:
        from_attributes = True


class DashboardResponse(BaseModel):
    user: UserBriefDashboard
    daily_missions: List[DailyMissionResponse]
    recommended_lessons: List[RecommendedLesson]
