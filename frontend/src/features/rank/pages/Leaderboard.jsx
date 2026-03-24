import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { FaTrophy, FaStar } from 'react-icons/fa'
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
    return <img src={avatarUrl} alt={name} className={`${size} rounded-full object-cover`} />
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
      flex items-center justify-center text-white font-extrabold shadow-lg`}>
      {initials}
    </div>
  )
}

/* ── Celebratory star that floats around the podium ── */
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
      transition={{
        delay,
        duration: 3,
        repeat: Infinity,
        repeatDelay: 1,
        ease: 'easeInOut',
      }}
    >
      ⭐
    </motion.span>
  )
}

/* ── Top-3 card (shown above the podium block) ── */
function TopCard({ entry, place }) {
  const crown = place === 1 ? '👑' : place === 2 ? '🥈' : '🥉'
  const cardBorder = place === 1
    ? 'border-yellow-300 shadow-yellow-200'
    : place === 2
    ? 'border-gray-300 shadow-gray-200'
    : 'border-orange-300 shadow-orange-200'
  const avatarSize = place === 1 ? 'w-20 h-20 text-2xl' : 'w-16 h-16 text-xl'
  const scoreSize = place === 1 ? 'text-2xl' : 'text-lg'
  const scoreBg = place === 1
    ? 'bg-yellow-400 text-white'
    : place === 2
    ? 'bg-gray-200 text-gray-700'
    : 'bg-orange-200 text-orange-700'

  return (
    <motion.div
      variants={item}
      className={`flex flex-col items-center ${
        place === 1 ? 'order-2 -mt-4' : place === 2 ? 'order-1 mt-4' : 'order-3 mt-4'
      }`}
    >
      <div className={`bg-white rounded-2xl border-2 ${cardBorder} shadow-lg p-4 flex flex-col items-center relative w-32`}>
        <span className="absolute -top-4 text-3xl">{crown}</span>
        <div className="mt-2 mb-2">
          <Avatar name={entry.name} avatarUrl={entry.avatar_url} size={avatarSize} />
        </div>
        <p className="font-extrabold text-gray-800 text-sm text-center truncate w-full">
          {entry.name}
        </p>
        <div className={`${scoreBg} rounded-full px-4 py-1 mt-2 font-extrabold ${scoreSize}`}>
          {entry.ranking_score}
        </div>
      </div>
    </motion.div>
  )
}

/* ── Podium blocks (1, 2, 3) ── */
function Podium() {
  const blocks = [
    { place: 2, height: 'h-20', gradient: 'from-gray-300 to-slate-400', order: 'order-1' },
    { place: 1, height: 'h-28', gradient: 'from-yellow-300 to-amber-400', order: 'order-2' },
    { place: 3, height: 'h-16', gradient: 'from-orange-300 to-amber-400', order: 'order-3' },
  ]
  return (
    <div className="flex items-end justify-center gap-2 mt-3">
      {blocks.map((b) => (
        <motion.div
          key={b.place}
          initial={{ height: 0 }}
          animate={{ height: 'auto' }}
          transition={{ delay: 0.4, duration: 0.5, ease: 'easeOut' }}
          className={`${b.order} w-32`}
        >
          <div className={`${b.height} bg-gradient-to-t ${b.gradient} rounded-t-2xl
            flex items-center justify-center shadow-md`}>
            <span className="text-white font-extrabold text-3xl drop-shadow">{b.place}</span>
          </div>
        </motion.div>
      ))}
    </div>
  )
}

/* ── Top 10 row (no avatar) ── */
function RankRow({ entry }) {
  const stripeColor = entry.rank === 1
    ? 'border-l-yellow-400'
    : entry.rank === 2
    ? 'border-l-gray-400'
    : entry.rank === 3
    ? 'border-l-orange-400'
    : 'border-l-purple-300'

  return (
    <motion.div
      variants={item}
      className={`flex items-center gap-4 px-5 py-3 rounded-xl border-l-4 ${stripeColor} transition-all ${
        entry.is_current_user
          ? 'bg-gradient-to-r from-purple-50 to-blue-50 border border-purple-200 shadow-md'
          : 'bg-white border border-gray-100 shadow-sm hover:shadow-md'
      }`}
    >
      {/* Rank */}
      <div className="w-8 text-center">
        {entry.rank <= 3 ? (
          <span className="text-lg">{entry.rank === 1 ? '🥇' : entry.rank === 2 ? '🥈' : '🥉'}</span>
        ) : (
          <span className="font-extrabold text-gray-400 text-lg">{entry.rank}</span>
        )}
      </div>

      {/* Name + level */}
      <div className="flex-1 min-w-0">
        <p className="font-bold text-gray-800 truncate">
          {entry.name}
          {entry.is_current_user && (
            <span className="ml-2 text-xs bg-purple-100 text-purple-600 px-2 py-0.5 rounded-full font-bold">
              You
            </span>
          )}
        </p>
        <p className="text-xs text-gray-400">Level {entry.level}</p>
      </div>

      {/* Score */}
      <div className="flex items-center gap-1">
        <FaTrophy className="text-yellow-400 text-sm" />
        <span className="font-extrabold text-gray-700">{entry.ranking_score}</span>
      </div>

      {/* Stars */}
      <div className="flex items-center gap-1 min-w-[40px] justify-end">
        <span className="font-bold text-gray-500">{entry.stars}</span>
        <FaStar className="text-yellow-400 text-sm" />
      </div>
    </motion.div>
  )
}

/* ── Main Leaderboard ── */
export default function Leaderboard() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    api.get('/leaderboard')
      .then((res) => setData(res.data))
      .catch((err) => setError(err.response?.data?.detail || 'Failed to load leaderboard'))
      .finally(() => setLoading(false))
  }, [])

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

  const { leaderboard } = data
  const top3 = leaderboard.slice(0, 3)
  const top10 = leaderboard.slice(0, 10)

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-2xl mx-auto"
    >
      {/* ── Top Podium Section (works with 1, 2, or 3 students) ── */}
      {top3.length > 0 && (
        <motion.div variants={item} className="mb-8">
          <div className="bg-gradient-to-br from-pink-100 via-orange-50 to-yellow-100 rounded-3xl shadow-xl p-6 pb-0 overflow-hidden relative">
            {/* Celebratory stars */}
            <CelebStar delay={0}   left="5%"  top="10%" size="text-xl" />
            <CelebStar delay={0.5} left="90%" top="8%"  size="text-lg" />
            <CelebStar delay={1.0} left="12%" top="55%" size="text-base" />
            <CelebStar delay={1.5} left="85%" top="50%" size="text-xl" />
            <CelebStar delay={0.3} left="2%"  top="35%" size="text-sm" />
            <CelebStar delay={0.8} left="93%" top="30%" size="text-sm" />
            <CelebStar delay={1.2} left="48%" top="3%"  size="text-2xl" />
            <CelebStar delay={0.7} left="30%" top="5%"  size="text-base" />
            <CelebStar delay={1.8} left="70%" top="5%"  size="text-base" />

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

      {/* ── Top 10 Section ── */}
      {top10.length > 0 && (
        <motion.div variants={item}>
          {/* Section header */}
          <div className="bg-gradient-to-r from-pink-400 via-orange-400 to-yellow-400 rounded-2xl px-5 py-3 mb-4 flex items-center gap-2 shadow-md">
            <FaTrophy className="text-white text-lg" />
            <h2 className="text-white font-extrabold text-lg">Top 10</h2>
          </div>

          {/* Top 10 list */}
          <div className="space-y-2">
            {top10.map((entry) => (
              <RankRow key={entry.student_id} entry={entry} />
            ))}
          </div>
        </motion.div>
      )}

      {/* Empty state */}
      {leaderboard.length === 0 && (
        <motion.div variants={item} className="text-center py-16">
          <div className="text-6xl mb-4">📊</div>
          <h3 className="text-xl font-bold text-gray-600 mb-2">No students yet!</h3>
          <p className="text-gray-400">Complete some lessons to appear on the leaderboard.</p>
        </motion.div>
      )}
    </motion.div>
  )
}
