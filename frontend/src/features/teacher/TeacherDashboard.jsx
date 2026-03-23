import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaUsers, FaUserFriends, FaBolt, FaChartLine, FaUserPlus, FaEye, FaClock } from 'react-icons/fa'
import { useAuth } from '../../features/auth/AuthContext'

// Mock stats data
const statsCards = [
  {
    title: 'Total Students',
    value: 42,
    icon: FaUsers,
    bg: 'bg-blue-500',
    lightBg: 'bg-blue-50',
    textColor: 'text-blue-600',
  },
  {
    title: 'Total Parents',
    value: 28,
    icon: FaUserFriends,
    bg: 'bg-green-500',
    lightBg: 'bg-green-50',
    textColor: 'text-green-600',
  },
  {
    title: 'Active Today',
    value: 18,
    icon: FaBolt,
    bg: 'bg-orange-500',
    lightBg: 'bg-orange-50',
    textColor: 'text-orange-600',
  },
  {
    title: 'Average Score',
    value: '78%',
    icon: FaChartLine,
    bg: 'bg-purple-500',
    lightBg: 'bg-purple-50',
    textColor: 'text-purple-600',
  },
]

// Mock recent activity
const recentActivities = [
  {
    id: 1,
    text: 'Alex completed Lesson: Addition Basics',
    time: '2 min ago',
    avatar: 'A',
    color: 'from-blue-400 to-cyan-400',
  },
  {
    id: 2,
    text: 'Sarah earned 3 stars on Quiz: Subtraction',
    time: '15 min ago',
    avatar: 'S',
    color: 'from-pink-400 to-rose-400',
  },
  {
    id: 3,
    text: 'Tom started Grade 2',
    time: '1 hour ago',
    avatar: 'T',
    color: 'from-green-400 to-emerald-400',
  },
  {
    id: 4,
    text: 'Emily scored 95% on Multiplication Quiz',
    time: '2 hours ago',
    avatar: 'E',
    color: 'from-purple-400 to-violet-400',
  },
  {
    id: 5,
    text: 'Jake unlocked the Geometry badge',
    time: '3 hours ago',
    avatar: 'J',
    color: 'from-orange-400 to-amber-400',
  },
  {
    id: 6,
    text: 'Mia completed all daily missions',
    time: '4 hours ago',
    avatar: 'M',
    color: 'from-teal-400 to-green-400',
  },
]

// Quick actions
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
]

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.08 },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function TeacherDashboard() {
  const { user } = useAuth()
  const firstName = (user?.name || 'Teacher').split(' ')[0]

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
      <motion.div variants={item} className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        {statsCards.map((stat, i) => (
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
              <span className={`text-xs font-bold ${stat.textColor} ${stat.lightBg} px-2 py-1 rounded-full`}>
                +12%
              </span>
            </div>
            <div className="text-3xl font-extrabold text-gray-800 mb-1">{stat.value}</div>
            <div className="text-sm font-semibold text-gray-400">{stat.title}</div>
          </motion.div>
        ))}
      </motion.div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recent Activity */}
        <motion.div variants={item} className="lg:col-span-2">
          <div className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden">
            <div className="flex items-center justify-between p-6 pb-4">
              <h2 className="text-xl font-extrabold text-gray-800">Recent Activity</h2>
              <FaClock className="text-gray-300" />
            </div>
            <div className="divide-y divide-gray-50">
              {recentActivities.map((activity) => (
                <motion.div
                  key={activity.id}
                  whileHover={{ backgroundColor: 'rgba(249,250,251,1)' }}
                  className="flex items-center gap-4 px-6 py-4 transition-colors"
                >
                  <div className={`w-10 h-10 rounded-full bg-gradient-to-br ${activity.color} flex items-center justify-center text-white font-bold text-sm flex-shrink-0`}>
                    {activity.avatar}
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-semibold text-gray-700 truncate">
                      {activity.text}
                    </p>
                    <p className="text-xs text-gray-400 mt-0.5">{activity.time}</p>
                  </div>
                </motion.div>
              ))}
            </div>
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
