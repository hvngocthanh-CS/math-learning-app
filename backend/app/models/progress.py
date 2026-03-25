import uuid
import enum
from datetime import datetime, date
from sqlalchemy import Column, String, Integer, Boolean, Enum, ForeignKey, DateTime, Date
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base


class ProgressStatus(str, enum.Enum):
    locked = "locked"
    in_progress = "in_progress"
    completed = "completed"


class MissionType(str, enum.Enum):
    lessons = "lessons"
    stars = "stars"
    games = "games"


class StudentProgress(Base):
    __tablename__ = "student_progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"), nullable=False, index=True)
    status = Column(Enum(ProgressStatus), nullable=False, default=ProgressStatus.locked)
    score = Column(Integer, default=0)
    stars_earned = Column(Integer, default=0)
    attempts = Column(Integer, default=0)
    best_score = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)


class QuizAnswer(Base):
    """Tracks individual question responses for each quiz attempt."""
    __tablename__ = "quiz_answers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"), nullable=False, index=True)
    question_text = Column(String, nullable=False)
    student_answer = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    attempted_at = Column(DateTime, default=datetime.utcnow)


class DailyMission(Base):
    __tablename__ = "daily_missions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    target_value = Column(Integer, nullable=False)
    current_value = Column(Integer, default=0)
    mission_type = Column(Enum(MissionType), nullable=False)
    date = Column(Date, nullable=False, default=date.today)
    is_completed = Column(Boolean, default=False)
