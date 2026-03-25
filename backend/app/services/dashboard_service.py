"""Dashboard business logic: daily missions, recommendations."""

from datetime import date
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.lesson import Lesson, Chapter
from app.models.grade import Grade
from app.models.progress import DailyMission, StudentProgress, ProgressStatus, MissionType
from sqlalchemy import func
from app.schemas.dashboard import (
    DashboardResponse, DailyMissionResponse,
    RecommendedLesson, UserBriefDashboard, DashboardStats,
)


def get_dashboard(db: Session, user: User) -> DashboardResponse:
    missions = _get_or_create_daily_missions(db, user.id)
    recommended = _get_recommended_lessons(db, user.id)

    lessons_completed = (
        db.query(func.count(StudentProgress.id))
        .filter(
            StudentProgress.student_id == user.id,
            StudentProgress.status == ProgressStatus.completed,
        )
        .scalar()
    ) or 0

    total_stars = (
        db.query(func.coalesce(func.sum(StudentProgress.stars_earned), 0))
        .filter(StudentProgress.student_id == user.id)
        .scalar()
    ) or 0

    return DashboardResponse(
        user=UserBriefDashboard(
            id=user.id, name=user.name, avatar_url=user.avatar_url,
            level=user.level, xp=user.xp, stars=user.stars,
            coins=user.coins, streak=user.streak,
        ),
        daily_missions=[DailyMissionResponse.model_validate(m) for m in missions],
        recommended_lessons=recommended,
        stats=DashboardStats(
            lessons_completed=lessons_completed,
            total_stars=total_stars,
        ),
    )


def _get_or_create_daily_missions(db: Session, student_id):
    today = date.today()
    missions = db.query(DailyMission).filter(
        DailyMission.student_id == student_id, DailyMission.date == today,
    ).all()
    if not missions:
        missions = [
            DailyMission(student_id=student_id, title="Complete 3 Lessons",
                         target_value=3, current_value=0, mission_type=MissionType.lessons, date=today),
            DailyMission(student_id=student_id, title="Earn 5 Stars",
                         target_value=5, current_value=0, mission_type=MissionType.stars, date=today),
            DailyMission(student_id=student_id, title="Play 2 Games",
                         target_value=2, current_value=0, mission_type=MissionType.games, date=today),
        ]
        db.add_all(missions)
        db.commit()
    return missions


def _get_recommended_lessons(db: Session, student_id, limit: int = 5):
    completed_ids = db.query(StudentProgress.lesson_id).filter(
        StudentProgress.student_id == student_id,
        StudentProgress.status == ProgressStatus.completed,
    ).subquery()
    rows = (
        db.query(Lesson, Chapter.title.label("ch_title"), Grade.name.label("g_name"))
        .join(Chapter, Lesson.chapter_id == Chapter.id)
        .join(Grade, Chapter.grade_id == Grade.id)
        .filter(Lesson.id.notin_(completed_ids))
        .order_by(Grade.number, Chapter.order, Lesson.order)
        .limit(limit).all()
    )
    return [
        RecommendedLesson(id=l.id, title=l.title, description=l.description,
                          content_type=l.content_type.value, chapter_title=ct, grade_name=gn)
        for l, ct, gn in rows
    ]
