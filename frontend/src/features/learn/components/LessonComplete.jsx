import { motion } from 'framer-motion'
import { FaStar, FaTrophy, FaCoins, FaArrowLeft, FaArrowRight } from 'react-icons/fa'
import { HiSparkles } from 'react-icons/hi'

export default function LessonComplete({
  score,
  totalQuestions,
  xpEarned,
  starsEarned,
  coinsEarned,
  levelUp,
  onRetake,
  onNext,
  onBackToGrades,
}) {
  const perfect = starsEarned === 3

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
      className="bg-white rounded-3xl shadow-xl border border-gray-100 p-8 sm:p-12 text-center relative overflow-hidden"
    >
      {/* Background confetti for perfect score */}
      {perfect && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="absolute inset-0 pointer-events-none"
        >
          {['🎉', '🎊', '⭐', '✨', '🌟', '💫', '🎆', '🏆'].map((emoji, i) => (
            <motion.span
              key={i}
              initial={{
                opacity: 0,
                y: -20,
                x: `${10 + (i * 12)}%`,
                scale: 0,
              }}
              animate={{
                opacity: [0, 1, 1, 0],
                y: ['-10%', '110%'],
                scale: [0.5, 1.2, 1, 0.8],
                rotate: [0, 360],
              }}
              transition={{
                duration: 3 + (i * 0.3),
                delay: 0.5 + (i * 0.15),
                repeat: Infinity,
                repeatDelay: 2,
              }}
              className="absolute text-2xl sm:text-3xl"
              style={{ left: `${5 + (i * 12)}%` }}
            >
              {emoji}
            </motion.span>
          ))}
        </motion.div>
      )}

      <div className="relative z-10">
        {/* Celebration header for 3 stars */}
        {perfect && (
          <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="text-6xl mb-4"
          >
            🎉🏆🎊🌟🎉
          </motion.div>
        )}

        {/* Trophy */}
        <motion.div
          initial={{ scale: 0, rotate: -180 }}
          animate={{ scale: 1, rotate: 0 }}
          transition={{ delay: 0.3, type: 'spring', stiffness: 200 }}
        >
          <FaTrophy className={`text-7xl sm:text-8xl mx-auto mb-4 ${
            starsEarned >= 2 ? 'text-yellow-400' : starsEarned === 1 ? 'text-gray-400' : 'text-gray-300'
          }`} />
        </motion.div>

        {/* Title */}
        <motion.h2
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.5 }}
          className="text-3xl sm:text-4xl font-extrabold text-gray-800 mb-2"
        >
          {perfect
            ? 'PERFECT SCORE! 🌟'
            : starsEarned >= 2
            ? 'Great Job! 👏'
            : starsEarned === 1
            ? 'Good Try! 💪'
            : 'Keep Practicing! 📚'}
        </motion.h2>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.6 }}
          className="text-xl text-gray-500 font-bold mb-6"
        >
          You scored {score} out of {totalQuestions}
        </motion.p>

        {/* Stars - animated fill one by one */}
        <div className="flex justify-center gap-4 mb-8">
          {[1, 2, 3].map((star) => (
            <motion.div
              key={star}
              initial={{ opacity: 0, y: -30, rotate: -180, scale: 0 }}
              animate={{
                opacity: 1,
                y: 0,
                rotate: 0,
                scale: star <= starsEarned ? [0, 1.3, 1] : [0, 1],
              }}
              transition={{
                delay: 0.7 + star * 0.3,
                type: 'spring',
                stiffness: 200,
              }}
            >
              <FaStar className={`text-5xl sm:text-6xl ${
                star <= starsEarned ? 'text-yellow-400 drop-shadow-lg' : 'text-gray-200'
              }`} />
            </motion.div>
          ))}
        </div>

        {/* Stats Row */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 1.6 }}
          className="flex justify-center gap-4 sm:gap-6 mb-8 flex-wrap"
        >
          {/* XP */}
          <div className="bg-gradient-to-br from-purple-100 to-purple-50 border-2 border-purple-200 rounded-2xl px-5 py-3 text-center min-w-[100px]">
            <HiSparkles className="text-2xl text-purple-500 mx-auto mb-1" />
            <div className="text-2xl font-extrabold text-purple-600">{xpEarned}</div>
            <div className="text-sm font-bold text-purple-400">XP Earned</div>
          </div>

          {/* Coins */}
          <div className="bg-gradient-to-br from-yellow-100 to-amber-50 border-2 border-yellow-200 rounded-2xl px-5 py-3 text-center min-w-[100px]">
            <FaCoins className="text-2xl text-yellow-500 mx-auto mb-1" />
            <div className="text-2xl font-extrabold text-yellow-600">{coinsEarned}</div>
            <div className="text-sm font-bold text-yellow-400">Coins</div>
          </div>

          {/* Stars */}
          <div className="bg-gradient-to-br from-orange-100 to-orange-50 border-2 border-orange-200 rounded-2xl px-5 py-3 text-center min-w-[100px]">
            <FaStar className="text-2xl text-orange-500 mx-auto mb-1" />
            <div className="text-2xl font-extrabold text-orange-600">{starsEarned}</div>
            <div className="text-sm font-bold text-orange-400">Stars</div>
          </div>
        </motion.div>

        {/* Level Up Banner */}
        {levelUp && (
          <motion.div
            initial={{ opacity: 0, scale: 0.5 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 2, type: 'spring', stiffness: 150 }}
            className="bg-gradient-to-r from-pink-500 via-purple-500 to-blue-500 text-white rounded-2xl p-4 mb-8 shadow-lg"
          >
            <div className="text-3xl mb-1">🎊🆙🎊</div>
            <h3 className="text-2xl font-extrabold">Level Up!</h3>
            <p className="text-sm font-bold opacity-90">You reached a new level! Keep going!</p>
          </motion.div>
        )}

        {/* Buttons */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 2.2 }}
          className="flex flex-col sm:flex-row justify-center gap-3"
        >
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={onRetake}
            className="px-6 py-3 rounded-xl font-extrabold text-gray-600 bg-gray-100 hover:bg-gray-200 transition-all flex items-center justify-center gap-2"
          >
            <FaArrowLeft /> Retake Quiz
          </motion.button>

          {onNext ? (
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={onNext}
              className="px-8 py-3 rounded-xl font-extrabold text-white bg-gradient-to-r from-pink-500 via-purple-500 to-blue-500 shadow-lg hover:shadow-xl transition-all flex items-center justify-center gap-2"
            >
              Continue <FaArrowRight />
            </motion.button>
          ) : (
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={onBackToGrades}
              className="px-8 py-3 rounded-xl font-extrabold text-white bg-gradient-to-r from-pink-500 via-purple-500 to-blue-500 shadow-lg hover:shadow-xl transition-all flex items-center justify-center gap-2"
            >
              Back to Grades 🎓
            </motion.button>
          )}
        </motion.div>
      </div>
    </motion.div>
  )
}
