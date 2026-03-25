import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaBook, FaGamepad, FaTrophy, FaStar, FaFire, FaCheckCircle } from 'react-icons/fa'
import { useAuth } from '../../features/auth/AuthContext'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.1 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

const MISSION_STYLES = {
  lessons: { emoji: '📚', color: 'from-pink-400 to-rose-500', bg: 'bg-pink-50' },
  stars: { emoji: '⭐', color: 'from-yellow-400 to-amber-500', bg: 'bg-yellow-50' },
  games: { emoji: '🎮', color: 'from-blue-400 to-cyan-500', bg: 'bg-blue-50' },
}

const QUICK_ACCESS = [
  {
    to: '/student/grades',
    icon: FaBook,
    title: 'Learn',
    desc: 'Continue your lessons',
    gradient: 'from-purple-500 to-blue-500',
    shadow: 'shadow-purple-200',
    emoji: '📚',
  },
  {
    to: '/student/play',
    icon: FaGamepad,
    title: 'Play',
    desc: 'Fun math games',
    gradient: 'from-pink-500 to-rose-500',
    shadow: 'shadow-pink-200',
    emoji: '🎮',
  },
  {
    to: '/student/rank',
    icon: FaTrophy,
    title: 'Rank',
    desc: 'See the leaderboard',
    gradient: 'from-orange-500 to-amber-500',
    shadow: 'shadow-orange-200',
    emoji: '🏆',
  },
]

export default function Dashboard() {
  const { user } = useAuth()
  const firstName = (user?.name || 'Student').split(' ')[0]

  const [dashboard, setDashboard] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.get('/dashboard')
      .then((res) => setDashboard(res.data))
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  const missions = dashboard?.daily_missions || []
  const stats = dashboard?.stats || {}
  const userData = dashboard?.user || {}
  const streak = userData.streak || user?.streak || 0
  const xp = userData.xp || user?.xp || 0
  const stars = userData.stars || user?.stars || 0
  const coins = userData.coins || user?.coins || 0
  const lessonsCompleted = stats.lessons_completed || 0
  const totalStars = stats.total_stars || 0

  const streakMessage =
    streak >= 7 ? `${streak}-day streak! You're on fire! 🔥`
    : streak >= 3 ? `${streak}-day streak! Keep going! 💪`
    : streak >= 1 ? `${streak}-day streak! Great start! 🌟`
    : "Start learning today! 🚀"

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-6xl mx-auto space-y-8"
    >
      {/* ── Hero Card ── */}
      <motion.div
        variants={item}
        className="gradient-pink-blue rounded-3xl p-8 lg:p-10 text-white relative overflow-hidden"
      >
        <div className="absolute top-0 right-0 w-64 h-64 bg-white/5 rounded-full -translate-y-1/2 translate-x-1/4" />
        <div className="absolute bottom-0 left-1/3 w-40 h-40 bg-white/5 rounded-full translate-y-1/2" />

        <div className="relative z-10 flex items-center justify-between">
          <div className="flex-1">
            <motion.h1
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 }}
              className="text-4xl lg:text-5xl font-extrabold mb-3"
            >
              Hey {firstName}! 👋
            </motion.h1>
            <motion.p
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.4 }}
              className="text-xl opacity-90 mb-1 font-bold"
            >
              {streakMessage}
            </motion.p>
            <motion.p
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.5 }}
              className="text-base opacity-75 mb-8"
            >
              Let's learn something new today!
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.6 }}
              className="flex flex-wrap gap-3"
            >
              <Link to="/student/grades">
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  className="flex items-center gap-2 bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-5 py-2.5 rounded-xl transition-all border border-white/20"
                >
                  <FaBook /> Continue Learning
                </motion.button>
              </Link>
              <Link to="/student/play">
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  className="flex items-center gap-2 bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-5 py-2.5 rounded-xl transition-all border border-white/20"
                >
                  <FaGamepad /> Play Games
                </motion.button>
              </Link>
              <Link to="/student/rank">
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  className="flex items-center gap-2 bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-5 py-2.5 rounded-xl transition-all border border-white/20"
                >
                  <FaTrophy /> Check Rank
                </motion.button>
              </Link>
            </motion.div>
          </div>

          <div className="hidden lg:block">
            <motion.div
              animate={{ y: [-8, 8, -8] }}
              transition={{ duration: 3, repeat: Infinity, ease: 'easeInOut' }}
              className="text-[120px] leading-none"
            >
              🦉
            </motion.div>
          </div>
        </div>
      </motion.div>

      {/* ── Today's Missions (real data from API) ── */}
      <motion.div variants={item}>
        <div className="flex items-center justify-between mb-5">
          <h2 className="text-2xl font-extrabold text-gray-800">
            Today's Missions 🎯
          </h2>
          {missions.length > 0 && (
            <span className="text-sm font-bold text-gray-400">
              {missions.filter((m) => m.is_completed).length}/{missions.length} completed
            </span>
          )}
        </div>

        {loading ? (
          <div className="text-center py-8 text-gray-400 font-semibold">Loading missions...</div>
        ) : missions.length === 0 ? (
          <div className="text-center py-8 text-gray-400">No missions today</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
            {missions.map((mission, i) => {
              const style = MISSION_STYLES[mission.mission_type] || MISSION_STYLES.lessons
              const percent = mission.target_value > 0
                ? Math.min(100, Math.round((mission.current_value / mission.target_value) * 100))
                : 0

              return (
                <motion.div
                  key={mission.id}
                  variants={item}
                  whileHover={{ y: -4, scale: 1.02 }}
                  className={`bg-white rounded-2xl p-5 shadow-md border border-gray-100 transition-all ${
                    mission.is_completed ? 'ring-2 ring-green-300' : ''
                  }`}
                >
                  <div className="flex items-center justify-between mb-4">
                    <div className={`w-12 h-12 ${style.bg} rounded-xl flex items-center justify-center`}>
                      <span className="text-2xl">{style.emoji}</span>
                    </div>
                    {mission.is_completed ? (
                      <FaCheckCircle className="text-green-500 text-xl" />
                    ) : (
                      <span className="text-xs font-bold text-gray-400 bg-gray-100 px-2 py-1 rounded-full">
                        In Progress
                      </span>
                    )}
                  </div>

                  <h3 className="font-extrabold text-gray-800 mb-3">{mission.title}</h3>

                  <div className="h-3 bg-gray-100 rounded-full overflow-hidden mb-2">
                    <motion.div
                      initial={{ width: 0 }}
                      animate={{ width: `${percent}%` }}
                      transition={{ duration: 1, delay: 0.5 + i * 0.2 }}
                      className={`h-full bg-gradient-to-r ${style.color} rounded-full`}
                    />
                  </div>
                  <div className="flex justify-between text-sm">
                    <span className="font-bold text-gray-500">
                      {mission.current_value}/{mission.target_value} done
                    </span>
                    <span className="font-bold text-gray-400">{percent}%</span>
                  </div>
                </motion.div>
              )
            })}
          </div>
        )}
      </motion.div>

      {/* ── Quick Access (replaces Recommended) ── */}
      <motion.div variants={item}>
        <h2 className="text-2xl font-extrabold text-gray-800 mb-5">
          Quick Access 🚀
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {QUICK_ACCESS.map((qa) => (
            <Link key={qa.to} to={qa.to}>
              <motion.div
                variants={item}
                whileHover={{ y: -6, scale: 1.03 }}
                whileTap={{ scale: 0.97 }}
                className={`bg-gradient-to-br ${qa.gradient} rounded-2xl p-6 text-white shadow-lg ${qa.shadow} cursor-pointer relative overflow-hidden`}
              >
                <div className="absolute top-2 right-3 text-5xl opacity-20 select-none pointer-events-none">
                  {qa.emoji}
                </div>
                <div className="relative z-10">
                  <qa.icon className="text-3xl mb-3 opacity-90" />
                  <h3 className="text-xl font-extrabold mb-1">{qa.title}</h3>
                  <p className="text-sm opacity-80 font-semibold">{qa.desc}</p>
                </div>
              </motion.div>
            </Link>
          ))}
        </div>
      </motion.div>

      {/* ── Stats Row (real data) ── */}
      <motion.div variants={item} className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2"><FaFire className="inline text-orange-400" /></div>
          <div className="text-2xl font-extrabold text-gray-800">{streak}</div>
          <div className="text-sm font-bold text-gray-400">Day Streak</div>
        </div>
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2">📚</div>
          <div className="text-2xl font-extrabold text-gray-800">{lessonsCompleted}</div>
          <div className="text-sm font-bold text-gray-400">Lessons Done</div>
        </div>
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2"><FaStar className="inline text-yellow-400" /></div>
          <div className="text-2xl font-extrabold text-gray-800">{totalStars}</div>
          <div className="text-sm font-bold text-gray-400">Stars Earned</div>
        </div>
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2">💰</div>
          <div className="text-2xl font-extrabold text-gray-800">{coins}</div>
          <div className="text-sm font-bold text-gray-400">Coins</div>
        </div>
      </motion.div>
    </motion.div>
  )
}
