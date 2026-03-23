import axios from 'axios'

const API_URL = '/api/v1'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor - attach JWT token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// Response interceptor - handle 401
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      const isAuthRoute = window.location.pathname === '/login' || window.location.pathname === '/register'
      if (!isAuthRoute) {
        // Only redirect for expired tokens, not login failures
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        window.location.href = '/login'
      }
    }
    return Promise.reject(error)
  }
)

// Auth API
export const loginAPI = async (email, password) => {
  const response = await api.post('/auth/login', { email, password })
  return response.data
}

export const registerAPI = async (name, email, password, role, teacherCode) => {
  const response = await api.post('/auth/register', { name, email, password, role, teacher_code: teacherCode })
  return response.data
}

export const getMeAPI = async () => {
  const response = await api.get('/auth/me')
  return response.data
}

// Users API
export const getUsers = async () => {
  const response = await api.get('/users')
  return response.data
}

export const getUser = async (id) => {
  const response = await api.get(`/users/${id}`)
  return response.data
}

// Grades API
export const getGrades = async () => {
  const response = await api.get('/grades')
  return response.data
}

export const getGrade = async (id) => {
  const response = await api.get(`/grades/${id}`)
  return response.data
}

// Lessons API
export const getLessons = async (gradeId) => {
  const response = await api.get(`/grades/${gradeId}/lessons`)
  return response.data
}

export const getLesson = async (id) => {
  const response = await api.get(`/lessons/${id}`)
  return response.data
}

// Student progress API
export const getStudentProgress = async () => {
  const response = await api.get('/student/progress')
  return response.data
}

export const getStudentMissions = async () => {
  const response = await api.get('/student/missions')
  return response.data
}

// Lesson content API
export const getLessonContent = async (id) => {
  const response = await api.get(`/lessons/${id}/content`)
  return response.data
}

export const completeLesson = async (id, data) => {
  const response = await api.post(`/lessons/${id}/complete`, data)
  return response.data
}

export const getProgressSummary = async () => {
  const response = await api.get('/student/progress')
  return response.data
}

// Health check
export const healthCheck = async () => {
  const response = await api.get('/health')
  return response.data
}

export default api
