import uuid
import enum
from sqlalchemy import Column, String, Integer, Boolean, Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.core.database import Base


class ContentType(str, enum.Enum):
    video = "video"
    slide = "slide"


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    grade_id = Column(UUID(as_uuid=True), ForeignKey("grades.id"), nullable=False)
    title = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    description = Column(String, nullable=True)

    grade = relationship("Grade", back_populates="chapters")
    lessons = relationship("Lesson", back_populates="chapter", order_by="Lesson.order")


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id"), nullable=False)
    title = Column(String, nullable=False)
    order = Column(Integer, nullable=False)
    content_type = Column(Enum(ContentType), nullable=False, default=ContentType.video)
    content_url = Column(String, nullable=True)
    description = Column(String, nullable=True)
    is_locked = Column(Boolean, default=True)
    xp_reward = Column(Integer, default=20)

    chapter = relationship("Chapter", back_populates="lessons")
    content = relationship("LessonContent", uselist=False, back_populates="lesson")


class LessonContent(Base):
    __tablename__ = "lesson_contents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"), unique=True, nullable=False)
    explanation = Column(Text, nullable=False)
    examples = Column(JSONB, nullable=True)
    steps = Column(JSONB, nullable=True)
    fun_fact = Column(String, nullable=True)
    practice_problems = Column(JSONB, nullable=True)
    quiz_problems = Column(JSONB, nullable=True)
    problem_config = Column(JSONB, nullable=True)

    lesson = relationship("Lesson", back_populates="content")
