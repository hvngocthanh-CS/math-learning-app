"""User management endpoints (teacher only)."""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from app.core.deps import get_db, get_current_user, require_role
from app.core.security import hash_password
from app.models.user import User, UserRole
from app.models.progress import StudentProgress, QuizAnswer, DailyMission
from app.schemas.auth import UserCreate, UserResponse
from app.services.auth_service import register_user, get_user_by_email


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    add_student_ids: Optional[List[UUID]] = None  # Link more students to this parent

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

    # If creating a parent, link selected students to this parent
    if payload.role == UserRole.parent and payload.student_ids:
        for sid in payload.student_ids:
            student = db.query(User).filter(User.id == sid, User.role == UserRole.student).first()
            if student:
                student.parent_id = new_user.id
        db.commit()
        db.refresh(new_user)

    # If creating a student, link to an existing parent
    if payload.role == UserRole.student and payload.parent_id:
        parent = db.query(User).filter(User.id == payload.parent_id, User.role == UserRole.parent).first()
        if parent:
            new_user.parent_id = parent.id
            db.commit()
            db.refresh(new_user)

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


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: str, payload: UserUpdate, db: Session = Depends(get_db), user: User = Depends(require_role(UserRole.teacher))):
    try:
        uid = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID")
    found = db.query(User).filter(User.id == uid).first()
    if not found:
        raise HTTPException(status_code=404, detail="User not found")
    if found.role == UserRole.teacher:
        raise HTTPException(status_code=403, detail="Cannot edit teacher accounts")

    if payload.name is not None:
        found.name = payload.name.strip()
    if payload.email is not None:
        existing = get_user_by_email(db, payload.email.strip())
        if existing and existing.id != found.id:
            raise HTTPException(status_code=400, detail="Email already in use")
        found.email = payload.email.strip()
    if payload.password is not None:
        if len(payload.password) < 6:
            raise HTTPException(status_code=400, detail="Password must be at least 6 characters")
        found.password_hash = hash_password(payload.password)

    # Link additional students to this parent
    if payload.add_student_ids and found.role == UserRole.parent:
        for sid in payload.add_student_ids:
            student = db.query(User).filter(User.id == sid, User.role == UserRole.student).first()
            if student:
                student.parent_id = found.id

    db.commit()
    db.refresh(found)
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

    # Delete related data first to avoid FK constraint errors
    db.query(QuizAnswer).filter(QuizAnswer.student_id == uid).delete()
    db.query(StudentProgress).filter(StudentProgress.student_id == uid).delete()
    db.query(DailyMission).filter(DailyMission.student_id == uid).delete()

    # If deleting a parent, unlink their children
    if found.role == UserRole.parent:
        db.query(User).filter(User.parent_id == uid).update({"parent_id": None})

    # If deleting a student, clear parent_id reference
    if found.role == UserRole.student and found.parent_id:
        pass  # no action needed, just delete the student

    db.delete(found)
    db.commit()
