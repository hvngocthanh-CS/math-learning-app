import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaBook, FaGamepad, FaTrophy, FaStar, FaFire, FaCheckCircle } from 'react-icons/fa'
import { useAuth } from '../../features/auth/AuthContext'

// Mock data
const missions = [
  {
    id: 1,
    title: 'Complete 3 Lessons',
    emoji: '📚',
    current: 2,
    target: 3,
    reward: '50 XP',
    color: 'from-pink-400 to-rose-500',
    bg: 'bg-pink-50',
  },
  {
    id: 2,
    title: 'Earn 100 Stars',
    emoji: '⭐',
    current: 75,
    target: 100,
    reward: '30 Coins',
    color: 'from-yellow-400 to-amber-500',
    bg: 'bg-yellow-50',
  },
  {
    id: 3,
    title: 'Win 2 Games',
    emoji: '🎮',
    current: 1,
    target: 2,
    reward: '1 Trophy',
    color: 'from-secondary-400 to-blue-500',
    bg: 'bg-blue-50',
  },
]

const recommendedLessons = [
  {
    id: 1,
    title: 'Fractions Fun',
    emoji: '🍕',
    difficulty: 'Easy',
    xp: 30,
    color: 'from-green-400 to-emerald-500',
  },
  {
    id: 2,
    title: 'Multiplication Master',
    emoji: '✖️',
    difficulty: 'Medium',
    xp: 50,
    color: 'from-purple-400 to-violet-500',
  },
  {
    id: 3,
    title: 'Geometry Shapes',
    emoji: '📐',
    difficulty: 'Easy',
    xp: 25,
    color: 'from-blue-400 to-cyan-500',
  },
  {
    id: 4,
    title: 'Word Problems',
    emoji: '📝',
    difficulty: 'Hard',
    xp: 75,
    color: 'from-orange-400 to-red-500',
  },
  {
    id: 5,
    title: 'Decimals & Percents',
    emoji: '💯',
    difficulty: 'Medium',
    xp: 45,
    color: 'from-teal-400 to-green-500',
  },
]

const difficultyColors = {
  Easy: 'bg-green-100 text-green-700',
  Medium: 'bg-yellow-100 text-yellow-700',
  Hard: 'bg-red-100 text-red-700',
}

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1 },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function Dashboard() {
  const { user } = useAuth()
  const firstName = (user?.name || 'Student').split(' ')[0]

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-6xl mx-auto space-y-8"
    >
      {/* Hero Card */}
      <motion.div
        variants={item}
        className="gradient-pink-blue rounded-3xl p-8 lg:p-10 text-white relative overflow-hidden"
      >
        {/* Background decorations */}
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
              You're doing AMAZING! 7-day streak! 🎉
            </motion.p>
            <motion.p
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.5 }}
              className="text-base opacity-75 mb-8"
            >
              Let's learn something new today!
            </motion.p>

            {/* Action buttons */}
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
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="flex items-center gap-2 bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-5 py-2.5 rounded-xl transition-all border border-white/20"
              >
                <FaGamepad /> Play Games
              </motion.button>
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="flex items-center gap-2 bg-white/20 backdrop-blur-sm hover:bg-white/30 text-white font-bold px-5 py-2.5 rounded-xl transition-all border border-white/20"
              >
                <FaTrophy /> Check Rank
              </motion.button>
            </motion.div>
          </div>

          {/* Owl mascot */}
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

      {/* Today's Missions */}
      <motion.div variants={item}>
        <div className="flex items-center justify-between mb-5">
          <h2 className="text-2xl font-extrabold text-gray-800">
            Today's Missions 🎯
          </h2>
          <span className="text-sm font-bold text-gray-400">
            {missions.filter(m => m.current >= m.target).length}/{missions.length} completed
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
          {missions.map((mission, i) => {
            const percent = Math.round((mission.current / mission.target) * 100)
            const isComplete = mission.current >= mission.target

            return (
              <motion.div
                key={mission.id}
                variants={item}
                whileHover={{ y: -4, scale: 1.02 }}
                className={`bg-white rounded-2xl p-5 shadow-md border border-gray-100 transition-all ${isComplete ? 'ring-2 ring-green-300' : ''}`}
              >
                <div className="flex items-center justify-between mb-4">
                  <div className={`w-12 h-12 ${mission.bg} rounded-xl flex items-center justify-center`}>
                    <span className="text-2xl">{mission.emoji}</span>
                  </div>
                  {isComplete ? (
                    <FaCheckCircle className="text-green-500 text-xl" />
                  ) : (
                    <span className="text-xs font-bold text-gray-400 bg-gray-100 px-2 py-1 rounded-full">
                      {mission.reward}
                    </span>
                  )}
                </div>

                <h3 className="font-extrabold text-gray-800 mb-3">{mission.title}</h3>

                {/* Progress bar */}
                <div className="h-3 bg-gray-100 rounded-full overflow-hidden mb-2">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${percent}%` }}
                    transition={{ duration: 1, delay: 0.5 + i * 0.2 }}
                    className={`h-full bg-gradient-to-r ${mission.color} rounded-full`}
                  />
                </div>
                <div className="flex justify-between text-sm">
                  <span className="font-bold text-gray-500">
                    {mission.current}/{mission.target} done
                  </span>
                  <span className="font-bold text-gray-400">{percent}%</span>
                </div>
              </motion.div>
            )
          })}
        </div>
      </motion.div>

      {/* Recommended Lessons */}
      <motion.div variants={item}>
        <div className="flex items-center justify-between mb-5">
          <h2 className="text-2xl font-extrabold text-gray-800">
            Recommended for You 📖
          </h2>
          <Link to="/student/grades" className="text-sm font-bold text-primary-500 hover:text-primary-600">
            View All &rarr;
          </Link>
        </div>

        <div className="flex gap-4 overflow-x-auto pb-4 -mx-2 px-2 scrollbar-thin">
          {recommendedLessons.map((lesson, i) => (
            <motion.div
              key={lesson.id}
              variants={item}
              whileHover={{ y: -6, scale: 1.03 }}
              className="min-w-[200px] bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden cursor-pointer flex-shrink-0"
            >
              {/* Top gradient */}
              <div className={`h-24 bg-gradient-to-br ${lesson.color} flex items-center justify-center`}>
                <span className="text-4xl">{lesson.emoji}</span>
              </div>

              <div className="p-4">
                <h3 className="font-extrabold text-gray-800 text-sm mb-2">{lesson.title}</h3>
                <div className="flex items-center justify-between">
                  <span className={`text-xs font-bold px-2 py-0.5 rounded-full ${difficultyColors[lesson.difficulty]}`}>
                    {lesson.difficulty}
                  </span>
                  <span className="flex items-center gap-1 text-xs font-bold text-secondary-500">
                    <FaStar className="text-yellow-400" /> {lesson.xp} XP
                  </span>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Quick Stats Row */}
      <motion.div variants={item} className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2">🔥</div>
          <div className="text-2xl font-extrabold text-gray-800">7</div>
          <div className="text-sm font-bold text-gray-400">Day Streak</div>
        </div>
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2">📚</div>
          <div className="text-2xl font-extrabold text-gray-800">24</div>
          <div className="text-sm font-bold text-gray-400">Lessons Done</div>
        </div>
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2">🎮</div>
          <div className="text-2xl font-extrabold text-gray-800">12</div>
          <div className="text-sm font-bold text-gray-400">Games Won</div>
        </div>
        <div className="bg-white rounded-2xl p-5 shadow-md border border-gray-100 text-center">
          <div className="text-3xl mb-2">🏆</div>
          <div className="text-2xl font-extrabold text-gray-800">5</div>
          <div className="text-sm font-bold text-gray-400">Trophies</div>
        </div>
      </motion.div>
    </motion.div>
  )
}
