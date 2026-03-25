from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime, date
from app.models.user import UserRole


class UserCreate(BaseModel):
    email: str
    name: str
    password: str = Field(..., min_length=6)
    role: UserRole = UserRole.student
    teacher_code: Optional[str] = None
    student_ids: Optional[List[UUID]] = None  # When creating parent, link to these students
    parent_id: Optional[UUID] = None  # When creating student, link to this parent


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    name: str
    role: UserRole
    avatar_url: Optional[str] = None
    level: int
    xp: int
    stars: int
    coins: int
    streak: int
    last_login_date: Optional[date] = None
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[UUID] = None

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class RegisterResponse(BaseModel):
    message: str = "Registration successful. Please log in."
    user: UserResponse
