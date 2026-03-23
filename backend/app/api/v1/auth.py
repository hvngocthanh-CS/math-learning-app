"""Auth endpoints: register, login, me."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.core.config import get_settings
from app.core.security import create_access_token
from app.models.user import User, UserRole
from app.schemas.auth import UserCreate, UserLogin, UserResponse, TokenResponse, RegisterResponse
from app.services.auth_service import register_user, authenticate_user, get_user_by_email, AuthError

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if payload.role != UserRole.teacher:
        raise HTTPException(status_code=403, detail="Only teachers can register. Students/parents must be created by a teacher.")
    settings = get_settings()
    if not payload.teacher_code or payload.teacher_code != settings.TEACHER_REGISTER_CODE:
        raise HTTPException(status_code=403, detail="Invalid teacher registration code.")
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = register_user(db, payload.email, payload.name, payload.password, payload.role)
    return RegisterResponse(user=UserResponse.model_validate(user))


@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    try:
        user = authenticate_user(db, payload.email, payload.password)
    except AuthError as e:
        raise HTTPException(status_code=401, detail=e.message)
    return TokenResponse(access_token=create_access_token(str(user.id)), user=UserResponse.model_validate(user))


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return UserResponse.model_validate(current_user)
