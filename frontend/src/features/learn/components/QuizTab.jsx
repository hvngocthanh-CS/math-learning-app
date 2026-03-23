import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { FaCheckCircle, FaTimesCircle } from 'react-icons/fa'

const OPTION_LABELS = ['A', 'B', 'C', 'D']

const OPTION_COLORS = [
  'hover:border-pink-400 hover:bg-pink-50',
  'hover:border-purple-400 hover:bg-purple-50',
  'hover:border-blue-400 hover:bg-blue-50',
  'hover:border-orange-400 hover:bg-orange-50',
]

export default function QuizTab({ problems, onComplete }) {
  const [current, setCurrent] = useState(0)
  const [selected, setSelected] = useState(null)
  const [result, setResult] = useState(null) // 'correct' | 'wrong' | null
  const [score, setScore] = useState(0)
  const timerRef = useRef(null)

  const total = problems?.length || 5

  // Cleanup timer
  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
    }
  }, [])

  if (!problems || problems.length === 0) return null

  const problem = problems[current]
  const options = problem.options || []
  const isComparisonPick = problem.subtype === 'comparison_pick'
  const isComparisonSign = problem.subtype === 'comparison'
  const isComparisonVisual = problem.subtype === 'comparison_visual'
  const isShapeIdentify = problem.subtype === 'shape_identify'
  const isPatternPick = problem.subtype === 'pattern_pick'

  const selectAnswer = (option) => {
    if (result) return
    setSelected(option)

    const correctVal = problem.answer
    // Support both numeric and string answers
    const isCorrect = typeof correctVal === 'string'
      ? String(option).toLowerCase() === correctVal.toLowerCase()
      : Math.abs(parseFloat(option) - parseFloat(correctVal)) < 0.01

    if (isCorrect) {
      setResult('correct')
      const newScore = score + 1
      setScore(newScore)

      // Auto-advance after 1.5s
      timerRef.current = setTimeout(() => {
        if (current < total - 1) {
          setCurrent(prev => prev + 1)
          setSelected(null)
          setResult(null)
        } else {
          onComplete(newScore)
        }
      }, 1500)
    } else {
      setResult('wrong')

      // Auto-advance after 1.5s
      timerRef.current = setTimeout(() => {
        if (current < total - 1) {
          setCurrent(prev => prev + 1)
          setSelected(null)
          setResult(null)
        } else {
          onComplete(score)
        }
      }, 1500)
    }
  }

  const progressPercent = ((current) / total) * 100

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="space-y-6"
    >
      {/* Progress Bar */}
      <div className="bg-white rounded-2xl shadow-md border border-gray-100 p-4">
        <div className="flex items-center justify-between mb-2">
          <span className="text-lg font-extrabold text-gray-700">
            🎯 Question {current + 1} of {total}
          </span>
          <span className="text-sm font-bold text-purple-500">
            {score} correct so far
          </span>
        </div>
        <div className="h-3 bg-gray-100 rounded-full overflow-hidden">
          <motion.div
            initial={{ width: 0 }}
            animate={{ width: `${progressPercent}%` }}
            transition={{ duration: 0.4 }}
            className="h-full bg-gradient-to-r from-pink-400 via-purple-400 to-blue-400 rounded-full"
          />
        </div>
      </div>

      {/* Question Card */}
      <AnimatePresence mode="wait">
        <motion.div
          key={current}
          initial={{ opacity: 0, x: 60 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -60 }}
          transition={{ type: 'spring', stiffness: 200, damping: 20 }}
          className="bg-white rounded-3xl shadow-lg border border-gray-100 p-6 sm:p-8"
        >
          {/* Question */}
          {isShapeIdentify ? (
            <div className="text-center mb-8">
              <p className="text-xl sm:text-2xl font-bold text-gray-700 mb-4">
                {problem.question}
              </p>
              <motion.div
                initial={{ scale: 0.5, rotate: -10 }}
                animate={{ scale: 1, rotate: 0 }}
                transition={{ type: 'spring', stiffness: 200 }}
                className="inline-block"
              >
                <span className="text-[8rem] sm:text-[10rem] leading-none drop-shadow-lg">
                  {problem.shape_emoji}
                </span>
              </motion.div>
            </div>
          ) : isComparisonVisual ? (
            <div className="text-center mb-8">
              <p className="text-xl sm:text-2xl font-bold text-gray-700 mb-6">
                {problem.question}
              </p>
              {(() => {
                const parts = problem.question_text.split('  ?  ')
                return (
                  <div className="flex items-center justify-center gap-4 sm:gap-6">
                    <div className="flex-1 bg-gradient-to-br from-pink-50 to-pink-100 border-2 border-pink-200 rounded-2xl p-4 sm:p-5 text-center">
                      <div className="text-3xl sm:text-4xl leading-relaxed break-words">
                        {parts[0]}
                      </div>
                    </div>
                    <div className="text-4xl sm:text-5xl font-extrabold text-purple-400">?</div>
                    <div className="flex-1 bg-gradient-to-br from-blue-50 to-blue-100 border-2 border-blue-200 rounded-2xl p-4 sm:p-5 text-center">
                      <div className="text-3xl sm:text-4xl leading-relaxed break-words">
                        {parts[1]}
                      </div>
                    </div>
                  </div>
                )
              })()}
            </div>
          ) : (
            <div className="text-center mb-8">
              <div className="text-5xl mb-4">🎯</div>
              <p className="text-xl sm:text-2xl font-bold text-gray-700 mb-2">
                {problem.question}
              </p>
              <p className="text-3xl sm:text-4xl font-extrabold text-gray-800 tracking-wider">
                {problem.question_text}
              </p>
            </div>
          )}

          {/* Options */}
          {isPatternPick ? (
            <div className="flex justify-center gap-6 mb-6">
              {options.map((emoji, i) => {
                const isCorrectOption = emoji === problem.answer
                const isSelected = selected !== null && selected === emoji
                const idleColors = [
                  'border-pink-300 bg-pink-50 hover:border-pink-500 hover:bg-pink-100',
                  'border-blue-300 bg-blue-50 hover:border-blue-500 hover:bg-blue-100',
                ]
                return (
                  <motion.button
                    key={i}
                    whileHover={!result ? { scale: 1.15, y: -4 } : {}}
                    whileTap={!result ? { scale: 0.9 } : {}}
                    onClick={() => selectAnswer(emoji)}
                    disabled={!!result}
                    className={`w-28 h-28 sm:w-32 sm:h-32 rounded-3xl border-4 shadow-lg transition-all flex items-center justify-center ${
                      result && isCorrectOption
                        ? 'border-green-400 bg-green-50 shadow-green-200'
                        : result && isSelected && !isCorrectOption
                        ? 'border-red-400 bg-red-50 shadow-red-200'
                        : result
                        ? 'border-gray-200 bg-gray-50 opacity-40'
                        : `${idleColors[i]} cursor-pointer hover:shadow-xl`
                    }`}
                  >
                    <span className="text-5xl sm:text-6xl">{emoji}</span>
                  </motion.button>
                )
              })}
            </div>
          ) : isShapeIdentify ? (
            <div className="flex justify-center gap-5 mb-6">
              {options.map((shape, i) => {
                const isCorrectOption = String(shape).toLowerCase() === String(problem.answer).toLowerCase()
                const isSelected = selected !== null && String(selected).toLowerCase() === String(shape).toLowerCase()
                const shapeIcons = { circle: '⭕', square: '⬜', triangle: '📐', rectangle: '📋' }
                const shapeIcon = shapeIcons[shape.toLowerCase()] || '🔷'
                const idleColors = [
                  'from-pink-100 to-pink-50 border-pink-300 hover:border-pink-500',
                  'from-blue-100 to-blue-50 border-blue-300 hover:border-blue-500',
                  'from-amber-100 to-amber-50 border-amber-300 hover:border-amber-500',
                  'from-green-100 to-green-50 border-green-300 hover:border-green-500',
                ]
                return (
                  <motion.button
                    key={i}
                    whileHover={!result ? { scale: 1.1, y: -4 } : {}}
                    whileTap={!result ? { scale: 0.9 } : {}}
                    onClick={() => selectAnswer(shape)}
                    disabled={!!result}
                    className={`w-36 h-32 sm:w-40 sm:h-36 rounded-3xl flex flex-col items-center justify-center gap-2 border-4 shadow-lg transition-all ${
                      result && isCorrectOption
                        ? 'border-green-400 bg-gradient-to-br from-green-100 to-green-50 shadow-green-300'
                        : result && isSelected && !isCorrectOption
                        ? 'border-red-400 bg-gradient-to-br from-red-100 to-red-50 shadow-red-300'
                        : result
                        ? 'border-gray-200 bg-gray-50 opacity-40'
                        : `bg-gradient-to-br ${idleColors[i % idleColors.length]} hover:shadow-xl cursor-pointer`
                    }`}
                  >
                    <span className="text-4xl">{shapeIcon}</span>
                    <span className={`text-lg sm:text-xl font-extrabold capitalize ${
                      result && isCorrectOption ? 'text-green-600'
                        : result && isSelected && !isCorrectOption ? 'text-red-600'
                        : result ? 'text-gray-300'
                        : i === 0 ? 'text-pink-600' : 'text-blue-600'
                    }`}>
                      {shape}
                    </span>
                    {result && isCorrectOption && (
                      <motion.span initial={{ scale: 0 }} animate={{ scale: 1 }}>
                        <FaCheckCircle className="text-green-500 text-lg" />
                      </motion.span>
                    )}
                    {result && isSelected && !isCorrectOption && (
                      <motion.span initial={{ scale: 0 }} animate={{ scale: 1 }}>
                        <FaTimesCircle className="text-red-500 text-lg" />
                      </motion.span>
                    )}
                  </motion.button>
                )
              })}
            </div>
          ) : (isComparisonSign || isComparisonVisual) ? (
            <div className="flex justify-center gap-5 mb-6">
              {options.map((sign, i) => {
                const isCorrectOption = String(sign) === String(problem.answer)
                const isSelected = selected !== null && String(selected) === String(sign)
                const idleColors = [
                  'from-pink-100 to-pink-50 border-pink-300 hover:border-pink-500',
                  'from-blue-100 to-blue-50 border-blue-300 hover:border-blue-500',
                  'from-amber-100 to-amber-50 border-amber-300 hover:border-amber-500',
                ]
                return (
                  <motion.button
                    key={i}
                    whileHover={!result ? { scale: 1.1, y: -4 } : {}}
                    whileTap={!result ? { scale: 0.9 } : {}}
                    onClick={() => selectAnswer(sign)}
                    disabled={!!result}
                    className={`w-28 h-28 sm:w-32 sm:h-32 rounded-3xl flex flex-col items-center justify-center border-4 shadow-lg transition-all ${
                      result && isCorrectOption
                        ? 'border-green-400 bg-gradient-to-br from-green-100 to-green-50 shadow-green-300'
                        : result && isSelected && !isCorrectOption
                        ? 'border-red-400 bg-gradient-to-br from-red-100 to-red-50 shadow-red-300'
                        : result
                        ? 'border-gray-200 bg-gray-50 opacity-40'
                        : `bg-gradient-to-br ${idleColors[i]} hover:shadow-xl cursor-pointer`
                    }`}
                  >
                    <span className={`text-5xl sm:text-6xl font-extrabold ${
                      result && isCorrectOption
                        ? 'text-green-600'
                        : result && isSelected && !isCorrectOption
                        ? 'text-red-600'
                        : result
                        ? 'text-gray-300'
                        : i === 0 ? 'text-pink-600' : i === 1 ? 'text-blue-600' : 'text-amber-600'
                    }`}>
                      {sign}
                    </span>
                    {result && isCorrectOption && (
                      <motion.span initial={{ scale: 0 }} animate={{ scale: 1 }} className="mt-1">
                        <FaCheckCircle className="text-green-500 text-xl" />
                      </motion.span>
                    )}
                    {result && isSelected && !isCorrectOption && (
                      <motion.span initial={{ scale: 0 }} animate={{ scale: 1 }} className="mt-1">
                        <FaTimesCircle className="text-red-500 text-xl" />
                      </motion.span>
                    )}
                  </motion.button>
                )
              })}
            </div>
          ) : isComparisonPick ? (
            <div className="flex justify-center gap-8 mb-6">
              {options.map((option, i) => {
                const isCorrectOption = Math.abs(parseFloat(option) - parseFloat(problem.answer)) < 0.01
                const isSelected = selected !== null && Math.abs(parseFloat(selected) - parseFloat(option)) < 0.01
                const colors = [
                  'from-pink-100 to-pink-50 border-pink-300 hover:border-pink-500 hover:shadow-pink-200',
                  'from-blue-100 to-blue-50 border-blue-300 hover:border-blue-500 hover:shadow-blue-200',
                ]
                return (
                  <motion.button
                    key={i}
                    whileHover={!result ? { scale: 1.1, y: -4 } : {}}
                    whileTap={!result ? { scale: 0.95 } : {}}
                    onClick={() => selectAnswer(option)}
                    disabled={!!result}
                    className={`w-32 h-32 sm:w-36 sm:h-36 rounded-3xl flex flex-col items-center justify-center border-4 shadow-lg transition-all ${
                      result && isCorrectOption
                        ? 'border-green-400 bg-gradient-to-br from-green-100 to-green-50 shadow-green-300'
                        : result && isSelected && !isCorrectOption
                        ? 'border-red-400 bg-gradient-to-br from-red-100 to-red-50 shadow-red-300'
                        : result
                        ? 'border-gray-200 bg-gray-50 opacity-40'
                        : `bg-gradient-to-br ${colors[i]} hover:shadow-xl cursor-pointer`
                    }`}
                  >
                    <span className={`text-5xl sm:text-6xl font-extrabold ${
                      result && isCorrectOption
                        ? 'text-green-600'
                        : result && isSelected && !isCorrectOption
                        ? 'text-red-600'
                        : result
                        ? 'text-gray-300'
                        : i === 0 ? 'text-pink-600' : 'text-blue-600'
                    }`}>
                      {option}
                    </span>
                    {result && isCorrectOption && (
                      <motion.span
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        className="mt-1"
                      >
                        <FaCheckCircle className="text-green-500 text-xl" />
                      </motion.span>
                    )}
                    {result && isSelected && !isCorrectOption && (
                      <motion.span
                        initial={{ scale: 0 }}
                        animate={{ scale: 1 }}
                        className="mt-1"
                      >
                        <FaTimesCircle className="text-red-500 text-xl" />
                      </motion.span>
                    )}
                  </motion.button>
                )
              })}
            </div>
          ) : (
            <div className="grid grid-cols-2 gap-3 max-w-lg mx-auto mb-6">
              {options.map((option, i) => {
                const isStringAnswer = typeof problem.answer === 'string'
                const isCorrectOption = isStringAnswer
                  ? String(option).toLowerCase() === String(problem.answer).toLowerCase()
                  : Math.abs(parseFloat(option) - parseFloat(problem.answer)) < 0.01
                const isSelected = selected !== null && (isStringAnswer
                  ? String(selected).toLowerCase() === String(option).toLowerCase()
                  : Math.abs(parseFloat(selected) - parseFloat(option)) < 0.01)

                let bgClass = `bg-white border-2 border-gray-200 ${OPTION_COLORS[i % OPTION_COLORS.length]}`

                if (result) {
                  if (isCorrectOption) {
                    bgClass = 'bg-green-50 border-2 border-green-400'
                  } else if (isSelected && !isCorrectOption) {
                    bgClass = 'bg-red-50 border-2 border-red-400'
                  } else {
                    bgClass = 'bg-gray-50 border-2 border-gray-200 opacity-40'
                  }
                }

                return (
                  <motion.button
                    key={i}
                    whileHover={!result ? { scale: 1.05 } : {}}
                    whileTap={!result ? { scale: 0.95 } : {}}
                    onClick={() => selectAnswer(option)}
                    disabled={!!result}
                    className={`p-4 sm:p-5 rounded-2xl transition-all ${bgClass}`}
                  >
                    <div className="flex items-center gap-3">
                      <span className={`w-9 h-9 rounded-full flex items-center justify-center font-extrabold text-sm ${
                        result && isCorrectOption
                          ? 'bg-green-500 text-white'
                          : result && isSelected && !isCorrectOption
                          ? 'bg-red-500 text-white'
                          : 'bg-gray-100 text-gray-500'
                      }`}>
                        {result && isCorrectOption ? (
                          <FaCheckCircle className="text-lg" />
                        ) : result && isSelected && !isCorrectOption ? (
                          <FaTimesCircle className="text-lg" />
                        ) : (
                          OPTION_LABELS[i]
                        )}
                      </span>
                      <span className="text-xl sm:text-2xl font-extrabold text-gray-800 capitalize">
                        {typeof option === 'number' && option % 1 !== 0
                          ? option.toFixed(1)
                          : option}
                      </span>
                    </div>
                  </motion.button>
                )
              })}
            </div>
          )}

          {/* Feedback */}
          <AnimatePresence>
            {result === 'correct' && (
              <motion.div
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                className="text-center"
              >
                <div className="text-5xl mb-2">🎉✨🌟</div>
                <p className="text-xl font-extrabold text-green-500">Correct! +20 XP</p>
              </motion.div>
            )}
            {result === 'wrong' && (
              <motion.div
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                className="text-center"
              >
                <div className="text-5xl mb-2">😅</div>
                <p className="text-lg font-extrabold text-red-500">
                  The correct answer was{' '}
                  {typeof problem.answer === 'number' && problem.answer % 1 !== 0
                    ? problem.answer.toFixed(1)
                    : problem.answer}
                </p>
              </motion.div>
            )}
          </AnimatePresence>
        </motion.div>
      </AnimatePresence>
    </motion.div>
  )
}
