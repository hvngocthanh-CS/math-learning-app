import { useState, useEffect, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { FaTrophy, FaStar, FaFire, FaMedal } from 'react-icons/fa'
import api from '../../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

/* ── Avatar ── */
function Avatar({ name, avatarUrl, size = 'w-16 h-16 text-xl' }) {
  if (avatarUrl) {
    return <img src={avatarUrl} alt={name} className={`${size} rounded-full object-cover border-2 border-white shadow-md`} />
  }
  const initials = name.split(' ').map((w) => w[0]).join('').slice(0, 2).toUpperCase()
  const colors = [
    'from-pink-400 to-rose-500',
    'from-blue-400 to-cyan-500',
    'from-green-400 to-emerald-500',
    'from-purple-400 to-violet-500',
    'from-orange-400 to-amber-500',
  ]
  return (
    <div className={`${size} rounded-full bg-gradient-to-br ${colors[name.length % 5]}
      flex items-center justify-center text-white font-extrabold shadow-lg border-2 border-white`}>
      {initials}
    </div>
  )
}

/* ── Celebratory star ── */
function CelebStar({ delay, left, top, size = 'text-lg' }) {
  return (
    <motion.span
      className={`absolute ${size} select-none pointer-events-none`}
      style={{ left, top }}
      initial={{ opacity: 0, scale: 0 }}
      animate={{
        opacity: [0, 1, 1, 0],
        scale: [0, 1.2, 1, 0.5],
        y: [0, -8, 0, 8],
        rotate: [0, 15, -15, 0],
      }}
      transition={{ delay, duration: 3, repeat: Infinity, repeatDelay: 1, ease: 'easeInOut' }}
    >
      ⭐
    </motion.span>
  )
}

/* ── Current User Rank Card ── */
function CurrentUserCard({ entry, totalStudents }) {
  if (!entry) return null
  return (
    <motion.div variants={item} className="mb-6">
      <div className="bg-gradient-to-r from-emerald-400 via-green-400 to-teal-400 rounded-2xl p-4 shadow-lg text-white">
        <div className="flex items-center gap-4">
          {/* Rank badge */}
          <div className="bg-white/20 backdrop-blur-sm rounded-xl px-3 py-2 text-center min-w-[60px]">
            <div className="text-2xl font-extrabold">#{entry.rank}</div>
            <div className="text-[10px] opacity-80">/ {totalStudents}</div>
          </div>

          {/* Avatar + info */}
          <div className="flex items-center gap-3 flex-1 min-w-0">
            <Avatar name={entry.name} avatarUrl={entry.avatar_url} size="w-12 h-12 text-base" />
            <div className="min-w-0">
              <p className="font-bold text-sm truncate">{entry.name}</p>
              <p className="text-xs opacity-80">Level {entry.level}</p>
            </div>
          </div>

          {/* Stats */}
          <div className="flex items-center gap-4 text-sm">
            <div className="text-center">
              <div className="font-extrabold text-lg">{entry.ranking_score}</div>
              <div className="text-[10px] opacity-80 flex items-center gap-0.5 justify-center">
                <FaTrophy className="text-yellow-200" /> Score
              </div>
            </div>
            <div className="text-center">
              <div className="font-extrabold text-lg">{entry.stars}</div>
              <div className="text-[10px] opacity-80 flex items-center gap-0.5 justify-center">
                <FaStar className="text-yellow-200" /> Stars
              </div>
            </div>
            <div className="text-center">
              <div className="font-extrabold text-lg">+{entry.streak}</div>
              <div className="text-[10px] opacity-80 flex items-center gap-0.5 justify-center">
                <FaFire className="text-orange-200" /> Streak
              </div>
            </div>
          </div>
        </div>
      </div>
    </motion.div>
  )
}

/* ── Filter Tabs ── */
function FilterTabs({ period, setPeriod, gradeId, setGradeId, grades }) {
  const periodOptions = [
    { value: 'week', label: 'This Week' },
    { value: 'month', label: 'This Month' },
    { value: 'all', label: 'All Time' },
  ]

  return (
    <motion.div variants={item} className="mb-6">
      {/* Period tabs */}
      <div className="flex items-center gap-2 bg-gray-100 rounded-xl p-1 mb-3">
        {periodOptions.map((opt) => (
          <button
            key={opt.value}
            onClick={() => setPeriod(opt.value)}
            className={`flex-1 py-2 px-3 rounded-lg text-sm font-bold transition-all ${
              period === opt.value
                ? 'bg-white text-purple-600 shadow-md'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            {opt.label}
          </button>
        ))}
      </div>

      {/* Grade filter */}
      {grades.length > 0 && (
        <div className="flex items-center gap-2 overflow-x-auto pb-1">
          <button
            onClick={() => setGradeId(null)}
            className={`px-3 py-1.5 rounded-full text-xs font-bold whitespace-nowrap transition-all ${
              gradeId === null
                ? 'bg-purple-500 text-white shadow-md'
                : 'bg-gray-100 text-gray-500 hover:bg-gray-200'
            }`}
          >
            All Grades
          </button>
          {grades.map((g) => (
            <button
              key={g.id}
              onClick={() => setGradeId(g.id)}
              className={`px-3 py-1.5 rounded-full text-xs font-bold whitespace-nowrap transition-all ${
                gradeId === g.id
                  ? 'bg-purple-500 text-white shadow-md'
                  : 'bg-gray-100 text-gray-500 hover:bg-gray-200'
              }`}
            >
              {g.name}
            </button>
          ))}
        </div>
      )}
    </motion.div>
  )
}

/* ── Top-3 Podium Card ── */
function TopCard({ entry, place }) {
  const crown = place === 1 ? '👑' : place === 2 ? '🥈' : '🥉'
  const cardStyles = {
    1: { border: 'border-yellow-300 shadow-yellow-200/50', scoreBg: 'bg-yellow-400 text-white', avatar: 'w-20 h-20 text-2xl', score: 'text-xl' },
    2: { border: 'border-gray-300 shadow-gray-200/50', scoreBg: 'bg-gray-200 text-gray-700', avatar: 'w-16 h-16 text-xl', score: 'text-lg' },
    3: { border: 'border-orange-300 shadow-orange-200/50', scoreBg: 'bg-orange-200 text-orange-700', avatar: 'w-16 h-16 text-xl', score: 'text-lg' },
  }
  const s = cardStyles[place]

  return (
    <motion.div
      variants={item}
      className={`flex flex-col items-center ${
        place === 1 ? 'order-2 -mt-4' : place === 2 ? 'order-1 mt-4' : 'order-3 mt-4'
      }`}
    >
      <div className={`bg-white rounded-2xl border-2 ${s.border} shadow-lg p-4 flex flex-col items-center relative w-32`}>
        <span className="absolute -top-4 text-3xl">{crown}</span>
        <div className="mt-2 mb-1">
          <Avatar name={entry.name} avatarUrl={entry.avatar_url} size={s.avatar} />
        </div>
        <p className="font-extrabold text-gray-800 text-xs text-center truncate w-full">
          {entry.name}
        </p>
        {entry.is_current_user && (
          <span className="text-[10px] bg-purple-100 text-purple-600 px-2 py-0.5 rounded-full font-bold">
            You
          </span>
        )}
        <div className={`${s.scoreBg} rounded-full px-4 py-1 mt-1.5 font-extrabold ${s.score}`}>
          {entry.ranking_score}
        </div>
      </div>
    </motion.div>
  )
}

/* ── Top 10 Row ── */
function RankRow({ entry }) {
  const stripeColor = entry.rank === 1
    ? 'border-l-yellow-400'
    : entry.rank === 2
    ? 'border-l-gray-400'
    : entry.rank === 3
    ? 'border-l-orange-400'
    : 'border-l-purple-300'

  const rankBadge = (rank) => {
    if (rank === 1) return '🥇'
    if (rank === 2) return '🥈'
    if (rank === 3) return '🥉'
    return <span className="font-extrabold text-gray-400 text-lg">{rank}</span>
  }

  return (
    <motion.div
      variants={item}
      className={`flex items-center gap-3 px-4 py-3 rounded-xl border-l-4 ${stripeColor} transition-all ${
        entry.is_current_user
          ? 'bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 shadow-md'
          : 'bg-white border border-gray-100 shadow-sm hover:shadow-md'
      }`}
    >
      {/* Rank */}
      <div className="w-8 text-center text-lg">
        {rankBadge(entry.rank)}
      </div>

      {/* Avatar */}
      <Avatar name={entry.name} avatarUrl={entry.avatar_url} size="w-10 h-10 text-sm" />

      {/* Name + level */}
      <div className="flex-1 min-w-0">
        <p className="font-bold text-gray-800 text-sm truncate">
          {entry.name}
          {entry.is_current_user && (
            <span className="ml-2 text-[10px] bg-purple-100 text-purple-600 px-2 py-0.5 rounded-full font-bold">
              You
            </span>
          )}
        </p>
        <p className="text-xs text-gray-400">Level {entry.level}</p>
      </div>

      {/* Score */}
      <div className="flex items-center gap-1">
        <FaTrophy className="text-yellow-400 text-xs" />
        <span className="font-extrabold text-gray-700 text-sm">{entry.ranking_score}</span>
      </div>

      {/* Stars */}
      <div className="flex items-center gap-1 min-w-[36px] justify-end">
        <span className="font-bold text-gray-500 text-sm">{entry.stars}</span>
        <FaStar className="text-yellow-400 text-xs" />
      </div>
    </motion.div>
  )
}

/* ── Main Leaderboard ── */
export default function Leaderboard() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [period, setPeriod] = useState('week')
  const [gradeId, setGradeId] = useState(null)
  const [grades, setGrades] = useState([])

  // Fetch grade options once
  useEffect(() => {
    api.get('/leaderboard/filters')
      .then((res) => setGrades(res.data.grades))
      .catch(() => {})
  }, [])

  // Fetch leaderboard data when filters change
  const fetchLeaderboard = useCallback(() => {
    setLoading(true)
    setError(null)
    const params = { period }
    if (gradeId) params.grade_id = gradeId
    api.get('/leaderboard', { params })
      .then((res) => setData(res.data))
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load leaderboard'))
      .finally(() => setLoading(false))
  }, [period, gradeId])

  useEffect(() => {
    fetchLeaderboard()
  }, [fetchLeaderboard])

  if (loading) {
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="text-5xl mb-4 animate-bounce">🏆</div>
          <p className="text-gray-400 font-semibold">Loading leaderboard...</p>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="flex items-center justify-center py-20">
        <div className="text-center">
          <div className="text-5xl mb-4">😕</div>
          <p className="text-gray-500 font-semibold">{error}</p>
        </div>
      </div>
    )
  }

  const { leaderboard, current_user_rank, total_students } = data
  const top3 = leaderboard.slice(0, 3)
  const restList = leaderboard.slice(3, 10)

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-2xl mx-auto"
    >
      {/* ── Header ── */}
      <motion.div variants={item} className="text-center mb-6">
        <div className="text-5xl mb-2">🏆</div>
        <h1 className="text-2xl font-extrabold text-gray-800">Leaderboard</h1>
        <p className="text-sm text-gray-400">See how you rank against other math champions!</p>
      </motion.div>

      {/* ── Current User Rank Card ── */}
      <CurrentUserCard entry={current_user_rank} totalStudents={total_students} />

      {/* ── Filter Tabs ── */}
      <FilterTabs
        period={period}
        setPeriod={setPeriod}
        gradeId={gradeId}
        setGradeId={setGradeId}
        grades={grades}
      />

      {/* ── Top 3 Podium ── */}
      <AnimatePresence mode="wait">
        {top3.length > 0 && (
          <motion.div
            key={`podium-${period}-${gradeId}`}
            variants={item}
            initial="hidden"
            animate="show"
            exit="hidden"
            className="mb-8"
          >
            <div className="bg-gradient-to-br from-pink-100 via-orange-50 to-yellow-100 rounded-3xl shadow-xl p-6 pb-0 overflow-hidden relative">
              {/* Celebratory stars */}
              <CelebStar delay={0}   left="5%"  top="10%" size="text-xl" />
              <CelebStar delay={0.5} left="90%" top="8%"  size="text-lg" />
              <CelebStar delay={1.0} left="12%" top="55%" size="text-base" />
              <CelebStar delay={1.5} left="85%" top="50%" size="text-xl" />
              <CelebStar delay={0.3} left="2%"  top="35%" size="text-sm" />
              <CelebStar delay={0.8} left="93%" top="30%" size="text-sm" />
              <CelebStar delay={1.2} left="48%" top="3%"  size="text-2xl" />

              {/* Top cards */}
              <div className="flex items-end justify-center gap-3 relative z-10">
                {top3.length >= 2 && <TopCard entry={top3[1]} place={2} />}
                <TopCard entry={top3[0]} place={1} />
                {top3.length >= 3 && <TopCard entry={top3[2]} place={3} />}
              </div>

              {/* Podium blocks */}
              <div className="flex items-end justify-center gap-2 mt-3">
                {top3.length >= 2 && (
                  <motion.div initial={{ height: 0 }} animate={{ height: 'auto' }} transition={{ delay: 0.4, duration: 0.5 }} className="order-1 w-32">
                    <div className="h-20 bg-gradient-to-t from-gray-300 to-slate-400 rounded-t-2xl flex items-center justify-center shadow-md">
                      <span className="text-white font-extrabold text-3xl drop-shadow">2</span>
                    </div>
                  </motion.div>
                )}
                <motion.div initial={{ height: 0 }} animate={{ height: 'auto' }} transition={{ delay: 0.4, duration: 0.5 }} className="order-2 w-32">
                  <div className="h-28 bg-gradient-to-t from-yellow-300 to-amber-400 rounded-t-2xl flex items-center justify-center shadow-md">
                    <span className="text-white font-extrabold text-3xl drop-shadow">1</span>
                  </div>
                </motion.div>
                {top3.length >= 3 && (
                  <motion.div initial={{ height: 0 }} animate={{ height: 'auto' }} transition={{ delay: 0.4, duration: 0.5 }} className="order-3 w-32">
                    <div className="h-16 bg-gradient-to-t from-orange-300 to-amber-400 rounded-t-2xl flex items-center justify-center shadow-md">
                      <span className="text-white font-extrabold text-3xl drop-shadow">3</span>
                    </div>
                  </motion.div>
                )}
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* ── Top 10 List (ranks 4-13) ── */}
      {restList.length > 0 && (
        <motion.div variants={item}>
          <div className="bg-gradient-to-r from-pink-400 via-orange-400 to-yellow-400 rounded-2xl px-5 py-3 mb-4 flex items-center gap-2 shadow-md">
            <FaMedal className="text-white text-lg" />
            <h2 className="text-white font-extrabold text-lg">Top Rankings</h2>
          </div>

          <div className="space-y-2">
            {restList.map((entry) => (
              <RankRow key={entry.student_id} entry={entry} />
            ))}
          </div>
        </motion.div>
      )}

      {/* ── Current user outside top list ── */}
      {current_user_rank && current_user_rank.rank > 10 && (
        <motion.div variants={item} className="mt-4">
          <div className="text-center text-xs text-gray-400 my-2">• • •</div>
          <RankRow entry={current_user_rank} />
        </motion.div>
      )}

      {/* ── Empty state ── */}
      {leaderboard.length === 0 && (
        <motion.div variants={item} className="text-center py-16">
          <div className="text-6xl mb-4">📊</div>
          <h3 className="text-xl font-bold text-gray-600 mb-2">No rankings yet!</h3>
          <p className="text-gray-400">Complete some lessons to appear on the leaderboard.</p>
        </motion.div>
      )}
    </motion.div>
  )
}
