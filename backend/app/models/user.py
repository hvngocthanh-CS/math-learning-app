import uuid
import enum
from datetime import datetime
from sqlalchemy import Column, String, Integer, Enum, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class UserRole(str, enum.Enum):
    student = "student"
    parent = "parent"
    teacher = "teacher"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.student)
    avatar_url = Column(String, nullable=True)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    stars = Column(Integer, default=0)
    coins = Column(Integer, default=0)
    streak = Column(Integer, default=0)
    last_login_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
