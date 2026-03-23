import { useState, useEffect, useRef } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { FaLightbulb } from 'react-icons/fa'

export default function PracticeTab({ problems, onComplete }) {
  const [current, setCurrent] = useState(0)
  const [answer, setAnswer] = useState('')
  const [result, setResult] = useState(null) // 'correct' | 'wrong' | null
  const [score, setScore] = useState(0)
  const [showHint, setShowHint] = useState(false)
  const inputRef = useRef(null)
  const timerRef = useRef(null)

  const total = problems?.length || 5

  // Focus input on problem change
  useEffect(() => {
    if (inputRef.current && result === null) {
      inputRef.current.focus()
    }
  }, [current, result])

  // Cleanup timer
  useEffect(() => {
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
    }
  }, [])

  if (!problems || problems.length === 0) return null

  const problem = problems[current]

  const isComparison = problem.subtype === 'comparison'
  const isShapeIdentify = problem.subtype === 'shape_identify'
  const isPatternPick = problem.subtype === 'pattern_pick'
  const isButtonMode = isComparison || isShapeIdentify || isPatternPick

  const checkAnswer = () => {
    if (!answer.trim()) return
    const isCorrect = isButtonMode
      ? answer.toLowerCase() === String(problem.answer).toLowerCase()
      : Math.abs(parseFloat(answer) - parseFloat(problem.answer)) < 0.01

    if (isCorrect) {
      setResult('correct')
      const newScore = score + 1
      setScore(newScore)

      // Auto-advance after 1.5s
      timerRef.current = setTimeout(() => {
        if (current < total - 1) {
          setCurrent(prev => prev + 1)
          setAnswer('')
          setResult(null)
          setShowHint(false)
        } else {
          onComplete(newScore)
        }
      }, 1500)
    } else {
      setResult('wrong')
      setShowHint(true)
    }
  }

  const retryProblem = () => {
    setAnswer('')
    setResult(null)
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="space-y-6"
    >
      {/* Progress Dots */}
      <div className="flex justify-center gap-3">
        {Array.from({ length: total }).map((_, i) => (
          <motion.div
            key={i}
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            transition={{ delay: i * 0.05 }}
            className={`w-4 h-4 rounded-full transition-all duration-300 ${
              i < current
                ? 'bg-green-400 scale-100'
                : i === current
                ? 'bg-purple-500 scale-125 ring-4 ring-purple-200'
                : 'bg-gray-200'
            }`}
          />
        ))}
      </div>

      {/* Score bar */}
      <div className="bg-white rounded-2xl shadow-md border border-gray-100 p-4 flex items-center justify-between">
        <span className="text-lg font-bold text-gray-600">
          Problem {current + 1} of {total}
        </span>
        <div className="flex items-center gap-2 text-lg font-extrabold text-green-500">
          ✅ {score}/{total} correct
        </div>
      </div>

      {/* Problem Card */}
      <AnimatePresence mode="wait">
        <motion.div
          key={current}
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -50 }}
          transition={{ type: 'spring', stiffness: 200, damping: 20 }}
          className={`bg-white rounded-3xl shadow-lg border-2 p-6 sm:p-8 ${
            result === 'correct'
              ? 'border-green-300 bg-green-50'
              : result === 'wrong'
              ? 'border-red-300'
              : 'border-gray-100'
          }`}
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
          ) : (
            <div className="text-center mb-8">
              <div className="text-5xl mb-4">
                {problem.emoji || '🔢'}
              </div>
              <p className="text-xl sm:text-2xl font-bold text-gray-700 mb-2">
                {problem.question}
              </p>
              <p className="text-3xl sm:text-4xl font-extrabold text-gray-800 tracking-wider">
                {problem.question_text}
              </p>
            </div>
          )}

          {/* Answer Input */}
          {isPatternPick ? (
            <div className="flex justify-center gap-6 mb-6">
              {(problem.options || []).map((emoji, i) => {
                const isSelected = answer === emoji
                const isCorrect = result && emoji === problem.answer
                const isWrong = result === 'wrong' && isSelected && emoji !== problem.answer
                const idleColors = [
                  'border-pink-300 bg-pink-50 hover:border-pink-500 hover:bg-pink-100',
                  'border-blue-300 bg-blue-50 hover:border-blue-500 hover:bg-blue-100',
                ]
                return (
                  <motion.button
                    key={i}
                    whileHover={!result ? { scale: 1.15, y: -4 } : {}}
                    whileTap={!result ? { scale: 0.9 } : {}}
                    onClick={() => {
                      if (result) return
                      setAnswer(emoji)
                    }}
                    disabled={!!result}
                    className={`w-28 h-28 sm:w-32 sm:h-32 rounded-3xl border-4 shadow-lg transition-all flex items-center justify-center ${
                      isCorrect
                        ? 'border-green-400 bg-green-50 shadow-green-200'
                        : isWrong
                        ? 'border-red-400 bg-red-50 shadow-red-200'
                        : isSelected
                        ? 'border-purple-400 bg-purple-50 shadow-purple-200'
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
              {(problem.options || []).map((shape) => {
                const isSelected = answer === shape
                const isCorrect = result && shape.toLowerCase() === String(problem.answer).toLowerCase()
                const isWrong = result === 'wrong' && isSelected && shape.toLowerCase() !== String(problem.answer).toLowerCase()
                const shapeIcons = { circle: '⭕', square: '⬜', triangle: '🍕', rectangle: '✉️' }
                const shapeIcon = shapeIcons[shape.toLowerCase()] || '🔷'
                return (
                  <motion.button
                    key={shape}
                    whileHover={!result ? { scale: 1.1, y: -4 } : {}}
                    whileTap={!result ? { scale: 0.9 } : {}}
                    onClick={() => {
                      if (result) return
                      setAnswer(shape)
                    }}
                    disabled={!!result}
                    className={`w-36 h-28 sm:w-40 sm:h-32 rounded-2xl border-4 shadow-md transition-all flex flex-col items-center justify-center gap-2 ${
                      isCorrect
                        ? 'border-green-400 bg-green-50 shadow-green-200'
                        : isWrong
                        ? 'border-red-400 bg-red-50 shadow-red-200'
                        : isSelected
                        ? 'border-purple-400 bg-purple-50 shadow-purple-200'
                        : 'border-gray-300 bg-white hover:border-purple-400 hover:bg-purple-50 hover:shadow-lg cursor-pointer'
                    }`}
                  >
                    <span className="text-4xl">{shapeIcon}</span>
                    <span className={`text-lg sm:text-xl font-extrabold capitalize ${
                      isCorrect ? 'text-green-600'
                        : isWrong ? 'text-red-600'
                        : isSelected ? 'text-purple-600'
                        : 'text-gray-700'
                    }`}>
                      {shape}
                    </span>
                  </motion.button>
                )
              })}
            </div>
          ) : isComparison ? (
            <div className="flex justify-center gap-4 mb-6">
              {(problem.options || ['>','<']).map((sign) => {
                const isSelected = answer === sign
                const isCorrect = result && sign === problem.answer
                const isWrong = result === 'wrong' && isSelected && sign !== problem.answer
                return (
                  <motion.button
                    key={sign}
                    whileHover={!result ? { scale: 1.1 } : {}}
                    whileTap={!result ? { scale: 0.9 } : {}}
                    onClick={() => {
                      if (result) return
                      setAnswer(sign)
                    }}
                    disabled={!!result}
                    className={`w-28 h-28 rounded-2xl text-6xl font-extrabold border-4 shadow-md transition-all ${
                      isCorrect
                        ? 'border-green-400 bg-green-50 text-green-600 shadow-green-200'
                        : isWrong
                        ? 'border-red-400 bg-red-50 text-red-600 shadow-red-200'
                        : isSelected
                        ? 'border-purple-400 bg-purple-50 text-purple-600 shadow-purple-200'
                        : 'border-gray-300 bg-white text-gray-700 hover:border-purple-400 hover:bg-purple-50 hover:shadow-lg cursor-pointer'
                    }`}
                  >
                    {sign}
                  </motion.button>
                )
              })}
            </div>
          ) : (
            <div className="max-w-xs mx-auto mb-6">
              <motion.input
                ref={inputRef}
                animate={result === 'wrong' ? { x: [0, -10, 10, -10, 10, 0] } : {}}
                transition={{ duration: 0.4 }}
                type="number"
                value={answer}
                onChange={(e) => setAnswer(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && (result === 'wrong' ? retryProblem() : checkAnswer())}
                placeholder="Type your answer..."
                disabled={result === 'correct'}
                className={`w-full text-center text-3xl font-extrabold p-4 rounded-2xl border-3 outline-none transition-all ${
                  result === 'correct'
                    ? 'border-green-400 bg-green-50 text-green-600'
                    : result === 'wrong'
                    ? 'border-red-400 bg-red-50 text-red-600'
                    : 'border-gray-200 focus:border-purple-400 text-gray-800'
                }`}
              />
            </div>
          )}

          {/* Feedback */}
          <AnimatePresence>
            {result === 'correct' && (
              <motion.div
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0 }}
                className="text-center mb-6"
              >
                <div className="text-5xl mb-2">🎉🌟🎊</div>
                <motion.div
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: 0.2, type: 'spring' }}
                  className="inline-block bg-gradient-to-r from-green-400 to-emerald-500 text-white px-4 py-2 rounded-full font-extrabold text-lg shadow-lg"
                >
                  +10 XP ⭐
                </motion.div>
                <p className="text-xl font-extrabold text-green-500 mt-2">
                  Correct! Amazing!
                </p>
              </motion.div>
            )}
            {result === 'wrong' && (
              <motion.div
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0 }}
                className="text-center mb-6"
              >
                <div className="text-5xl mb-2">🤔</div>
                <p className="text-xl font-extrabold text-red-500">
                  Not quite! Try again!
                </p>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Hint */}
          <AnimatePresence>
            {showHint && problem.hint && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                exit={{ opacity: 0, height: 0 }}
                className="bg-yellow-50 border-2 border-yellow-200 rounded-2xl p-4 mb-6 text-center"
              >
                <p className="text-yellow-700 font-bold flex items-center justify-center gap-2">
                  <FaLightbulb className="text-yellow-400 text-xl" />
                  {problem.hint}
                </p>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Buttons */}
          <div className="flex justify-center gap-3 flex-wrap">
            {!showHint && result !== 'correct' && (
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => setShowHint(true)}
                className="px-6 py-3 rounded-xl font-bold text-yellow-600 bg-yellow-50 border-2 border-yellow-200 hover:bg-yellow-100 transition-all"
              >
                💡 Hint
              </motion.button>
            )}

            {result === null && (
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={checkAnswer}
                className="px-8 py-3 rounded-xl font-extrabold text-white bg-gradient-to-r from-purple-500 to-blue-500 shadow-lg hover:shadow-xl transition-all"
              >
                Check Answer ✓
              </motion.button>
            )}

            {result === 'wrong' && (
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={retryProblem}
                className="px-8 py-3 rounded-xl font-extrabold text-white bg-gradient-to-r from-orange-400 to-pink-500 shadow-lg hover:shadow-xl transition-all"
              >
                Try Again! 💪
              </motion.button>
            )}
          </div>
        </motion.div>
      </AnimatePresence>
    </motion.div>
  )
}
