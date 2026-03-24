from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.api.v1 import auth, learn, dashboard, users, progress, leaderboard

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MathQuest API",
    description="Backend API for MathQuest - A Math Learning App",
    version="1.0.0",
    redirect_slashes=False,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# All API routes under /api/v1
app.include_router(auth.router, prefix="/api/v1")
app.include_router(learn.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(progress.router, prefix="/api/v1")
app.include_router(leaderboard.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Welcome to MathQuest API", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}
