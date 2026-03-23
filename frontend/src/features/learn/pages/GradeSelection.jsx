import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaStar } from 'react-icons/fa'
import { ImSpinner8 } from 'react-icons/im'
import toast from 'react-hot-toast'
import api from '../../../utils/api'

const GRADE_EMOJIS = { 1: '🐣', 2: '🐥', 3: '🦊', 4: '🦁', 5: '🦅' }

const GRADE_COLORS = [
  { color: 'from-green-400 to-emerald-500', shadow: 'shadow-green-200' },
  { color: 'from-blue-400 to-cyan-500', shadow: 'shadow-blue-200' },
  { color: 'from-purple-400 to-violet-500', shadow: 'shadow-purple-200' },
  { color: 'from-orange-400 to-amber-500', shadow: 'shadow-orange-200' },
  { color: 'from-red-400 to-rose-500', shadow: 'shadow-red-200' },
]

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.1 } },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function GradeSelection() {
  const [grades, setGrades] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchGrades = async () => {
      try {
        const response = await api.get('/grades')
        setGrades(response.data)
      } catch (error) {
        console.error('Failed to fetch grades:', error)
        toast.error('Failed to load grades. Please try again!')
      } finally {
        setLoading(false)
      }
    }
    fetchGrades()
  }, [])

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <ImSpinner8 className="text-5xl text-primary-500 animate-spin mb-4" />
        <p className="text-lg font-bold text-gray-500">Loading grades...</p>
      </div>
    )
  }

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-5xl mx-auto"
    >
      {/* Header */}
      <motion.div variants={item} className="text-center mb-10">
        <h1 className="text-4xl font-extrabold text-gray-800 mb-2">
          Choose Your Grade 🎓
        </h1>
        <p className="text-lg text-gray-500 font-medium">
          Pick a grade and start learning amazing math skills!
        </p>
      </motion.div>

      {/* Grade Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {grades.map((grade, index) => {
          const colorSet = GRADE_COLORS[index % GRADE_COLORS.length]
          const emoji = GRADE_EMOJIS[grade.number] || '📚'
          const progress = grade.total_lessons > 0
            ? Math.round((grade.completed_lessons / grade.total_lessons) * 100)
            : 0
          const stars = progress >= 100 ? 3 : progress >= 60 ? 2 : progress >= 30 ? 1 : 0

          return (
            <motion.div
              key={grade.id}
              variants={item}
              whileHover={{ y: -8, scale: 1.03 }}
              whileTap={{ scale: 0.98 }}
            >
              <Link to={`/student/grades/${grade.id}`} className="block">
                <div className={`bg-white rounded-3xl overflow-hidden shadow-lg ${colorSet.shadow} border border-gray-100 transition-all hover:shadow-xl`}>
                  {/* Top gradient header */}
                  <div className={`bg-gradient-to-br ${colorSet.color} p-6 text-white relative overflow-hidden`}>
                    <div className="absolute -top-6 -right-6 w-24 h-24 bg-white/10 rounded-full" />
                    <div className="absolute -bottom-4 -left-4 w-16 h-16 bg-white/10 rounded-full" />
                    <div className="relative z-10 flex items-center justify-between">
                      <span className="text-5xl">{emoji}</span>
                      <div className="text-right">
                        <div className="text-4xl font-extrabold">{grade.number}</div>
                        <div className="text-sm font-bold opacity-80">Grade</div>
                      </div>
                    </div>
                  </div>

                  {/* Content */}
                  <div className="p-5">
                    <h3 className="text-lg font-extrabold text-gray-800 mb-1">{grade.name}</h3>
                    <p className="text-sm text-gray-500 font-medium mb-4">{grade.description || 'Math Lessons'}</p>

                    {/* Stars */}
                    <div className="flex items-center gap-1 mb-4">
                      {[1, 2, 3].map((s) => (
                        <FaStar key={s} className={`text-lg ${s <= stars ? 'text-yellow-400' : 'text-gray-200'}`} />
                      ))}
                    </div>

                    {/* Progress bar */}
                    <div className="mb-2">
                      <div className="flex justify-between text-sm mb-1">
                        <span className="font-bold text-gray-600">{progress}% complete</span>
                        <span className="font-medium text-gray-400">{grade.total_lessons} lessons</span>
                      </div>
                      <div className="h-3 bg-gray-100 rounded-full overflow-hidden">
                        <motion.div
                          initial={{ width: 0 }}
                          animate={{ width: `${progress}%` }}
                          transition={{ duration: 1, ease: 'easeOut' }}
                          className={`h-full bg-gradient-to-r ${colorSet.color} rounded-full`}
                        />
                      </div>
                    </div>

                    {/* CTA */}
                    <div className="mt-4 text-center">
                      <span className={`inline-block text-sm font-extrabold ${progress === 0 ? 'text-gray-400' : 'text-secondary-500'}`}>
                        {progress === 0 ? 'Start Learning! 🚀' : progress === 100 ? 'Review Lessons ✅' : 'Continue Learning 📖'}
                      </span>
                    </div>
                  </div>
                </div>
              </Link>
            </motion.div>
          )
        })}
      </div>
    </motion.div>
  )
}
