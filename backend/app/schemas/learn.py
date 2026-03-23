from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from app.models.lesson import ContentType
from app.models.progress import ProgressStatus


class GradeResponse(BaseModel):
    id: UUID
    number: int
    name: str
    description: Optional[str] = None
    icon_url: Optional[str] = None
    total_chapters: int = 0
    total_lessons: int = 0
    completed_lessons: int = 0

    class Config:
        from_attributes = True


class LessonBriefResponse(BaseModel):
    id: UUID
    title: str
    order: int
    description: Optional[str] = None
    xp_reward: int = 20
    status: ProgressStatus = ProgressStatus.locked
    stars_earned: int = 0
    score: int = 0

    class Config:
        from_attributes = True


class ChapterDetailResponse(BaseModel):
    id: UUID
    grade_id: UUID
    title: str
    order: int
    description: Optional[str] = None
    total_lessons: int = 0
    completed_lessons: int = 0
    lessons: List[LessonBriefResponse] = []

    class Config:
        from_attributes = True


class LessonResponse(BaseModel):
    id: UUID
    chapter_id: UUID
    title: str
    order: int
    content_type: ContentType = ContentType.video
    content_url: Optional[str] = None
    description: Optional[str] = None
    is_locked: bool = True
    status: ProgressStatus = ProgressStatus.locked
    score: int = 0
    stars_earned: int = 0

    class Config:
        from_attributes = True


class LessonDetailResponse(LessonResponse):
    chapter_title: Optional[str] = None
    grade_name: Optional[str] = None


class LessonContentResponse(BaseModel):
    explanation: str
    examples: list
    steps: list
    fun_fact: str
    practice_problems: list
    quiz_problems: list

    class Config:
        from_attributes = True


class LessonCompleteRequest(BaseModel):
    quiz_score: int
    total_questions: int = 5


class LessonCompleteResponse(BaseModel):
    stars_earned: int
    xp_earned: int
    coins_earned: int
    next_lesson_id: Optional[str] = None
    level_up: bool = False
