# TÀI LIỆU HỆ THỐNG BACKEND - MATHQUEST

## Mục lục

1. [Giới thiệu ứng dụng](#1-giới-thiệu-ứng-dụng)
2. [Công nghệ sử dụng](#2-công-nghệ-sử-dụng)
3. [Kiến trúc tổng quan](#3-kiến-trúc-tổng-quan)
4. [Cấu trúc thư mục Backend](#4-cấu-trúc-thư-mục-backend)
5. [Chi tiết từng thành phần](#5-chi-tiết-từng-thành-phần)
6. [Cơ sở dữ liệu](#6-cơ-sở-dữ-liệu)
7. [Luồng hoạt động chính](#7-luồng-hoạt-động-chính)
8. [Danh sách API](#8-danh-sách-api)
9. [Hướng dẫn cài đặt và triển khai](#9-hướng-dẫn-cài-đặt-và-triển-khai)

---

## 1. Giới thiệu ứng dụng

### MathQuest là gì?

MathQuest là ứng dụng học toán dành cho học sinh từ Lớp 1 đến Lớp 5. Ứng dụng tự động sinh đề bài toán phù hợp với từng cấp lớp, theo dõi tiến độ học tập, và tạo động lực học qua hệ thống phần thưởng (sao, XP, coins).

### Các vai trò trong hệ thống

| Vai trò | Mô tả | Quyền hạn |
|---------|-------|-----------|
| **Student (Học sinh)** | Người dùng chính của ứng dụng | Học bài, làm quiz, chơi game, xem bảng xếp hạng |
| **Teacher (Giáo viên)** | Quản lý lớp học | Tạo tài khoản student/parent, theo dõi tiến độ tất cả học sinh, xem bảng xếp hạng |
| **Parent (Phụ huynh)** | Theo dõi con em | Xem điểm số, tiến độ, chi tiết từng câu đúng/sai của con mình (không xem được học sinh khác) |

### Các tính năng chính

- **Learn (Học)**: 5 lớp × nhiều chương × nhiều bài học. Mỗi bài có: giải thích → ví dụ → luyện tập → kiểm tra
- **Play (Chơi)**: 2 game toán học - Math Pop (bắn bong bóng) và Math Memory (lật thẻ nhớ)
- **Rank (Xếp hạng)**: Bảng xếp hạng lọc theo tuần/tháng/lớp
- **Theo dõi tiến độ**: Ghi nhận từng câu trả lời đúng/sai, sao, XP, coins, chuỗi ngày học liên tục (streak)
- **Tự động sinh đề**: Đề toán được tạo tự động theo cấp lớp, không lặp lại

---

## 2. Công nghệ sử dụng

### Backend (Phần máy chủ)

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| **Python** | 3.10 | Ngôn ngữ lập trình chính |
| **FastAPI** | 0.109.0 | Framework xây dựng REST API. Tự động tạo tài liệu API (Swagger), hỗ trợ async, nhanh |
| **SQLAlchemy** | 2.0.25 | ORM (Object-Relational Mapping) - cho phép thao tác database bằng code Python thay vì viết SQL trực tiếp |
| **PostgreSQL** | 14+ | Hệ quản trị cơ sở dữ liệu quan hệ, lưu trữ tất cả dữ liệu của ứng dụng |
| **Pydantic** | 2.5.3 | Kiểm tra và validate dữ liệu đầu vào/đầu ra của API |
| **python-jose** | 3.3.0 | Tạo và giải mã JWT token cho xác thực người dùng |
| **passlib + bcrypt** | 1.7.4 | Mã hóa mật khẩu (hash) - không lưu mật khẩu gốc trong database |
| **Uvicorn** | 0.27.0 | ASGI server - chạy ứng dụng FastAPI |

### Frontend (Phần giao diện)

| Công nghệ | Mục đích |
|-----------|----------|
| **React 18** | Thư viện xây dựng giao diện người dùng |
| **Vite** | Công cụ build và chạy dev server |
| **Tailwind CSS** | Framework CSS để tạo giao diện nhanh |
| **Framer Motion** | Tạo hiệu ứng animation |
| **Axios** | Thư viện gọi API từ frontend |
| **React Router v6** | Điều hướng trang (routing) |

### Giải thích đơn giản

- **FastAPI**: Giống như "bộ não" xử lý mọi yêu cầu từ người dùng. Khi học sinh bấm "Hoàn thành bài", FastAPI nhận yêu cầu đó, tính điểm, lưu kết quả, rồi trả lại kết quả cho học sinh xem.
- **PostgreSQL**: Giống như "kho lưu trữ" chứa tất cả thông tin: tài khoản người dùng, bài học, điểm số, tiến độ...
- **SQLAlchemy**: Giống như "người phiên dịch" giữa Python và PostgreSQL. Thay vì viết câu lệnh SQL thủ công, ta viết code Python và SQLAlchemy tự dịch sang SQL.
- **JWT Token**: Giống như "vé vào cửa". Khi đăng nhập thành công, server cấp một token (mã). Mỗi lần gọi API, frontend gửi kèm token này để chứng minh "tôi đã đăng nhập rồi".

---

## 3. Kiến trúc tổng quan

### Sơ đồ hệ thống

```
┌─────────────────────────────┐              ┌──────────────────────────────┐
│    FRONTEND (React)         │              │     BACKEND (FastAPI)        │
│                             │    HTTP      │                              │
│  https://mathquest.aipower  │─────────────→│  https://mathquest-api       │
│  .vn                        │    JSON      │  .aipower.vn                 │
│                             │←─────────────│                              │
│  Chạy trên trình duyệt     │              │  Chạy trên server            │
│  (HTML + CSS + JavaScript)  │              │  (Python, port 8080)         │
│                             │              │           │                  │
│  Server: 192.168.1.250      │              │           ▼                  │
│  (file tĩnh)                │              │  ┌──────────────────┐        │
└─────────────────────────────┘              │  │   PostgreSQL     │        │
                                             │  │   (port 5432)    │        │
                                             │  │   Lưu dữ liệu   │        │
                                             │  └──────────────────┘        │
                                             │  Server: 192.168.1.239      │
                                             └──────────────────────────────┘
```

### Luồng request (yêu cầu) cơ bản

```
1. Người dùng mở trình duyệt → tải trang React (HTML/CSS/JS) từ server file tĩnh
2. Người dùng bấm "Đăng nhập" → React gửi POST /api/v1/auth/login tới Backend
3. Backend kiểm tra email + password → đúng → trả về JWT token
4. React lưu token vào localStorage (bộ nhớ trình duyệt)
5. Mọi request sau đó đều gửi kèm: Authorization: Bearer <token>
6. Backend nhận token → kiểm tra hợp lệ → xử lý yêu cầu → trả kết quả JSON
7. React hiển thị kết quả lên giao diện
```

---

## 4. Cấu trúc thư mục Backend

```
backend/
│
├── .env                              ← File cấu hình (mật khẩu DB, JWT secret, ...)
│                                       KHÔNG được đưa lên git (bảo mật)
│
├── requirements.txt                  ← Danh sách thư viện Python cần cài
│
└── app/                              ← Toàn bộ mã nguồn ứng dụng
    │
    ├── main.py                       ← ĐIỂM KHỞI ĐẦU của ứng dụng
    │                                   Khởi tạo FastAPI, cấu hình CORS, đăng ký tất cả routes
    │
    ├── seed.py                       ← Script tạo dữ liệu mẫu ban đầu
    │                                   Chạy 1 lần khi setup: tạo grades, lessons, tài khoản demo
    │
    ├── core/                         ← CẤU HÌNH HỆ THỐNG (nền tảng)
    │   ├── config.py                 ← Đọc file .env → tạo đối tượng Settings
    │   ├── database.py               ← Kết nối đến PostgreSQL
    │   ├── security.py               ← Mã hóa mật khẩu + tạo/giải mã JWT token
    │   └── deps.py                   ← Middleware xác thực: kiểm tra token, kiểm tra vai trò
    │
    ├── models/                       ← ĐỊNH NGHĨA BẢNG DATABASE
    │   ├── user.py                   ← Bảng users (thông tin người dùng)
    │   ├── grade.py                  ← Bảng grades (lớp 1-5)
    │   ├── lesson.py                 ← Bảng chapters, lessons, lesson_contents
    │   └── progress.py               ← Bảng student_progress, quiz_answers, daily_missions
    │
    ├── schemas/                      ← KIỂM TRA DỮ LIỆU VÀO/RA
    │   ├── auth.py                   ← Format dữ liệu đăng ký, đăng nhập, thông tin user
    │   ├── learn.py                  ← Format dữ liệu bài học, hoàn thành bài
    │   ├── dashboard.py              ← Format dữ liệu dashboard
    │   └── progress.py               ← Format dữ liệu tiến độ
    │
    ├── services/                     ← XỬ LÝ NGHIỆP VỤ (logic chính)
    │   ├── auth_service.py           ← Logic đăng ký, đăng nhập, tính streak
    │   ├── learn_service.py          ← Logic lấy bài học, chấm điểm, mở khóa bài tiếp
    │   ├── dashboard_service.py      ← Logic tạo nhiệm vụ hàng ngày, gợi ý bài học
    │   └── progress_service.py       ← Logic tổng hợp tiến độ theo lớp
    │
    ├── api/v1/                       ← API ENDPOINTS (đường dẫn API)
    │   ├── auth.py                   ← /auth/register, /auth/login, /auth/me
    │   ├── users.py                  ← /users (tạo, sửa, xóa tài khoản)
    │   ├── learn.py                  ← /grades, /chapters, /lessons, /lessons/complete
    │   ├── dashboard.py              ← /dashboard
    │   ├── progress.py               ← /student/progress
    │   ├── leaderboard.py            ← /leaderboard (bảng xếp hạng)
    │   ├── teacher.py                ← /teacher/* (dashboard, students, ranking)
    │   └── parent.py                 ← /parent/dashboard (xem tiến độ con)
    │
    └── features/learn/               ← SINH ĐỀ TOÁN TỰ ĐỘNG
        ├── generators/               ← Bộ sinh đề theo từng lớp
        │   ├── __init__.py           ← Đăng ký và điều phối các generator
        │   ├── grade1/               ← Cộng, trừ, so sánh, hình học cơ bản
        │   ├── grade2/               ← Nhân, chia, đo lường, thời gian
        │   ├── grade3/               ← Phân số, hình học, ước lượng
        │   ├── grade4/               ← Số thập phân, góc, diện tích
        │   └── grade5/               ← Phần trăm, tỷ lệ, hình tròn
        └── seed_data/                ← Nội dung bài học (giải thích, ví dụ, cấu hình quiz)
            ├── grade1.py → grade5.py
```

---

## 5. Chi tiết từng thành phần

### 5.1. core/ — Nền tảng hệ thống

Chứa các file cấu hình cơ bản mà ứng dụng cần để khởi động. **Không chứa logic nghiệp vụ.**

#### config.py — Quản lý cấu hình

**Nhiệm vụ**: Đọc file `.env` và cung cấp các giá trị cấu hình cho toàn bộ ứng dụng.

**Cách hoạt động**:
- Sử dụng `pydantic_settings.BaseSettings` để tự động đọc biến môi trường từ file `.env`
- Hàm `get_settings()` được cache bằng `@lru_cache` → chỉ đọc file `.env` **một lần duy nhất**, các lần gọi sau trả kết quả đã cache

**Các biến cấu hình**:

| Biến | Mục đích | Giá trị mặc định |
|------|----------|-------------------|
| `DATABASE_URL` | Chuỗi kết nối PostgreSQL |
| `JWT_SECRET` | Khóa bí mật để mã hóa/giải mã token | `your-secret-key-change-in-production` |
| `JWT_ALGORITHM` | Thuật toán mã hóa JWT | `HS256` |
| `JWT_EXPIRE_HOURS` | Thời gian token hết hạn (giờ) | `24` |
| `TEACHER_REGISTER_CODE` | Mã bí mật để giáo viên đăng ký |

#### database.py — Kết nối cơ sở dữ liệu

**Nhiệm vụ**: Thiết lập kết nối đến PostgreSQL và quản lý phiên làm việc (session).

**Các thành phần**:
- `engine`: Đối tượng kết nối đến database, quản lý pool (nhóm kết nối). Cấu hình `pool_size=10` (tối đa 10 kết nối đồng thời), `pool_pre_ping=True` (kiểm tra kết nối trước khi sử dụng)
- `SessionLocal`: "Nhà máy" tạo session. Mỗi request API nhận một session riêng
- `Base`: Lớp cơ sở cho tất cả model. Tất cả bảng database đều kế thừa từ `Base`
- `get_db()`: Hàm dependency — tạo session cho mỗi request, tự động đóng khi xong

**Ví dụ cách dùng**: Khi một API endpoint cần truy vấn database:
```python
@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    # db là session, tự động tạo khi request đến, tự động đóng khi xong
    return db.query(User).all()
```

#### security.py — Bảo mật

**Nhiệm vụ**: Xử lý mã hóa mật khẩu và quản lý JWT token.

**Các hàm**:

| Hàm | Đầu vào | Đầu ra | Mục đích |
|-----|---------|--------|----------|
| `hash_password(password)` | Mật khẩu gốc (ví dụ: "abc123") | Chuỗi hash (ví dụ: "$2b$12$...") | Mã hóa mật khẩu trước khi lưu vào DB. Không thể giải mã ngược |
| `verify_password(plain, hashed)` | Mật khẩu gốc + hash đã lưu | True/False | So sánh mật khẩu khi đăng nhập |
| `create_access_token(user_id)` | ID người dùng | JWT token (chuỗi dài) | Tạo "vé vào cửa" sau khi đăng nhập thành công |
| `decode_access_token(token)` | JWT token | user_id hoặc None | Giải mã token để biết "ai đang gọi API" |

**JWT Token chứa gì?**
```json
{
  "sub": "550e8400-e29b-41d4-a716-446655440000",  // user_id
  "exp": 1711497600                                 // thời điểm hết hạn
}
```

#### deps.py — Middleware xác thực

**Nhiệm vụ**: Kiểm tra "ai đang gọi API" và "có quyền không" trước khi xử lý request.

**Các hàm**:

- **`get_current_user()`**: Chạy trước MỌI API cần đăng nhập
  ```
  Request đến với header: Authorization: Bearer eyJhbGci...
      ↓
  Trích xuất token "eyJhbGci..."
      ↓
  Giải mã token → lấy user_id
      ↓
  Tìm user trong database theo user_id
      ↓
  Trả về đối tượng User (hoặc trả lỗi 401 nếu token sai/hết hạn)
  ```

- **`require_role(*roles)`**: Kiểm tra vai trò
  ```python
  # Chỉ giáo viên mới được gọi API này
  @router.get("/users")
  def list_users(user: User = Depends(require_role(UserRole.teacher))):
      ...
  # Nếu student gọi → trả lỗi 403 Forbidden
  ```

---

### 5.2. models/ — Định nghĩa bảng Database

Mỗi file Python định nghĩa một hoặc nhiều bảng trong PostgreSQL. SQLAlchemy tự động dịch class Python thành bảng SQL.

#### user.py — Bảng `users`

Lưu thông tin tất cả người dùng (student, teacher, parent).

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh duy nhất (tự tạo) |
| `email` | String | Email đăng nhập (duy nhất, không trùng) |
| `name` | String | Họ tên |
| `password_hash` | String | Mật khẩu đã mã hóa (KHÔNG lưu mật khẩu gốc) |
| `role` | Enum | Vai trò: `student`, `teacher`, hoặc `parent` |
| `avatar_url` | String | Link ảnh đại diện (có thể null) |
| `level` | Integer | Cấp độ hiện tại (bắt đầu từ 1, lên level mỗi 500 XP) |
| `xp` | Integer | Điểm kinh nghiệm tích lũy |
| `stars` | Integer | Tổng số sao đạt được |
| `coins` | Integer | Tổng số coin kiếm được |
| `streak` | Integer | Số ngày học liên tục |
| `parent_id` | UUID (FK) | Liên kết student với parent (trỏ đến `users.id` của parent) |
| `last_login_date` | Date | Ngày đăng nhập cuối cùng (dùng để tính streak) |
| `created_at` | DateTime | Thời điểm tạo tài khoản |
| `updated_at` | DateTime | Thời điểm cập nhật gần nhất |

**Quan hệ parent-child**: Cột `parent_id` trên bản ghi student trỏ đến `id` của parent. Một parent có thể có nhiều student (1 parent : N students).

#### grade.py — Bảng `grades`

Lưu thông tin 5 cấp lớp (Grade 1 đến Grade 5).

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `number` | Integer | Số thứ tự lớp (1-5, duy nhất) |
| `name` | String | Tên hiển thị (ví dụ: "Grade 1") |
| `description` | String | Mô tả chương trình |

**Quan hệ**: Một grade có nhiều chapters (`grades` 1:N `chapters`)

#### lesson.py — Bảng `chapters`, `lessons`, `lesson_contents`

**Bảng `chapters`** (Chương):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `grade_id` | UUID (FK) | Thuộc grade nào |
| `title` | String | Tên chương (ví dụ: "Phép cộng cơ bản") |
| `order` | Integer | Thứ tự sắp xếp trong grade |

**Bảng `lessons`** (Bài học):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `chapter_id` | UUID (FK) | Thuộc chapter nào |
| `title` | String | Tên bài (ví dụ: "Cộng hai số có 1 chữ số") |
| `order` | Integer | Thứ tự trong chapter |
| `xp_reward` | Integer | XP thưởng khi hoàn thành (mặc định 20) |
| `content_type` | Enum | Loại nội dung: `video` hoặc `slide` |
| `is_locked` | Boolean | Bài có bị khóa không |

**Bảng `lesson_contents`** (Nội dung bài học):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `lesson_id` | UUID (FK) | Thuộc lesson nào (quan hệ 1:1) |
| `explanation` | Text | Phần giải thích lý thuyết |
| `examples` | JSON | Danh sách ví dụ minh họa |
| `steps` | JSON | Các bước giải |
| `fun_fact` | String | Kiến thức thú vị |
| `practice_problems` | JSON | Bài tập luyện tập (cố định) |
| `quiz_problems` | JSON | Câu hỏi kiểm tra (cố định) |
| `problem_config` | JSON | Cấu hình để sinh đề tự động |

**Cấu trúc phân cấp**: `Grade → Chapter → Lesson → LessonContent`

#### progress.py — Bảng `student_progress`, `quiz_answers`, `daily_missions`

**Bảng `student_progress`** (Tiến độ học sinh):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `student_id` | UUID (FK) | Học sinh nào |
| `lesson_id` | UUID (FK) | Bài học nào |
| `status` | Enum | Trạng thái: `locked` (khóa), `in_progress` (đang học), `completed` (hoàn thành) |
| `score` | Integer | Điểm lần làm gần nhất (%) |
| `best_score` | Integer | Điểm cao nhất (%) |
| `stars_earned` | Integer | Số sao đạt được (0-3) |
| `attempts` | Integer | Số lần làm bài |
| `completed_at` | DateTime | Thời điểm hoàn thành |

**Bảng `quiz_answers`** (Chi tiết câu trả lời):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `student_id` | UUID (FK) | Học sinh nào |
| `lesson_id` | UUID (FK) | Bài học nào |
| `question_text` | String | Nội dung câu hỏi (ví dụ: "5 + 3 = ?") |
| `student_answer` | String | Câu trả lời của học sinh |
| `correct_answer` | String | Đáp án đúng |
| `is_correct` | Boolean | Đúng hay sai |
| `attempted_at` | DateTime | Thời điểm trả lời |

**Bảng `daily_missions`** (Nhiệm vụ hàng ngày):

| Cột | Kiểu | Mô tả |
|-----|------|-------|
| `id` | UUID | Mã định danh |
| `student_id` | UUID (FK) | Học sinh nào |
| `title` | String | Tên nhiệm vụ (ví dụ: "Hoàn thành 3 bài học") |
| `target_value` | Integer | Mục tiêu (ví dụ: 3) |
| `current_value` | Integer | Tiến độ hiện tại (ví dụ: 1) |
| `mission_type` | Enum | Loại: `lessons`, `stars`, `games` |
| `date` | Date | Ngày của nhiệm vụ |
| `is_completed` | Boolean | Đã hoàn thành chưa |

---

### 5.3. schemas/ — Kiểm tra dữ liệu vào/ra

**Tại sao cần schemas tách riêng khỏi models?**

Models định nghĩa bảng database (có cả `password_hash`). Schemas quyết định:
- **Request**: Client gửi gì lên? → Validate (kiểm tra format, độ dài mật khẩu...)
- **Response**: Server trả gì về? → Giấu thông tin nhạy cảm (không trả `password_hash`)

**Ví dụ cụ thể**:
```
Client gửi: {"email": "a@b.com", "password": "123456"}
    ↓
Schema UserCreate validate: password >= 6 ký tự ✓
    ↓
Service hash password → lưu vào DB: password_hash = "$2b$12$..."
    ↓
Schema UserResponse trả về: {"id": "...", "email": "a@b.com", "name": "..."}
    (KHÔNG trả password_hash)
```

#### auth.py — Schemas xác thực

| Schema | Dùng khi | Các trường |
|--------|----------|------------|
| `UserCreate` | Tạo tài khoản mới | email, name, password (min 6 ký tự), role, student_ids, parent_id |
| `UserLogin` | Đăng nhập | email, password |
| `UserResponse` | Trả thông tin user | id, email, name, role, level, xp, stars, coins, streak, parent_id (KHÔNG có password) |
| `TokenResponse` | Trả kết quả đăng nhập | access_token, token_type, user |

#### learn.py — Schemas bài học

| Schema | Mô tả |
|--------|-------|
| `GradeResponse` | Thông tin lớp + số bài đã hoàn thành |
| `ChapterDetailResponse` | Thông tin chương + danh sách bài học |
| `LessonResponse` | Thông tin bài học + trạng thái (locked/in_progress/completed) |
| `LessonContentResponse` | Nội dung bài: giải thích, ví dụ, bài tập, quiz |
| `LessonCompleteRequest` | Dữ liệu gửi khi hoàn thành: quiz_score, total_questions, answers[] |
| `LessonCompleteResponse` | Kết quả: stars_earned, xp_earned, coins_earned, level_up, next_lesson_id |

---

### 5.4. services/ — Xử lý nghiệp vụ

Nơi chứa toàn bộ "logic thông minh" của ứng dụng. Tách riêng khỏi API routes để dễ bảo trì và test.

#### auth_service.py — Logic xác thực

**`register_user(db, email, name, password, role)`**:
1. Mã hóa mật khẩu bằng bcrypt
2. Tạo bản ghi User mới trong database
3. Set `last_login_date = hôm nay`

**`authenticate_user(db, email, password)`**:
1. Tìm user theo email → không tìm thấy → báo lỗi "No account found"
2. So sánh mật khẩu → sai → báo lỗi "Incorrect password"
3. Tính streak (chuỗi ngày học liên tục):
   - Đăng nhập hôm qua → streak + 1
   - Bỏ học 1 ngày trở lên → streak reset về 1
   - Đăng nhập cùng ngày → giữ nguyên streak
4. Cập nhật `last_login_date = hôm nay`

#### learn_service.py — Logic học tập (FILE QUAN TRỌNG NHẤT)

**`list_grades(db, student_id)`**: Trả danh sách 5 lớp kèm số bài đã hoàn thành.

**`get_grade_chapters(db, grade_id, student_id)`**: Trả danh sách chương kèm trạng thái mở khóa bài học.

**Logic mở khóa bài học**:
```
Bài 1 của Chương 1: luôn mở (in_progress)
Bài 2: mở khi Bài 1 hoàn thành
Bài 3: mở khi Bài 2 hoàn thành
...
Bài 1 của Chương 2: mở khi bài cuối Chương 1 hoàn thành
```

**`get_lesson_content(db, lesson_id)`**: Trả nội dung bài học.
- Nếu có `problem_config` → gọi generator để sinh đề toán mới mỗi lần
- Nếu không → dùng bài tập cố định từ `practice_problems` / `quiz_problems`

**`complete_lesson(db, lesson_id, quiz_score, total_questions, user, answers)`** — Hàm chấm điểm:

```
Đầu vào: quiz_score = 4, total_questions = 5

Bước 1: Tính tỷ lệ đúng
    ratio = 4 / 5 = 0.8 (80%)

Bước 2: Tính số sao
    100% → 3 sao
    ≥ 80% → 2 sao     ← 80% rơi vào đây
    ≥ 60% → 1 sao
    < 60% → 0 sao

Bước 3: Tính phần thưởng
    XP = sao × xp_reward = 2 × 20 = 40 XP
    Coins = sao × 10 = 2 × 10 = 20 coins
    Score = 80%

Bước 4: Cập nhật student_progress
    - Tăng attempts (số lần làm)
    - Nếu điểm cao hơn best_score → cập nhật
    - Nếu sao > 0 → status = completed

Bước 5: Lưu chi tiết từng câu trả lời (quiz_answers)
    - Câu 1: "5 + 3 = ?", trả lời "8", đáp án "8", đúng ✓
    - Câu 2: "7 × 4 = ?", trả lời "21", đáp án "28", sai ✗
    - ...

Bước 6: Cập nhật user
    - user.xp += 40
    - user.stars += 2
    - user.coins += 20
    - Kiểm tra level up: level = xp ÷ 500 + 1

Bước 7: Mở khóa bài tiếp theo
    - Tìm bài kế tiếp trong chapter (hoặc bài đầu chapter kế)
    - Tạo student_progress với status = in_progress

Đầu ra: {stars_earned: 2, xp_earned: 40, coins_earned: 20, level_up: false}
```

#### dashboard_service.py — Logic dashboard

**`get_dashboard(db, user)`**:
1. Tạo/lấy nhiệm vụ hàng ngày (3 nhiệm vụ mỗi ngày)
2. Gợi ý bài học tiếp theo (5 bài chưa hoàn thành, theo thứ tự)
3. Tổng hợp thống kê (số bài đã hoàn thành, tổng sao)

**Tự động tạo nhiệm vụ hàng ngày**:
- Hoàn thành 3 bài học
- Đạt 5 sao
- Chơi 2 game

#### progress_service.py — Logic tiến độ

**`get_student_progress(db, user)`**: Tổng hợp tiến độ theo từng lớp:
- Tổng số bài trong lớp
- Số bài đã hoàn thành
- Số sao đã đạt
- Tính tổng toàn bộ các lớp

---

### 5.5. api/v1/ — API Endpoints

Lớp mỏng nhận HTTP request, gọi service xử lý, trả response. Mỗi file quản lý một nhóm chức năng.

#### auth.py — Xác thực

- `POST /auth/register`: Đăng ký giáo viên (cần mã `TEACHER_REGISTER_CODE`)
- `POST /auth/login`: Đăng nhập → trả JWT token + thông tin user
- `GET /auth/me`: Lấy thông tin user đang đăng nhập

#### users.py — Quản lý tài khoản (chỉ Teacher)

- `GET /users`: Danh sách users (lọc theo role)
- `POST /users/create`: Tạo tài khoản student hoặc parent. Khi tạo parent có thể chọn students để liên kết
- `PUT /users/{id}`: Sửa thông tin (tên, email, mật khẩu), thêm students vào parent
- `DELETE /users/{id}`: Xóa user + tất cả dữ liệu liên quan (progress, quiz_answers, daily_missions)

#### learn.py — Nội dung học tập

- `GET /grades`: Danh sách lớp 1-5 kèm tiến độ
- `GET /grades/{id}/chapters`: Các chương trong lớp kèm trạng thái mở khóa
- `GET /chapters/{id}/lessons`: Các bài trong chương
- `GET /lessons/{id}`: Chi tiết bài học
- `GET /lessons/{id}/content`: Nội dung bài (lý thuyết + bài tập tự động sinh)
- `POST /lessons/{id}/complete`: Nộp bài quiz → tính điểm, thưởng, mở khóa bài tiếp

#### leaderboard.py — Bảng xếp hạng (chỉ Student)

- `GET /leaderboard?period=week&grade_id=xxx`: Xếp hạng top 10, lọc theo tuần/tháng/lớp
- `GET /leaderboard/filters`: Danh sách lớp để lọc

**Công thức xếp hạng**:
```
ranking_score = XP + (Sao × 15) + (Số bài hoàn thành × 20) + (Streak × 5)
```

#### teacher.py — Chức năng giáo viên

- `GET /teacher/dashboard`: Thống kê thực (tổng students, parents, active hôm nay, điểm TB)
- `GET /teacher/students`: Tất cả students kèm số bài, điểm TB, số câu đúng/sai
- `GET /teacher/students/{id}/progress`: Chi tiết từng bài kèm từng câu trả lời đúng/sai
- `GET /teacher/ranking`: Bảng xếp hạng toàn bộ students

#### parent.py — Chức năng phụ huynh

- `GET /parent/dashboard`: Tiến độ con mình (chỉ xem được con đã liên kết, KHÔNG xem được học sinh khác)

---

### 5.6. features/learn/generators/ — Sinh đề toán tự động

**Kiến trúc Registry Pattern**:

Mỗi hàm sinh đề được đăng ký với decorator `@register("problem_type")`:

```python
# Trong grade1/addition.py
@register("addition_basic")
def generate_addition(params, answer_type):
    a = random.randint(params["min"], params["max"])
    b = random.randint(params["min"], params["max"])
    return {
        "question_text": f"{a} + {b} = ?",
        "answer": a + b,
        "options": [...],   # nếu answer_type = multiple_choice
    }
```

**Cách hoạt động**:
```
Bài học có problem_config: {"type": "addition_basic", "params": {"min": 1, "max": 20}, "count": 5}
    ↓
learn_service gọi generate_problems(config, mode="quiz")
    ↓
generators/__init__.py tra cứu registry: "addition_basic" → hàm generate_addition
    ↓
Gọi hàm 5 lần, loại bỏ trùng lặp
    ↓
Trả về 5 bài toán (mỗi lần gọi API cho đề khác nhau)
```

**Các loại đề theo lớp**:

| Lớp | Các chủ đề |
|-----|-----------|
| Lớp 1 | Cộng, trừ trong phạm vi 20, đếm, so sánh, nhận biết hình |
| Lớp 2 | Nhân, chia, đo lường (cm, kg), đọc giờ đồng hồ |
| Lớp 3 | Phân số, phép tính nhiều chữ số, ước lượng |
| Lớp 4 | Số thập phân, góc, diện tích, chu vi |
| Lớp 5 | Phần trăm, tỷ lệ, diện tích/chu vi hình tròn |

---

## 6. Cơ sở dữ liệu

### Sơ đồ quan hệ (ERD)

```
┌──────────────────┐
│      users       │
├──────────────────┤            ┌──────────────────┐
│ id (PK)          │            │     grades       │
│ email            │            ├──────────────────┤
│ name             │            │ id (PK)          │
│ password_hash    │            │ number (1-5)     │
│ role             │            │ name             │
│ level, xp        │            └────────┬─────────┘
│ stars, coins     │                     │ 1 : N
│ streak           │            ┌────────▼─────────┐
│ parent_id (FK)───┼──┐         │    chapters      │
│ last_login_date  │  │         ├──────────────────┤
└──┬───┬───┬───────┘  │         │ id (PK)          │
   │   │   │     self-ref       │ grade_id (FK)    │
   │   │   │          └──→     │ title, order     │
   │   │   │                    └────────┬─────────┘
   │   │   │                             │ 1 : N
   │   │   │                    ┌────────▼─────────┐
   │   │   │                    │    lessons       │
   │   │   │                    ├──────────────────┤
   │   │   │                    │ id (PK)          │
   │   │   │                    │ chapter_id (FK)  │
   │   │   │                    │ title, order     │
   │   │   │                    │ xp_reward        │
   │   │   │                    └──┬─────┬─────────┘
   │   │   │                  1:N  │     │ 1:1
   │   │   │                       │  ┌──▼──────────────┐
   │   │   │                       │  │ lesson_contents  │
   │   │   │                       │  │ explanation      │
   │   │   │                       │  │ examples (JSON)  │
   │   │   │                       │  │ problem_config   │
   │   │   │                       │  └─────────────────┘
   │   │   │                       │
   │   │   │        ┌──────────────▼───────┐
   │   │   │        │  student_progress    │
   │   │   └───────→│  student_id (FK)     │
   │   │            │  lesson_id (FK)      │
   │   │            │  status, score       │
   │   │            │  stars_earned        │
   │   │            │  attempts, best_score│
   │   │            │  completed_at        │
   │   │            └──────────────────────┘
   │   │
   │   │            ┌──────────────────────┐
   │   │            │   quiz_answers       │
   │   └──────────→ │  student_id (FK)     │
   │                │  lesson_id (FK)      │
   │                │  question_text       │
   │                │  student_answer      │
   │                │  correct_answer      │
   │                │  is_correct          │
   │                │  attempted_at        │
   │                └──────────────────────┘
   │
   │                ┌──────────────────────┐
   │                │   daily_missions     │
   └──────────────→ │  student_id (FK)     │
                    │  title, mission_type │
                    │  target/current_value│
                    │  date, is_completed  │
                    └──────────────────────┘
```

### Tóm tắt quan hệ

| Quan hệ | Mô tả |
|---------|-------|
| User (parent) 1 : N User (student) | Một phụ huynh có thể có nhiều con (qua `parent_id`) |
| Grade 1 : N Chapter | Mỗi lớp có nhiều chương |
| Chapter 1 : N Lesson | Mỗi chương có nhiều bài |
| Lesson 1 : 1 LessonContent | Mỗi bài có đúng 1 nội dung |
| User 1 : N StudentProgress | Mỗi student có tiến độ ở nhiều bài |
| User 1 : N QuizAnswer | Mỗi student có nhiều câu trả lời |
| User 1 : N DailyMission | Mỗi student có nhiều nhiệm vụ hàng ngày |

---

## 7. Luồng hoạt động chính

### 7.1. Đăng ký và đăng nhập

```
Giáo viên đăng ký trên web (cần mã MATHQUEST2026)
    ↓
Giáo viên tạo tài khoản cho học sinh (tên, email, mật khẩu)
    ↓
Giáo viên tạo tài khoản phụ huynh + chọn học sinh liên kết
    ↓
Học sinh / Phụ huynh đăng nhập bằng thông tin giáo viên cung cấp
    ↓
Server trả JWT token → lưu vào trình duyệt
    ↓
Mọi thao tác sau đều gửi kèm token để xác thực
```

### 7.2. Học sinh học bài

```
Mở trang Learn → Chọn Lớp (Grade 1-5)
    ↓
Xem danh sách Chương → Chọn Chương
    ↓
Xem danh sách Bài (có khóa/mở) → Chọn Bài đã mở
    ↓
Tab 1 - Learn: Đọc giải thích + xem ví dụ
    ↓
Tab 2 - Practice: Làm 5 bài tập tự do (không tính điểm)
    ↓
Tab 3 - Quiz: Làm 5 câu trắc nghiệm (có tính điểm)
    ↓
Hoàn thành Quiz:
    ├── Tính điểm: 4/5 đúng = 80% → 2 sao
    ├── Thưởng: +40 XP, +20 coins
    ├── Kiểm tra level up (mỗi 500 XP)
    ├── Lưu chi tiết từng câu đúng/sai
    └── Mở khóa bài tiếp theo
```

### 7.3. Hệ thống tính điểm

| Tỷ lệ đúng | Số sao | XP | Coins |
|-------------|--------|-----|-------|
| 100% (5/5) | 3 ⭐ | 3 × 20 = 60 | 30 |
| ≥ 80% (4/5) | 2 ⭐ | 2 × 20 = 40 | 20 |
| ≥ 60% (3/5) | 1 ⭐ | 1 × 20 = 20 | 10 |
| < 60% (0-2/5) | 0 | 0 | 0 |

### 7.4. Hệ thống Streak (chuỗi ngày học)

Tính mỗi lần đăng nhập:

| Tình huống | Kết quả |
|-----------|---------|
| Hôm qua đã đăng nhập | streak + 1 |
| Bỏ 1 ngày trở lên | streak = 1 (reset) |
| Đăng nhập lại cùng ngày | Không thay đổi |

### 7.5. Giáo viên theo dõi học sinh

```
Mở Teacher Dashboard → xem thống kê tổng quan
    ├── Tổng số học sinh, phụ huynh
    ├── Số học sinh online hôm nay
    ├── Điểm trung bình
    └── Tổng bài đã hoàn thành
    ↓
Mở Monitor Students → xem danh sách từng học sinh
    ├── Điểm trung bình, số sao, streak
    ├── Số câu đúng / sai
    └── Bấm "View Details" → xem chi tiết
        ↓
Chi tiết học sinh:
    ├── Thống kê tổng: sao, coins, streak, số bài, điểm TB
    ├── Danh sách từng bài đã làm
    └── Mở rộng bài → xem TỪNG CÂU HỎI:
        ├── ✓ "5 + 3 = ?" → Trả lời: 8, Đáp án: 8 (ĐÚNG)
        └── ✗ "7 × 4 = ?" → Trả lời: 21, Đáp án: 28 (SAI)
```

### 7.6. Phụ huynh xem tiến độ con

```
Đăng nhập bằng tài khoản parent
    ↓
Tự động hiển thị thông tin con đã liên kết
    ├── Thống kê: sao, coins, streak, số bài, điểm TB
    ├── Danh sách bài đã hoàn thành
    └── Chi tiết từng câu đúng/sai (giống giáo viên)

Lưu ý: Phụ huynh KHÔNG thể xem dữ liệu học sinh khác
```

---

## 8. Danh sách API

### Xác thực (Auth)

| Phương thức | Endpoint | Cần đăng nhập | Mô tả |
|-------------|----------|---------------|-------|
| POST | `/api/v1/auth/register` | Không | Đăng ký giáo viên (cần mã bí mật) |
| POST | `/api/v1/auth/login` | Không | Đăng nhập → trả JWT token + thông tin user |
| GET | `/api/v1/auth/me` | Có | Lấy thông tin người dùng đang đăng nhập |

### Quản lý tài khoản (Users) — Chỉ Teacher

| Phương thức | Endpoint | Mô tả |
|-------------|----------|-------|
| GET | `/api/v1/users?role=student` | Danh sách users (lọc theo role) |
| POST | `/api/v1/users/create` | Tạo tài khoản student hoặc parent |
| PUT | `/api/v1/users/{id}` | Sửa thông tin, liên kết student-parent |
| DELETE | `/api/v1/users/{id}` | Xóa user + dữ liệu liên quan |

### Nội dung học tập (Learn)

| Phương thức | Endpoint | Mô tả |
|-------------|----------|-------|
| GET | `/api/v1/grades` | Danh sách lớp 1-5 kèm tiến độ |
| GET | `/api/v1/grades/{id}/chapters` | Các chương trong lớp kèm trạng thái mở khóa |
| GET | `/api/v1/chapters/{id}/lessons` | Các bài trong chương |
| GET | `/api/v1/lessons/{id}` | Chi tiết bài học |
| GET | `/api/v1/lessons/{id}/content` | Nội dung bài (lý thuyết + đề bài tự động sinh) |
| POST | `/api/v1/lessons/{id}/complete` | Nộp bài quiz → tính điểm, cấp thưởng |

### Dashboard & Tiến độ

| Phương thức | Endpoint | Mô tả |
|-------------|----------|-------|
| GET | `/api/v1/dashboard` | Dashboard học sinh (nhiệm vụ, gợi ý, thống kê) |
| GET | `/api/v1/student/progress` | Tổng hợp tiến độ theo từng lớp |

### Bảng xếp hạng (Leaderboard) — Chỉ Student

| Phương thức | Endpoint | Mô tả |
|-------------|----------|-------|
| GET | `/api/v1/leaderboard?period=week&grade_id=x` | Xếp hạng top 10 (lọc tuần/tháng/lớp) |
| GET | `/api/v1/leaderboard/filters` | Danh sách lớp để chọn filter |

### Giáo viên (Teacher)

| Phương thức | Endpoint | Mô tả |
|-------------|----------|-------|
| GET | `/api/v1/teacher/dashboard` | Thống kê tổng quan (số students, điểm TB, active) |
| GET | `/api/v1/teacher/students` | Tất cả students kèm tiến độ |
| GET | `/api/v1/teacher/students/{id}/progress` | Chi tiết từng bài + từng câu đúng/sai |
| GET | `/api/v1/teacher/ranking` | Bảng xếp hạng toàn bộ students |

### Phụ huynh (Parent)

| Phương thức | Endpoint | Mô tả |
|-------------|----------|-------|
| GET | `/api/v1/parent/dashboard` | Tiến độ con mình (chỉ xem được con đã liên kết) |



- Python 3.10
- Node.js 18+
- PostgreSQL 14+

python -m app.seed                   # Tạo dữ liệu (an toàn, không ghi đè)
python -m app.seed --update          # Cập nhật nội dung bài học
python -m app.seed --reset           # XÓA TOÀN BỘ và tạo lại (NGUY HIỂM)
```
