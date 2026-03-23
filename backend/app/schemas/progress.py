from pydantic import BaseModel
from typing import List
from uuid import UUID


class GradeProgressResponse(BaseModel):
    grade_id: UUID
    grade_name: str
    grade_number: int
    total_lessons: int
    completed_lessons: int
    total_stars: int
    earned_stars: int


class StudentProgressSummary(BaseModel):
    total_lessons_completed: int
    total_stars_earned: int
    total_xp: int
    current_level: int
    grades: List[GradeProgressResponse]
