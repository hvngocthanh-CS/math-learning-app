import { useState, useEffect } from 'react'
import toast from 'react-hot-toast'
import api from '../../../utils/api'

export default function useLessonContent(lessonId) {
  const [lesson, setLesson] = useState(null)
  const [content, setContent] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (!lessonId) {
      setLoading(false)
      return
    }

    const fetchData = async () => {
      setLoading(true)
      setError(null)

      try {
        const [lessonRes, contentRes] = await Promise.all([
          api.get(`/lessons/${lessonId}`),
          api.get(`/lessons/${lessonId}/content`),
        ])

        setLesson(lessonRes.data)

        // Transform flat API response into the shape components expect
        const raw = contentRes.data
        setContent({
          learn: {
            explanation: raw.explanation,
            examples: raw.examples,
            steps: raw.steps,
            fun_fact: raw.fun_fact,
          },
          practice: raw.practice_problems,
          quiz: raw.quiz_problems,
        })
      } catch (err) {
        console.error('Failed to fetch lesson content:', err)
        const status = err.response?.status
        if (status === 404) {
          setError('not_found')
        } else {
          setError('fetch_failed')
          toast.error('Failed to load lesson. Please try again!')
        }
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [lessonId])

  return { lesson, content, loading, error }
}
