import { motion } from 'framer-motion'
import { FaLightbulb } from 'react-icons/fa'
import SvgVisual from './SvgVisual'

const CARD_COLORS = [
  'from-pink-100 to-pink-50 border-pink-200',
  'from-purple-100 to-purple-50 border-purple-200',
  'from-orange-100 to-orange-50 border-orange-200',
  'from-blue-100 to-blue-50 border-blue-200',
  'from-green-100 to-green-50 border-green-200',
  'from-yellow-100 to-yellow-50 border-yellow-200',
]

const STEP_COLORS = [
  'from-green-50 to-emerald-50 border-green-200',
  'from-blue-50 to-cyan-50 border-blue-200',
  'from-purple-50 to-violet-50 border-purple-200',
  'from-orange-50 to-amber-50 border-orange-200',
  'from-pink-50 to-rose-50 border-pink-200',
]

const containerVariants = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.12 },
  },
}

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function LearnTab({ content, onComplete }) {
  if (!content) return null

  const { explanation, examples, steps, fun_fact } = content

  return (
    <motion.div
      variants={containerVariants}
      initial="hidden"
      animate="show"
      className="space-y-6"
    >
      {/* Explanation Card */}
      {explanation && (
        <motion.div
          variants={itemVariants}
          className="bg-white rounded-3xl shadow-md border border-gray-100 p-6 sm:p-8"
        >
          <h2 className="text-2xl font-extrabold text-gray-800 mb-4 flex items-center gap-2">
            <FaLightbulb className="text-yellow-400" /> What are we learning?
          </h2>
          <div className="text-lg text-gray-600 leading-relaxed font-medium space-y-3">
            {explanation.split('\n').filter(Boolean).map((paragraph, i) => (
              <p key={i}>{paragraph}</p>
            ))}
          </div>
        </motion.div>
      )}

      {/* Visual Examples */}
      {examples && examples.length > 0 && (
        <motion.div
          variants={itemVariants}
          className="bg-white rounded-3xl shadow-md border border-gray-100 p-6 sm:p-8"
        >
          <h2 className="text-2xl font-extrabold text-gray-800 mb-4">
            See It In Action! 👀
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {examples.map((example, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, scale: 0.85 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.15 * i, type: 'spring', stiffness: 200 }}
                className={`bg-gradient-to-br ${CARD_COLORS[i % CARD_COLORS.length]} rounded-2xl p-5 border-2 text-center`}
              >
                <div className="text-3xl sm:text-4xl mb-3 tracking-wider flex justify-center">
                  {(example.emoji || example.visual || '🔢').includes('<svg')
                    ? <SvgVisual content={example.emoji || example.visual} />
                    : (example.emoji || example.visual || '🔢')
                  }
                </div>
                <div className="font-bold text-gray-700 text-lg">
                  {example.text.split('\n').map((line, j) => (
                    <p key={j}>{line}</p>
                  ))}
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      )}

      {/* Steps - Vertical Timeline */}
      {steps && steps.length > 0 && (
        <motion.div
          variants={itemVariants}
          className="bg-white rounded-3xl shadow-md border border-gray-100 p-6 sm:p-8"
        >
          <h2 className="text-2xl font-extrabold text-gray-800 mb-6">
            Step by Step 🪜
          </h2>
          <div className="relative">
            {/* Timeline line */}
            <div className="absolute left-6 top-0 bottom-0 w-1 bg-gradient-to-b from-pink-300 via-purple-300 to-blue-300 rounded-full" />

            <div className="space-y-4">
              {steps.map((step, i) => (
                <motion.div
                  key={i}
                  initial={{ opacity: 0, x: -30 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: 0.2 * i, type: 'spring', stiffness: 150 }}
                  className={`relative flex items-start gap-4 p-4 ml-2 rounded-xl bg-gradient-to-r ${STEP_COLORS[i % STEP_COLORS.length]} border`}
                >
                  {/* Timeline dot */}
                  <div className="absolute -left-4 top-5 w-5 h-5 rounded-full bg-white border-4 border-purple-400 z-10" />

                  <span className="text-2xl font-extrabold text-purple-400 min-w-[2rem] text-center">
                    {i + 1}
                  </span>
                  <p className="text-gray-700 font-bold text-base pt-1">
                    {typeof step === 'string' ? step.replace(/^\d+\.\s*/, '') : step}
                  </p>
                </motion.div>
              ))}
            </div>
          </div>
        </motion.div>
      )}

      {/* Fun Fact */}
      {fun_fact && (
        <motion.div
          variants={itemVariants}
          initial={{ opacity: 0, y: 15 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-gradient-to-r from-yellow-50 to-amber-50 rounded-3xl border-2 border-yellow-200 p-6 text-center"
        >
          <h3 className="text-xl font-extrabold text-yellow-700 mb-2">
            💡 Fun Fact! 🤓
          </h3>
          <p className="text-yellow-800 font-medium text-lg">{fun_fact}</p>
        </motion.div>
      )}

      {/* CTA Button */}
      <motion.div
        variants={itemVariants}
        className="text-center pb-4"
      >
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={onComplete}
          className="px-8 py-4 rounded-2xl font-extrabold text-lg text-white bg-gradient-to-r from-pink-500 via-purple-500 to-blue-500 shadow-lg hover:shadow-xl transition-all"
        >
          I Understand! Let's Practice! 🚀
        </motion.button>
      </motion.div>
    </motion.div>
  )
}
