"""Student progress endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.progress import StudentProgressSummary
from app.services.progress_service import get_student_progress

router = APIRouter(tags=["progress"])


@router.get("/student/progress", response_model=StudentProgressSummary)
def student_progress(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_student_progress(db, user)
