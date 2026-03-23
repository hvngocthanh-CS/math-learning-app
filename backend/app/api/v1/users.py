"""User management endpoints (teacher only)."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.deps import get_db, get_current_user, require_role
from app.models.user import User, UserRole
from app.schemas.auth import UserCreate, UserResponse
from app.services.auth_service import register_user, get_user_by_email

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=List[UserResponse])
def list_users(role: UserRole = None, db: Session = Depends(get_db), user: User = Depends(require_role(UserRole.teacher))):
    query = db.query(User)
    if role:
        query = query.filter(User.role == role)
    return [UserResponse.model_validate(u) for u in query.order_by(User.created_at.desc()).all()]


@router.post("/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db), user: User = Depends(require_role(UserRole.teacher))):
    if payload.role == UserRole.teacher:
        raise HTTPException(status_code=403, detail="Teachers cannot create other teacher accounts")
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = register_user(db, payload.email, payload.name, payload.password, payload.role)
    return UserResponse.model_validate(new_user)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        uid = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    found = db.query(User).filter(User.id == uid).first()
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(found)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db), user: User = Depends(require_role(UserRole.teacher))):
    try:
        uid = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    found = db.query(User).filter(User.id == uid).first()
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    if found.role == UserRole.teacher:
        raise HTTPException(status_code=403, detail="Cannot delete teacher accounts")
    db.delete(found)
    db.commit()
