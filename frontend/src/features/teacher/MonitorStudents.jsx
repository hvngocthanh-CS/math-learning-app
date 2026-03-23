import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { FaUsers, FaChartBar, FaTrophy, FaExclamationTriangle, FaSpinner, FaStar, FaCoins, FaFire } from 'react-icons/fa'
import toast from 'react-hot-toast'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.06 },
  },
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

function getAvatarGradient(index) {
  return avatarGradients[index % avatarGradients.length]
}

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
  const [expandedId, setExpandedId] = useState(null)

  useEffect(() => {
    const fetchStudents = async () => {
      setLoading(true)
      try {
        const response = await api.get('/users?role=student')
        const data = response.data
        setStudents(Array.isArray(data) ? data : data.users || [])
      } catch (err) {
        toast.error('Failed to load students')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }
    fetchStudents()
  }, [])

  // Computed summary stats
  const totalStudents = students.length
  const averageLevel = totalStudents > 0
    ? (students.reduce((sum, s) => sum + (s.level || 0), 0) / totalStudents).toFixed(1)
    : 0
  const topPerformer = students.length > 0
    ? students.reduce((top, s) => (s.stars || 0) > (top.stars || 0) ? s : top, students[0])
    : null
  const inactiveStudents = students.filter((s) => {
    const days = daysSince(s.lastLogin || s.last_login)
    return days === null || days > 3
  })

  const summaryCards = [
    {
      title: 'Total Students',
      value: totalStudents,
      icon: FaUsers,
      color: 'text-blue-600',
      bg: 'bg-blue-50',
    },
    {
      title: 'Average Level',
      value: averageLevel,
      icon: FaChartBar,
      color: 'text-green-600',
      bg: 'bg-green-50',
    },
    {
      title: 'Top Performer',
      value: topPerformer?.name?.split(' ')[0] || '-',
      subtitle: topPerformer ? `${topPerformer.stars || 0} stars` : '',
      icon: FaTrophy,
      color: 'text-orange-600',
      bg: 'bg-orange-50',
    },
    {
      title: 'Inactive (>3 days)',
      value: inactiveStudents.length,
      icon: FaExclamationTriangle,
      color: inactiveStudents.length > 0 ? 'text-red-600' : 'text-green-600',
      bg: inactiveStudents.length > 0 ? 'bg-red-50' : 'bg-green-50',
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
        <p className="text-gray-500 mt-1">Track student progress, levels, and engagement.</p>
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

      {/* Student Cards Grid */}
      {students.length === 0 ? (
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
          {students.map((student, index) => {
            const isExpanded = expandedId === (student._id || student.id)
            const lastLoginStr = student.lastLogin || student.last_login
            const inactive = daysSince(lastLoginStr) === null || daysSince(lastLoginStr) > 3
            const xp = student.xp || 0
            const xpMax = student.xpMax || student.xp_max || 1000
            const xpPercent = Math.min(100, Math.round((xp / xpMax) * 100))

            return (
              <motion.div
                key={student._id || student.id || index}
                variants={item}
                whileHover={{ y: -4 }}
                layout
                className={`bg-white rounded-2xl shadow-md border overflow-hidden transition-all ${
                  inactive ? 'border-red-200' : 'border-gray-100'
                }`}
              >
                {/* Inactive Warning Banner */}
                {inactive && (
                  <div className="bg-red-50 px-4 py-1.5 flex items-center gap-2">
                    <FaExclamationTriangle className="text-red-400 text-xs" />
                    <span className="text-xs font-bold text-red-500">Inactive for {daysSince(lastLoginStr) ?? 'N/A'} days</span>
                  </div>
                )}

                <div className="p-5">
                  {/* Top row: avatar + name */}
                  <div className="flex items-center gap-4 mb-4">
                    <div className={`w-14 h-14 rounded-full bg-gradient-to-br ${getAvatarGradient(index)} flex items-center justify-center text-white font-extrabold text-xl shadow-lg flex-shrink-0`}>
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
                      <span className="text-sm font-bold text-gray-600">
                        Level {student.level || 1}
                      </span>
                      <span className="text-xs font-semibold text-gray-400">
                        {xp} / {xpMax} XP
                      </span>
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
                    <div className="bg-amber-50 rounded-xl p-2.5 text-center">
                      <FaCoins className="text-amber-500 mx-auto mb-1" />
                      <div className="text-sm font-extrabold text-gray-700">{student.coins || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Coins</div>
                    </div>
                    <div className="bg-orange-50 rounded-xl p-2.5 text-center">
                      <FaFire className="text-orange-500 mx-auto mb-1" />
                      <div className="text-sm font-extrabold text-gray-700">{student.streak || 0}</div>
                      <div className="text-[10px] font-semibold text-gray-400">Streak</div>
                    </div>
                  </div>

                  {/* Last login */}
                  <div className="flex items-center justify-between">
                    <span className="text-xs text-gray-400 font-semibold">
                      Last login: {formatLastLogin(lastLoginStr)}
                    </span>
                    <motion.button
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() =>
                        setExpandedId(isExpanded ? null : student._id || student.id)
                      }
                      className="text-xs font-bold text-orange-500 hover:text-orange-600 transition-colors"
                    >
                      {isExpanded ? 'Hide Details' : 'View Details'}
                    </motion.button>
                  </div>

                  {/* Expanded Details */}
                  {isExpanded && (
                    <motion.div
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: 'auto' }}
                      exit={{ opacity: 0, height: 0 }}
                      className="mt-4 pt-4 border-t border-gray-100"
                    >
                      <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                          <span className="text-gray-400 font-semibold">Email</span>
                          <span className="text-gray-700 font-medium">{student.email}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-gray-400 font-semibold">Grade</span>
                          <span className="text-gray-700 font-medium">{student.grade || '-'}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-gray-400 font-semibold">Lessons Completed</span>
                          <span className="text-gray-700 font-medium">{student.lessonsCompleted || student.lessons_completed || 0}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-gray-400 font-semibold">Quizzes Taken</span>
                          <span className="text-gray-700 font-medium">{student.quizzesTaken || student.quizzes_taken || 0}</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-gray-400 font-semibold">Average Score</span>
                          <span className="text-gray-700 font-medium">{student.averageScore || student.average_score || '-'}%</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-gray-400 font-semibold">Joined</span>
                          <span className="text-gray-700 font-medium">
                            {student.createdAt || student.created_at
                              ? new Date(student.createdAt || student.created_at).toLocaleDateString('en-US', {
                                  month: 'short',
                                  day: 'numeric',
                                  year: 'numeric',
                                })
                              : '-'}
                          </span>
                        </div>
                      </div>
                    </motion.div>
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
