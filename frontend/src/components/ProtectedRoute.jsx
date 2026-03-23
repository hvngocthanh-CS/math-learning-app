import { Navigate } from 'react-router-dom'
import { useAuth } from '../features/auth'

const roleRedirects = {
  student: '/student',
  parent: '/parent',
  teacher: '/teacher',
}

export default function ProtectedRoute({ children, role }) {
  const { user, loading } = useAuth()

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="text-center">
          <div className="text-6xl animate-bounce-slow mb-4">🦉</div>
          <div className="text-xl font-bold text-gray-600">Loading MathQuest...</div>
          <div className="mt-3 flex justify-center gap-1">
            <div className="w-3 h-3 bg-primary-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
            <div className="w-3 h-3 bg-secondary-500 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
            <div className="w-3 h-3 bg-accent-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
          </div>
        </div>
      </div>
    )
  }

  // Not authenticated
  if (!user) {
    return <Navigate to="/login" replace />
  }

  // Wrong role
  if (role && user.role !== role) {
    const redirectTo = roleRedirects[user.role] || '/'
    return <Navigate to={redirectTo} replace />
  }

  return children
}
