import { motion } from 'framer-motion'
import { Link } from 'react-router-dom'
import { FaGamepad, FaBolt, FaPlay } from 'react-icons/fa'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.15 } },
}
const item = {
  hidden: { opacity: 0, y: 30 },
  show: { opacity: 1, y: 0 },
}

const GAMES = [
  {
    id: 'math-pop',
    title: 'Math Pop',
    subtitle: 'Pop the right answer!',
    description: 'Colorful bubbles float up with numbers. Read the question and tap the correct bubble before it floats away! The faster you pop, the higher your score.',
    emoji: '🫧',
    gradient: 'from-pink-400 via-purple-400 to-blue-400',
    shadow: 'shadow-purple-200',
    bgPattern: '🫧 🔢 ✨ 🎯',
  },
  {
    id: 'math-memory',
    title: 'Math Memory',
    subtitle: 'Match the pairs!',
    description: 'Flip cards to find matching pairs — each math problem has a matching answer card. Find all pairs to win! Train your memory while practicing math.',
    emoji: '🃏',
    gradient: 'from-orange-400 via-amber-400 to-yellow-400',
    shadow: 'shadow-orange-200',
    bgPattern: '🃏 🧠 ✨ 🎴',
  },
]

export default function GameSelection() {
  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-5xl mx-auto"
    >
      {/* Header */}
      <motion.div variants={item} className="text-center mb-10">
        <div className="inline-flex items-center gap-3 bg-white/80 backdrop-blur-sm rounded-2xl px-6 py-3 shadow-md mb-4">
          <FaGamepad className="text-purple-500 text-2xl" />
          <h1 className="text-3xl font-extrabold text-gray-800">Play Games</h1>
        </div>
        <p className="text-gray-500 text-lg">Have fun while practicing math!</p>
      </motion.div>

      {/* Game Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {GAMES.map((game) => (
          <motion.div key={game.id} variants={item}>
            <Link to={`/student/play/${game.id}`}>
              <motion.div
                whileHover={{ y: -8, scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                className={`rounded-3xl overflow-hidden shadow-xl ${game.shadow} border border-white/50 bg-white cursor-pointer`}
              >
                {/* Gradient Header */}
                <div className={`bg-gradient-to-br ${game.gradient} p-8 relative overflow-hidden`}>
                  {/* Floating pattern */}
                  <div className="absolute inset-0 opacity-15 text-4xl flex items-center justify-center gap-4 font-bold select-none pointer-events-none">
                    {game.bgPattern}
                  </div>
                  <div className="relative text-center">
                    <span className="text-7xl block mb-3">{game.emoji}</span>
                    <h2 className="text-3xl font-extrabold text-white drop-shadow-md">
                      {game.title}
                    </h2>
                    <p className="text-white/90 text-lg mt-1 font-semibold">
                      {game.subtitle}
                    </p>
                  </div>
                </div>

                {/* Description */}
                <div className="p-6">
                  <p className="text-gray-600 leading-relaxed mb-5">
                    {game.description}
                  </p>
                  <div className="flex items-center justify-center">
                    <span className="inline-flex items-center gap-2 bg-gradient-to-r from-purple-500 to-blue-500 text-white font-bold px-6 py-3 rounded-full shadow-md text-lg">
                      <FaPlay className="text-sm" />
                      Play Now
                    </span>
                  </div>
                </div>
              </motion.div>
            </Link>
          </motion.div>
        ))}
      </div>
    </motion.div>
  )
}
