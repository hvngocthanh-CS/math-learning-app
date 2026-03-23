"""Learn endpoints: grades, chapters, lessons, content, completion."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.learn import (
    GradeResponse, ChapterDetailResponse, LessonResponse,
    LessonDetailResponse, LessonContentResponse,
    LessonCompleteRequest, LessonCompleteResponse,
)
from app.services import learn_service

router = APIRouter(tags=["learn"])


@router.get("/grades", response_model=List[GradeResponse])
def list_grades(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return learn_service.list_grades(db, user.id)


@router.get("/grades/{grade_id}/chapters", response_model=List[ChapterDetailResponse])
def get_grade_chapters(grade_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    result = learn_service.get_grade_chapters(db, grade_id, user.id)
    if result is None:
        raise HTTPException(status_code=404, detail="Grade not found")
    return result


@router.get("/chapters/{chapter_id}/lessons", response_model=List[LessonResponse])
def get_chapter_lessons(chapter_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    result = learn_service.get_chapter_lessons(db, chapter_id, user.id)
    if result is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return result


@router.get("/lessons/{lesson_id}", response_model=LessonDetailResponse)
def get_lesson_detail(lesson_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    result = learn_service.get_lesson_detail(db, lesson_id, user.id)
    if result is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return result


@router.get("/lessons/{lesson_id}/content", response_model=LessonContentResponse)
def get_lesson_content(lesson_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    result = learn_service.get_lesson_content(db, lesson_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Lesson content not found")
    return result


@router.post("/lessons/{lesson_id}/complete", response_model=LessonCompleteResponse)
def complete_lesson(lesson_id: UUID, body: LessonCompleteRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    result = learn_service.complete_lesson(db, lesson_id, body.quiz_score, body.total_questions, user)
    if result is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return result
