# math-learning-app
A math learning app for students from Grade 1 to Grade 5, offering auto-generated exercises tailored to each level. It tracks progress, evaluates performance, and adapts to each learner’s pace. With a simple interface and engaging rewards, it makes daily math practice effective, personalized, and enjoyable.


# MathQuest Backend (Python/FastAPI)

## Cấu trúc thư mục

```
backend/
├── .env                          # Biến môi trường (DB, JWT, ...)
├── requirements.txt              # Danh sách thư viện Python
└── app/
    ├── main.py                   # Entry point - khởi tạo FastAPI, CORS, đăng ký routes
    ├── seed.py                   # Script tạo dữ liệu mẫu (grades, lessons, demo users)
    │
    ├── core/                     # Cấu hình hệ thống
    │   ├── config.py             # Đọc .env → Settings (DATABASE_URL, JWT_SECRET, ...)
    │   ├── database.py           # Kết nối PostgreSQL (SQLAlchemy engine, session)
    │   ├── security.py           # Hash password (bcrypt), tạo/giải mã JWT token
    │   └── deps.py               # Dependencies dùng chung: get_current_user, require_role
    │
    ├── models/                   # Định nghĩa bảng DB (SQLAlchemy ORM)
    │   ├── user.py               # Bảng users: id, email, name, role, xp, stars, coins, streak, parent_id
    │   ├── grade.py              # Bảng grades: id, number, name (Grade 1-5)
    │   ├── lesson.py             # Bảng chapters, lessons, lesson_contents (nội dung bài học)
    │   └── progress.py           # Bảng student_progress, quiz_answers, daily_missions
    │
    ├── schemas/                  # Validate dữ liệu request/response (Pydantic)
    │   ├── auth.py               # UserCreate, UserLogin, UserResponse, TokenResponse
    │   ├── learn.py              # GradeResponse, LessonResponse, LessonCompleteRequest/Response
    │   ├── dashboard.py          # DashboardResponse, DailyMissionResponse
    │   └── progress.py           # StudentProgressSummary, GradeProgressResponse
    │
    ├── services/                 # Business logic (xử lý nghiệp vụ)
    │   ├── auth_service.py       # Đăng ký, đăng nhập, cập nhật streak
    │   ├── learn_service.py      # Lấy grades/chapters/lessons, hoàn thành bài, tính điểm
    │   ├── dashboard_service.py  # Tạo daily missions, gợi ý bài học
    │   └── progress_service.py   # Tổng hợp tiến độ học sinh theo grade
    │
    ├── api/v1/                   # API endpoints (routes)
    │   ├── auth.py               # POST /auth/register, /auth/login, GET /auth/me
    │   ├── users.py              # CRUD tài khoản (teacher tạo student/parent, edit, xóa)
    │   ├── learn.py              # GET grades, chapters, lessons, POST complete lesson
    │   ├── dashboard.py          # GET /dashboard (student)
    │   ├── progress.py           # GET /student/progress
    │   ├── leaderboard.py        # GET /leaderboard (xếp hạng theo week/month/grade)
    │   ├── teacher.py            # GET /teacher/dashboard, /students, /ranking
    │   └── parent.py             # GET /parent/dashboard (xem tiến độ con)
    │
    └── features/learn/           # Logic tạo bài tập
        ├── generators/           # Sinh đề toán tự động theo grade (Grade 1-5)
        │   ├── __init__.py       # Registry pattern: đăng ký và dispatch generators
        │   ├── grade1/           # Cộng, trừ, so sánh, hình học cơ bản
        │   ├── grade2/           # Nhân, chia, đo lường, thời gian
        │   ├── grade3/           # Phân số, hình học, ước lượng
        │   ├── grade4/           # Số thập phân, góc, diện tích
        │   └── grade5/           # Phần trăm, tỷ lệ, hình tròn
        └── seed_data/            # Dữ liệu nội dung bài học (explanation, examples, quiz)
            ├── grade1.py
            ├── grade2.py
            ├── grade3.py
            ├── grade4.py
            └── grade5.py
```

## Mục đích từng layer

### models/ — Bảng Database
Map trực tiếp với PostgreSQL. Mỗi class = 1 bảng.

| Model | Bảng | Mục đích |
|-------|------|----------|
| `User` | users | Thông tin user (student/teacher/parent), điểm, level, liên kết parent-child |
| `Grade` | grades | 5 cấp lớp (Grade 1-5) |
| `Chapter` | chapters | Chương trong mỗi grade |
| `Lesson` | lessons | Bài học trong mỗi chapter |
| `LessonContent` | lesson_contents | Nội dung bài: giải thích, ví dụ, bài tập |
| `StudentProgress` | student_progress | Tiến độ học sinh: điểm, sao, số lần làm |
| `QuizAnswer` | quiz_answers | Từng câu trả lời đúng/sai của học sinh |
| `DailyMission` | daily_missions | Nhiệm vụ hằng ngày |

### schemas/ — Validate Input/Output
Lọc dữ liệu giữa client và server. Không cho client gửi bậy hoặc nhận được thông tin nhạy cảm (như password_hash).

### services/ — Business Logic
Xử lý nghiệp vụ: tính điểm, cấp sao, mở bài tiếp theo, cập nhật streak. Tách riêng khỏi API route để dễ maintain.

### api/v1/ — API Endpoints
Nhận request → gọi service → trả response. Mỗi file quản lý 1 nhóm chức năng.

## Flow dữ liệu

```
Client request
    ↓
api/v1/ (route)      → Nhận request, validate bằng schema
    ↓
services/ (logic)    → Xử lý nghiệp vụ
    ↓
models/ (DB)         → Đọc/ghi PostgreSQL
    ↓
schemas/ (response)  → Format response, giấu thông tin nhạy cảm
    ↓
Client nhận response
```

## Quan hệ Database

```
User (1) ──→ (N) StudentProgress
User (1) ──→ (N) QuizAnswer
User (1) ──→ (N) DailyMission
User (parent) (1) ←── (N) User (student)    [parent_id FK]

Grade (1) ──→ (N) Chapter
Chapter (1) ──→ (N) Lesson
Lesson (1) ──→ (1) LessonContent
Lesson (1) ──→ (N) StudentProgress
Lesson (1) ──→ (N) QuizAnswer
```

## Setup

1. Tạo virtual environment:
```bash
python3.10 -m venv myenv
source myenv/bin/activate       # Linux
myenv\Scripts\activate          # Windows
```

2. Cài dependencies:
```bash
pip install -r requirements.txt
```

3. Tạo file `.env`:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mathquest
JWT_SECRET=your-secret-key
JWT_ALGORITHM=HS256
JWT_EXPIRE_HOURS=24
TEACHER_REGISTER_CODE=MATHQUEST2026
```

4. Seed dữ liệu:
```bash
python -m app.seed              # Tạo data lần đầu
python -m app.seed --update     # Cập nhật nội dung bài học
python -m app.seed --reset      # Xóa hết và tạo lại (DESTRUCTIVE)
```

5. Chạy server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Demo Accounts

- **Teacher**: teacher@mathquest.com / password123
- **Student**: student@mathquest.com / password123

## API Endpoints

### Auth
- `POST /api/v1/auth/register` — Đăng ký (teacher, cần code)
- `POST /api/v1/auth/login` — Đăng nhập → JWT token
- `GET /api/v1/auth/me` — Thông tin user hiện tại

### Users (Teacher only)
- `GET /api/v1/users` — Danh sách users
- `POST /api/v1/users/create` — Tạo student/parent
- `PUT /api/v1/users/{id}` — Sửa thông tin, link student-parent
- `DELETE /api/v1/users/{id}` — Xóa user

### Learn
- `GET /api/v1/grades` — Danh sách grades
- `GET /api/v1/grades/{id}/chapters` — Chapters trong grade
- `GET /api/v1/chapters/{id}/lessons` — Lessons trong chapter
- `GET /api/v1/lessons/{id}` — Chi tiết bài học
- `GET /api/v1/lessons/{id}/content` — Nội dung bài (đề bài, quiz)
- `POST /api/v1/lessons/{id}/complete` — Hoàn thành bài, tính điểm

### Dashboard & Progress
- `GET /api/v1/dashboard` — Dashboard student
- `GET /api/v1/student/progress` — Tiến độ theo grade

### Leaderboard (Student only)
- `GET /api/v1/leaderboard?period=week&grade_id=xxx` — Xếp hạng
- `GET /api/v1/leaderboard/filters` — Danh sách grades cho filter

### Teacher
- `GET /api/v1/teacher/dashboard` — Thống kê tổng quan
- `GET /api/v1/teacher/students` — Danh sách students + tiến độ
- `GET /api/v1/teacher/students/{id}/progress` — Chi tiết từng câu đúng/sai
- `GET /api/v1/teacher/ranking` — Bảng xếp hạng toàn bộ

### Parent
- `GET /api/v1/parent/dashboard` — Tiến độ con (chỉ xem con mình)

