import { Routes, Route, Navigate } from 'react-router-dom'
import { AnimatePresence } from 'framer-motion'

// Shared
import ProtectedRoute from './components/ProtectedRoute'
import StudentLayout from './components/Layout/StudentLayout'
import TeacherLayout from './components/Layout/TeacherLayout'
import Landing from './pages/Landing'

// Features
import { useAuth, Login, Register } from './features/auth'
import { StudentDashboard } from './features/dashboard'
import { GradeSelection, LessonList, LessonContent } from './features/learn'
import { TeacherDashboard, ManageAccounts, MonitorStudents, StudentDetail, TeacherRanking } from './features/teacher'
import { GameSelection, MathPopGame, MathMemoryGame } from './features/play'
import { Leaderboard } from './features/rank'
import { ParentDashboard } from './features/parent'
import ParentLayout from './components/Layout/ParentLayout'

function App() {
  const { user } = useAuth()

  return (
    <AnimatePresence mode="wait">
      <Routes>
        {/* Public */}
        <Route path="/" element={user ? <Navigate to={`/${user.role || 'student'}`} replace /> : <Landing />} />
        <Route path="/login" element={user ? <Navigate to={`/${user.role || 'student'}`} replace /> : <Login />} />
        <Route path="/register" element={user ? <Navigate to={`/${user.role || 'student'}`} replace /> : <Register />} />

        {/* Student */}
        <Route path="/student" element={<ProtectedRoute role="student"><StudentLayout /></ProtectedRoute>}>
          <Route index element={<StudentDashboard />} />
          <Route path="grades" element={<GradeSelection />} />
          <Route path="grades/:gradeId" element={<LessonList />} />
          <Route path="lessons/:lessonId" element={<LessonContent />} />
          <Route path="play" element={<GameSelection />} />
          <Route path="play/math-pop" element={<MathPopGame />} />
          <Route path="play/math-memory" element={<MathMemoryGame />} />
          <Route path="rank" element={<Leaderboard />} />
        </Route>

        {/* Teacher */}
        <Route path="/teacher" element={<ProtectedRoute role="teacher"><TeacherLayout /></ProtectedRoute>}>
          <Route index element={<TeacherDashboard />} />
          <Route path="accounts" element={<ManageAccounts />} />
          <Route path="students" element={<MonitorStudents />} />
          <Route path="students/:studentId" element={<StudentDetail />} />
          <Route path="ranking" element={<TeacherRanking />} />
        </Route>

        {/* Parent */}
        <Route path="/parent" element={<ProtectedRoute role="parent"><ParentLayout /></ProtectedRoute>}>
          <Route index element={<ParentDashboard />} />
        </Route>

        {/* 404 */}
        <Route path="*" element={
          <div className="min-h-screen flex items-center justify-center bg-gray-50">
            <div className="text-center">
              <div className="text-8xl mb-4">🦉</div>
              <h1 className="text-4xl font-bold text-gray-800 mb-2">404 - Page Not Found</h1>
              <p className="text-gray-500 mb-6">Oops! This page flew away!</p>
              <a href="/" className="btn btn-primary">Go Home</a>
            </div>
          </div>
        } />
      </Routes>
    </AnimatePresence>
  )
}

export default App
