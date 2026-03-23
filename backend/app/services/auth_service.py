"""Auth business logic: registration, authentication, user lookup."""

from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.models.user import User, UserRole


def register_user(db: Session, email: str, name: str, password: str, role: UserRole) -> User:
    user = User(
        email=email,
        name=name,
        password_hash=hash_password(password),
        role=role,
        last_login_date=date.today(),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


class AuthError(Exception):
    def __init__(self, message: str):
        self.message = message


def authenticate_user(db: Session, email: str, password: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise AuthError("No account found with this email.")
    if not verify_password(password, user.password_hash):
        raise AuthError("Incorrect password. Please try again.")
    # Update streak
    today = date.today()
    if user.last_login_date:
        diff = (today - user.last_login_date).days
        user.streak = user.streak + 1 if diff == 1 else 1 if diff > 1 else user.streak
    else:
        user.streak = 1
    user.last_login_date = today
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(db: Session, user_id: str) -> Optional[User]:
    try:
        return db.query(User).filter(User.id == UUID(user_id)).first()
    except ValueError:
        return None


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()
