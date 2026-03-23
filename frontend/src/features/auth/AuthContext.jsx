import { createContext, useContext, useState, useEffect } from 'react'
import { loginAPI, registerAPI, getMeAPI } from '../../utils/api'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  // Check token on mount
  useEffect(() => {
    const checkAuth = async () => {
      const token = localStorage.getItem('token')
      if (!token) {
        setLoading(false)
        return
      }

      try {
        const data = await getMeAPI()
        setUser(data.user || data)
      } catch {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
      } finally {
        setLoading(false)
      }
    }

    // Try to load cached user first for instant UI
    const cachedUser = localStorage.getItem('user')
    if (cachedUser) {
      try {
        setUser(JSON.parse(cachedUser))
      } catch {
        // ignore parse errors
      }
    }

    checkAuth()
  }, [])

  const login = async (email, password) => {
    const data = await loginAPI(email, password)
    const token = data.token || data.access_token
    const userData = data.user || data

    if (token) {
      localStorage.setItem('token', token)
    }
    localStorage.setItem('user', JSON.stringify(userData))
    setUser(userData)
    return userData
  }

  const register = async (name, email, password, role, teacherCode) => {
    const data = await registerAPI(name, email, password, role, teacherCode)
    // Don't auto-login — user must log in after registration
    return data
  }

  const logout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

export default AuthContext
