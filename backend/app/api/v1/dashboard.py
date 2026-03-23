"""Dashboard endpoint."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import get_dashboard

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_dashboard(db, user)
