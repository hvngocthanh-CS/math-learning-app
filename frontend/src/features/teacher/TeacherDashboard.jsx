import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  FaUsers, FaUserFriends, FaBolt, FaChartLine, FaUserPlus, FaEye,
  FaStar, FaSpinner, FaBook, FaTrophy,
} from 'react-icons/fa'
import { useAuth } from '../../features/auth/AuthContext'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

const quickActions = [
  {
    title: 'Create Student Account',
    description: 'Add a new student to your class',
    icon: FaUserPlus,
    link: '/teacher/accounts',
    color: 'from-blue-500 to-blue-600',
  },
  {
    title: 'Create Parent Account',
    description: 'Set up a parent to monitor their child',
    icon: FaUserFriends,
    link: '/teacher/accounts',
    color: 'from-green-500 to-green-600',
  },
  {
    title: 'View All Students',
    description: 'Monitor progress and performance',
    icon: FaEye,
    link: '/teacher/students',
    color: 'from-orange-500 to-orange-600',
  },
  {
    title: 'View Rankings',
    description: 'See student leaderboard',
    icon: FaTrophy,
    link: '/teacher/ranking',
    color: 'from-purple-500 to-purple-600',
  },
]

export default function TeacherDashboard() {
  const { user } = useAuth()
  const firstName = (user?.name || 'Teacher').split(' ')[0]
  const [stats, setStats] = useState(null)
  const [topStudents, setTopStudents] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [statsRes, studentsRes] = await Promise.all([
          api.get('/teacher/dashboard'),
          api.get('/teacher/students'),
        ])
        setStats(statsRes.data)
        // Top 5 students by stars
        const sorted = [...studentsRes.data].sort((a, b) => b.stars - a.stars).slice(0, 5)
        setTopStudents(sorted)
      } catch (err) {
        console.error('Failed to load dashboard:', err)
      } finally {
        setLoading(false)
      }
    }
    fetchData()
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <FaSpinner className="animate-spin text-4xl text-orange-400" />
      </div>
    )
  }

  const statsCards = [
    {
      title: 'Total Students',
      value: stats?.total_students ?? 0,
      icon: FaUsers,
      bg: 'bg-blue-500',
      lightBg: 'bg-blue-50',
      textColor: 'text-blue-600',
    },
    {
      title: 'Total Parents',
      value: stats?.total_parents ?? 0,
      icon: FaUserFriends,
      bg: 'bg-green-500',
      lightBg: 'bg-green-50',
      textColor: 'text-green-600',
    },
    {
      title: 'Active Today',
      value: stats?.active_today ?? 0,
      icon: FaBolt,
      bg: 'bg-orange-500',
      lightBg: 'bg-orange-50',
      textColor: 'text-orange-600',
    },
    {
      title: 'Average Score',
      value: `${stats?.average_score ?? 0}%`,
      icon: FaChartLine,
      bg: 'bg-purple-500',
      lightBg: 'bg-purple-50',
      textColor: 'text-purple-600',
    },
    {
      title: 'Lessons Completed',
      value: stats?.total_lessons_completed ?? 0,
      icon: FaBook,
      bg: 'bg-pink-500',
      lightBg: 'bg-pink-50',
      textColor: 'text-pink-600',
    },
    {
      title: 'Avg Stars/Student',
      value: stats?.average_stars ?? 0,
      icon: FaStar,
      bg: 'bg-yellow-500',
      lightBg: 'bg-yellow-50',
      textColor: 'text-yellow-600',
    },
  ]

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-7xl mx-auto space-y-8"
    >
      {/* Welcome Header */}
      <motion.div variants={item}>
        <h1 className="text-3xl font-extrabold text-gray-800">
          Welcome back, {firstName}!
        </h1>
        <p className="text-gray-500 mt-1">
          Here's what's happening with your students today.
        </p>
      </motion.div>

      {/* Stats Cards */}
      <motion.div variants={item} className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        {statsCards.map((stat) => (
          <motion.div
            key={stat.title}
            variants={item}
            whileHover={{ y: -4, scale: 1.02 }}
            className="bg-white rounded-2xl p-6 shadow-md border border-gray-100"
          >
            <div className="flex items-center justify-between mb-4">
              <div className={`w-12 h-12 ${stat.lightBg} rounded-xl flex items-center justify-center`}>
                <stat.icon className={`text-xl ${stat.textColor}`} />
              </div>
            </div>
            <div className="text-3xl font-extrabold text-gray-800 mb-1">{stat.value}</div>
            <div className="text-sm font-semibold text-gray-400">{stat.title}</div>
          </motion.div>
        ))}
      </motion.div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Top Students */}
        <motion.div variants={item} className="lg:col-span-2">
          <div className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden">
            <div className="flex items-center justify-between p-6 pb-4">
              <h2 className="text-xl font-extrabold text-gray-800">Top Students</h2>
              <FaTrophy className="text-yellow-400" />
            </div>
            {topStudents.length === 0 ? (
              <div className="text-center py-12 text-gray-400">No students yet</div>
            ) : (
              <div className="divide-y divide-gray-50">
                {topStudents.map((student, i) => (
                  <Link key={student.id} to={`/teacher/students/${student.id}`}>
                    <motion.div
                      whileHover={{ backgroundColor: 'rgba(249,250,251,1)' }}
                      className="flex items-center gap-4 px-6 py-4 transition-colors cursor-pointer"
                    >
                      <div className="w-8 text-center font-extrabold text-gray-300 text-lg">
                        {i + 1}
                      </div>
                      <div className={`w-10 h-10 rounded-full bg-gradient-to-br from-orange-400 to-amber-500 flex items-center justify-center text-white font-bold text-sm flex-shrink-0`}>
                        {student.name[0].toUpperCase()}
                      </div>
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-bold text-gray-700 truncate">{student.name}</p>
                        <p className="text-xs text-gray-400">Level {student.level} • {student.lessons_completed} lessons</p>
                      </div>
                      <div className="flex items-center gap-3 text-sm">
                        <div className="flex items-center gap-1">
                          <FaStar className="text-yellow-400 text-xs" />
                          <span className="font-bold text-gray-600">{student.stars}</span>
                        </div>
                        <div className="text-xs text-gray-400">
                          Avg: {student.average_score}%
                        </div>
                      </div>
                    </motion.div>
                  </Link>
                ))}
              </div>
            )}
          </div>
        </motion.div>

        {/* Quick Actions */}
        <motion.div variants={item}>
          <div className="bg-white rounded-2xl shadow-md border border-gray-100 p-6">
            <h2 className="text-xl font-extrabold text-gray-800 mb-5">Quick Actions</h2>
            <div className="space-y-4">
              {quickActions.map((action) => (
                <Link key={action.title} to={action.link}>
                  <motion.div
                    whileHover={{ scale: 1.02, x: 4 }}
                    whileTap={{ scale: 0.98 }}
                    className="flex items-center gap-4 p-4 rounded-xl border border-gray-100 hover:border-orange-200 hover:shadow-md transition-all cursor-pointer group"
                  >
                    <div className={`w-11 h-11 rounded-xl bg-gradient-to-br ${action.color} flex items-center justify-center text-white flex-shrink-0 shadow-md`}>
                      <action.icon className="text-lg" />
                    </div>
                    <div className="flex-1">
                      <h3 className="text-sm font-bold text-gray-700 group-hover:text-orange-600 transition-colors">
                        {action.title}
                      </h3>
                      <p className="text-xs text-gray-400 mt-0.5">{action.description}</p>
                    </div>
                    <span className="text-gray-300 group-hover:text-orange-400 transition-colors text-lg">
                      &rarr;
                    </span>
                  </motion.div>
                </Link>
              ))}
            </div>
          </div>
        </motion.div>
      </div>
    </motion.div>
  )
}
