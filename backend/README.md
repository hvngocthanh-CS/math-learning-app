# MathQuest Backend (Python/FastAPI)

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Create the PostgreSQL database:
```bash
createdb mathquest
```

5. Run the seed script:
```bash
python -m app.seed
```

6. Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Demo Accounts

- **Teacher**: teacher@mathquest.com / password123
- **Student**: student@mathquest.com / password123

## API Endpoints

### Auth
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get current user

### Users (Teacher only)
- `GET /api/v1/users/` - List users
- `POST /api/v1/users/create` - Create student/parent account
- `GET /api/v1/users/{id}` - Get user details

### Grades & Lessons
- `GET /api/v1/grades` - List grades with progress
- `GET /api/v1/grades/{id}/chapters` - Get chapters for a grade
- `GET /api/v1/chapters/{id}/lessons` - Get lessons for a chapter
- `GET /api/v1/lessons/{id}` - Get lesson detail

### Dashboard
- `GET /api/v1/dashboard` - Student dashboard data
