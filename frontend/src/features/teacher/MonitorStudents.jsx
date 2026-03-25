import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  FaUsers, FaChartBar, FaTrophy, FaExclamationTriangle, FaSpinner,
  FaStar, FaCoins, FaFire, FaCheckCircle, FaTimesCircle, FaSearch,
} from 'react-icons/fa'
import toast from 'react-hot-toast'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.06 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

const avatarGradients = [
  'from-blue-400 to-cyan-400',
  'from-pink-400 to-rose-400',
  'from-green-400 to-emerald-400',
  'from-purple-400 to-violet-400',
  'from-orange-400 to-amber-400',
  'from-teal-400 to-green-400',
  'from-red-400 to-pink-400',
  'from-indigo-400 to-blue-400',
]

function daysSince(dateStr) {
  if (!dateStr) return null
  const diff = Date.now() - new Date(dateStr).getTime()
  return Math.floor(diff / (1000 * 60 * 60 * 24))
}

function formatLastLogin(dateStr) {
  if (!dateStr) return 'Never'
  const days = daysSince(dateStr)
  if (days === 0) return 'Today'
  if (days === 1) return 'Yesterday'
  return `${days} days ago`
}

export default function MonitorStudents() {
  const [students, setStudents] = useState([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')

  useEffect(() => {
    const fetchStudents = async () => {
      setLoading(true)
      try {
        const response = await api.get('/teacher/students')
        setStudents(response.data)
      } catch (err) {
        toast.error('Failed to load students')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }
    fetchStudents()
  }, [])

  const filteredStudents = students.filter((s) =>
    s.name.toLowerCase().includes(search.toLowerCase()) ||
    s.email.toLowerCase().includes(search.toLowerCase())
  )

  // Computed summary stats
  const totalStudents = students.length
  const averageScore = totalStudents > 0
    ? (students.reduce((sum, s) => sum + (s.average_score || 0), 0) / totalStudents).toFixed(1)
    : 0
  const topPerformer = students.length > 0
    ? students.reduce((top, s) => (s.stars || 0) > (top.stars || 0) ? s : top, students[0])
    : null
  const inactiveCount = students.filter((s) => {
    const days = daysSince(s.last_login_date)
    return days === null || days > 3
  }).length

  const summaryCards = [
    { title: 'Total Students', value: totalStudents, icon: FaUsers, color: 'text-blue-600', bg: 'bg-blue-50' },
    { title: 'Average Score', value: `${averageScore}%`, icon: FaChartBar, color: 'text-green-600', bg: 'bg-green-50' },
    {
      title: 'Top Performer',
      value: topPerformer?.name?.split(' ')[0] || '-',
      subtitle: topPerformer ? `${topPerformer.stars || 0} stars` : '',
      icon: FaTrophy, color: 'text-orange-600', bg: 'bg-orange-50',
    },
    {
      title: 'Inactive (>3 days)',
      value: inactiveCount,
      icon: FaExclamationTriangle,
      color: inactiveCount > 0 ? 'text-red-600' : 'text-green-600',
      bg: inactiveCount > 0 ? 'bg-red-50' : 'bg-green-50',
    },
  ]

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <FaSpinner className="animate-spin text-4xl text-orange-400 mb-4" />
        <p className="text-gray-400 font-semibold">Loading students...</p>
      </div>
    )
  }

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-7xl mx-auto space-y-8"
    >
      {/* Page Header */}
      <motion.div variants={item}>
        <h1 className="text-3xl font-extrabold text-gray-800">Monitor Students</h1>
        <p className="text-gray-500 mt-1">Track student progress, scores, and performance.</p>
      </motion.div>

      {/* Summary Stats */}
      <motion.div variants={item} className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        {summaryCards.map((card) => (
          <motion.div
            key={card.title}
            variants={item}
            whileHover={{ y: -4, scale: 1.02 }}
            className="bg-white rounded-2xl p-5 shadow-md border border-gray-100"
          >
            <div className="flex items-center gap-3 mb-3">
              <div className={`w-10 h-10 ${card.bg} rounded-xl flex items-center justify-center`}>
                <card.icon className={`text-lg ${card.color}`} />
              </div>
              <span className="text-sm font-semibold text-gray-400">{card.title}</span>
            </div>
            <div className={`text-2xl font-extrabold ${card.color}`}>{card.value}</div>
            {card.subtitle && (
              <p className="text-xs text-gray-400 font-semibold mt-0.5">{card.subtitle}</p>
            )}
          </motion.div>
        ))}
      </motion.div>

      {/* Search */}
      <motion.div variants={item}>
        <div className="relative">
          <FaSearch className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-300" />
          <input
            type="text"
            placeholder="Search students by name or email..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full pl-11 pr-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
          />
        </div>
      </motion.div>

      {/* Student Cards Grid */}
      {filteredStudents.length === 0 ? (
        <motion.div variants={item} className="text-center py-20">
          <div className="text-6xl mb-4">📚</div>
          <p className="text-gray-400 font-bold text-lg">No students found</p>
          <p className="text-gray-300 text-sm mt-1">Create student accounts to start monitoring.</p>
        </motion.div>
      ) : (
        <motion.div
          variants={item}
          className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5"
        >
          {filteredStudents.map((student, index) => {
            const lastLoginStr = student.last_login_date
            const inactive = daysSince(lastLoginStr) === null || daysSince(lastLoginStr) > 3
            const xpPercent = Math.min(100, Math.round(((student.xp || 0) % 500) / 5))

            return (
              <motion.div
                key={student.id}
                variants={item}
                whileHover={{ y: -4 }}
                className={`bg-white rounded-2xl shadow-md border overflow-hidden transition-all ${
                  inactive ? 'border-red-200' : 'border-gray-100'
                }`}
              >
                {inactive && (
                  <div className="bg-red-50 px-4 py-1.5 flex items-center gap-2">
                    <FaExclamationTriangle className="text-red-400 text-xs" />
                    <span className="text-xs font-bold text-red-500">
                      Inactive for {daysSince(lastLoginStr) ?? 'N/A'} days
                    </span>
                  </div>
                )}

                <div className="p-5">
                  {/* Top row: avatar + name */}
                  <div className="flex items-center gap-4 mb-4">
                    <div className={`w-14 h-14 rounded-full bg-gradient-to-br ${avatarGradients[index % avatarGradients.length]} flex items-center justify-center text-white font-extrabold text-xl shadow-lg flex-shrink-0`}>
                      {(student.name || '?')[0].toUpperCase()}
                    </div>
                    <div className="flex-1 min-w-0">
                      <h3 className="font-extrabold text-gray-800 text-lg truncate">{student.name}</h3>
                      <p className="text-xs text-gray-400 truncate">{student.email}</p>
                    </div>
                  </div>

                  {/* Level + XP bar */}
                  <div className="mb-4">
                    <div className="flex items-center justify-between mb-1.5">
                      <span className="text-sm font-bold text-gray-600">Level {student.level || 1}</span>
                      <span className="text-xs font-semibold text-gray-400">{student.xp || 0} XP</span>
                    </div>
                    <div className="h-3 bg-gray-100 rounded-full overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${xpPercent}%` }}
                        transition={{ duration: 1, delay: index * 0.05 }}
                        className="h-full bg-gradient-to-r from-orange-400 to-amber-500 rounded-full"
                      />
                    </div>
                  </div>

                  {/* Stats row */}
                  <div className="grid grid-cols-3 gap-3 mb-4">
                    <div className="bg-yellow-50 rounded-xl p-2.5 text-center">
                      <FaStar className="text-yellow-500 mx-auto mb-1" />
                      <div className="text-sm font-extrabold text-gray-700">{student.stars || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Stars</div>
                    </div>
                    <div className="bg-green-50 rounded-xl p-2.5 text-center">
                      <FaCheckCircle className="text-green-500 mx-auto mb-1" />
                      <div className="text-sm font-extrabold text-gray-700">{student.total_correct || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Correct</div>
                    </div>
                    <div className="bg-red-50 rounded-xl p-2.5 text-center">
                      <FaTimesCircle className="text-red-400 mx-auto mb-1" />
                      <div className="text-sm font-extrabold text-gray-700">{student.total_incorrect || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Incorrect</div>
                    </div>
                  </div>

                  {/* Progress summary */}
                  <div className="grid grid-cols-3 gap-3 mb-4">
                    <div className="bg-blue-50 rounded-xl p-2.5 text-center">
                      <div className="text-sm font-extrabold text-blue-600">{student.lessons_completed || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Lessons</div>
                    </div>
                    <div className="bg-purple-50 rounded-xl p-2.5 text-center">
                      <div className="text-sm font-extrabold text-purple-600">{student.average_score || 0}%</div>
                      <div className="text-[10px] font-semibold text-gray-400">Avg Score</div>
                    </div>
                    <div className="bg-orange-50 rounded-xl p-2.5 text-center">
                      <FaFire className="text-orange-500 mx-auto mb-1" />
                      <div className="text-sm font-extrabold text-gray-700">{student.streak || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Streak</div>
                    </div>
                  </div>

                  {/* Footer */}
                  <div className="flex items-center justify-between">
                    <span className="text-xs text-gray-400 font-semibold">
                      Last login: {formatLastLogin(lastLoginStr)}
                    </span>
                    <Link to={`/teacher/students/${student.id}`}>
                      <motion.button
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        className="text-xs font-bold text-orange-500 hover:text-orange-600 transition-colors"
                      >
                        View Details &rarr;
                      </motion.button>
                    </Link>
                  </div>

                  {/* Parent info */}
                  {student.parent_name && (
                    <div className="mt-3 pt-3 border-t border-gray-100">
                      <span className="text-xs text-gray-400">
                        Parent: <span className="font-semibold text-gray-600">{student.parent_name}</span>
                      </span>
                    </div>
                  )}
                </div>
              </motion.div>
            )
          })}
        </motion.div>
      )}
    </motion.div>
  )
}
