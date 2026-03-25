import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  FaArrowLeft, FaSpinner, FaStar, FaFire, FaCoins,
  FaCheckCircle, FaTimesCircle, FaBook, FaChevronDown, FaChevronUp,
} from 'react-icons/fa'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.06 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

function LessonCard({ lesson }) {
  const [expanded, setExpanded] = useState(false)
  const statusColor = lesson.status === 'completed' ? 'bg-green-100 text-green-700' : 'bg-yellow-100 text-yellow-700'
  const starIcons = Array.from({ length: 3 }, (_, i) => (
    <FaStar key={i} className={i < lesson.stars_earned ? 'text-yellow-400' : 'text-gray-200'} />
  ))

  return (
    <motion.div variants={item} className="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden">
      <div
        className="p-4 cursor-pointer hover:bg-gray-50 transition-colors"
        onClick={() => setExpanded(!expanded)}
      >
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-purple-50 rounded-xl flex items-center justify-center flex-shrink-0">
            <FaBook className="text-purple-500" />
          </div>
          <div className="flex-1 min-w-0">
            <h4 className="font-bold text-gray-800 text-sm truncate">{lesson.lesson_title}</h4>
            <p className="text-xs text-gray-400">{lesson.grade_name} &bull; {lesson.chapter_title}</p>
          </div>
          <div className="flex items-center gap-2">
            <span className={`text-xs font-bold px-2 py-0.5 rounded-full ${statusColor}`}>
              {lesson.status === 'completed' ? 'Completed' : 'In Progress'}
            </span>
            <div className="flex gap-0.5">{starIcons}</div>
            <span className="text-sm font-extrabold text-gray-600">{lesson.best_score}%</span>
            {expanded ? <FaChevronUp className="text-gray-300" /> : <FaChevronDown className="text-gray-300" />}
          </div>
        </div>

        {/* Quick stats */}
        <div className="flex items-center gap-4 mt-2 ml-13 text-xs text-gray-400">
          <span>Attempts: <strong className="text-gray-600">{lesson.attempts}</strong></span>
          <span>Score: <strong className="text-gray-600">{lesson.score}%</strong></span>
          {lesson.completed_at && (
            <span>
              Completed: <strong className="text-gray-600">
                {new Date(lesson.completed_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
              </strong>
            </span>
          )}
        </div>
      </div>

      {/* Expanded: Quiz answers */}
      {expanded && lesson.quiz_answers && lesson.quiz_answers.length > 0 && (
        <motion.div
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          className="border-t border-gray-100 bg-gray-50 p-4"
        >
          <h5 className="text-xs font-bold text-gray-500 uppercase mb-3">Quiz Answers (Latest Attempt)</h5>
          <div className="space-y-2">
            {lesson.quiz_answers.map((answer, i) => (
              <div
                key={i}
                className={`flex items-start gap-3 p-3 rounded-lg ${
                  answer.is_correct ? 'bg-green-50 border border-green-100' : 'bg-red-50 border border-red-100'
                }`}
              >
                <div className="mt-0.5">
                  {answer.is_correct ? (
                    <FaCheckCircle className="text-green-500" />
                  ) : (
                    <FaTimesCircle className="text-red-400" />
                  )}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-semibold text-gray-700">{answer.question_text}</p>
                  <div className="flex flex-wrap gap-3 mt-1 text-xs">
                    <span>
                      Student answer: <strong className={answer.is_correct ? 'text-green-600' : 'text-red-500'}>
                        {answer.student_answer}
                      </strong>
                    </span>
                    {!answer.is_correct && (
                      <span>
                        Correct answer: <strong className="text-green-600">{answer.correct_answer}</strong>
                      </span>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </motion.div>
      )}

      {expanded && (!lesson.quiz_answers || lesson.quiz_answers.length === 0) && (
        <div className="border-t border-gray-100 bg-gray-50 p-4 text-center text-sm text-gray-400">
          No detailed quiz data available for this lesson.
        </div>
      )}
    </motion.div>
  )
}

export default function StudentDetail() {
  const { studentId } = useParams()
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    api.get(`/teacher/students/${studentId}/progress`)
      .then((res) => setData(res.data))
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load student'))
      .finally(() => setLoading(false))
  }, [studentId])

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <FaSpinner className="animate-spin text-4xl text-orange-400" />
      </div>
    )
  }

  if (error) {
    return (
      <div className="text-center py-20">
        <div className="text-5xl mb-4">😕</div>
        <p className="text-gray-500 font-semibold">{error}</p>
        <Link to="/teacher/students" className="text-orange-500 font-bold text-sm mt-4 inline-block">
          &larr; Back to students
        </Link>
      </div>
    )
  }

  const { student, progress } = data
  const completedLessons = progress.filter((p) => p.status === 'completed')
  const inProgressLessons = progress.filter((p) => p.status === 'in_progress')

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-4xl mx-auto space-y-6"
    >
      {/* Back button */}
      <motion.div variants={item}>
        <Link to="/teacher/students" className="inline-flex items-center gap-2 text-gray-400 hover:text-orange-500 font-bold text-sm transition-colors">
          <FaArrowLeft /> Back to students
        </Link>
      </motion.div>

      {/* Student Profile Card */}
      <motion.div variants={item} className="bg-white rounded-2xl shadow-md border border-gray-100 p-6">
        <div className="flex items-center gap-5">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-orange-400 to-amber-500 flex items-center justify-center text-white font-extrabold text-3xl shadow-lg">
            {student.name[0].toUpperCase()}
          </div>
          <div className="flex-1">
            <h1 className="text-2xl font-extrabold text-gray-800">{student.name}</h1>
            <p className="text-sm text-gray-400">{student.email}</p>
            {student.parent_name && (
              <p className="text-xs text-gray-400 mt-1">Parent: <strong>{student.parent_name}</strong></p>
            )}
          </div>
          <div className="text-right">
            <div className="text-sm font-bold text-gray-400">Level</div>
            <div className="text-3xl font-extrabold text-orange-500">{student.level}</div>
          </div>
        </div>

        {/* Stats grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-6 gap-3 mt-6">
          <div className="bg-yellow-50 rounded-xl p-3 text-center">
            <FaStar className="text-yellow-500 mx-auto mb-1" />
            <div className="text-lg font-extrabold text-gray-700">{student.stars}</div>
            <div className="text-[10px] font-semibold text-gray-400">Stars</div>
          </div>
          <div className="bg-amber-50 rounded-xl p-3 text-center">
            <FaCoins className="text-amber-500 mx-auto mb-1" />
            <div className="text-lg font-extrabold text-gray-700">{student.coins}</div>
            <div className="text-[10px] font-semibold text-gray-400">Coins</div>
          </div>
          <div className="bg-orange-50 rounded-xl p-3 text-center">
            <FaFire className="text-orange-500 mx-auto mb-1" />
            <div className="text-lg font-extrabold text-gray-700">{student.streak}</div>
            <div className="text-[10px] font-semibold text-gray-400">Streak</div>
          </div>
          <div className="bg-blue-50 rounded-xl p-3 text-center">
            <FaBook className="text-blue-500 mx-auto mb-1" />
            <div className="text-lg font-extrabold text-gray-700">{student.lessons_completed}</div>
            <div className="text-[10px] font-semibold text-gray-400">Lessons</div>
          </div>
          <div className="bg-green-50 rounded-xl p-3 text-center">
            <FaCheckCircle className="text-green-500 mx-auto mb-1" />
            <div className="text-lg font-extrabold text-gray-700">{student.total_correct}</div>
            <div className="text-[10px] font-semibold text-gray-400">Correct</div>
          </div>
          <div className="bg-red-50 rounded-xl p-3 text-center">
            <FaTimesCircle className="text-red-400 mx-auto mb-1" />
            <div className="text-lg font-extrabold text-gray-700">{student.total_incorrect}</div>
            <div className="text-[10px] font-semibold text-gray-400">Incorrect</div>
          </div>
        </div>

        {/* Average score */}
        <div className="mt-4 bg-purple-50 rounded-xl p-4 flex items-center justify-between">
          <span className="font-bold text-purple-600">Average Score</span>
          <span className="text-2xl font-extrabold text-purple-600">{student.average_score}%</span>
        </div>
      </motion.div>

      {/* Completed Lessons */}
      {completedLessons.length > 0 && (
        <motion.div variants={item}>
          <h2 className="text-lg font-extrabold text-gray-800 mb-3">
            Completed Lessons ({completedLessons.length})
          </h2>
          <div className="space-y-2">
            {completedLessons.map((lesson) => (
              <LessonCard key={lesson.lesson_id} lesson={lesson} />
            ))}
          </div>
        </motion.div>
      )}

      {/* In Progress Lessons */}
      {inProgressLessons.length > 0 && (
        <motion.div variants={item}>
          <h2 className="text-lg font-extrabold text-gray-800 mb-3">
            In Progress ({inProgressLessons.length})
          </h2>
          <div className="space-y-2">
            {inProgressLessons.map((lesson) => (
              <LessonCard key={lesson.lesson_id} lesson={lesson} />
            ))}
          </div>
        </motion.div>
      )}

      {/* Empty state */}
      {progress.length === 0 && (
        <motion.div variants={item} className="text-center py-16">
          <div className="text-6xl mb-4">📊</div>
          <h3 className="text-xl font-bold text-gray-600 mb-2">No progress yet</h3>
          <p className="text-gray-400">This student hasn't started any lessons.</p>
        </motion.div>
      )}
    </motion.div>
  )
}
