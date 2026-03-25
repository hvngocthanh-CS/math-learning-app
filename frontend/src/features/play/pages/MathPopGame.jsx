import { useState, useEffect, useRef, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Link } from 'react-router-dom'
import { FaArrowLeft, FaHeart, FaStar, FaRedo } from 'react-icons/fa'
import { generateProblem } from '../utils/problemGenerator'

const BUBBLE_COLORS = [
  'from-pink-400 to-rose-500',
  'from-blue-400 to-cyan-500',
  'from-green-400 to-emerald-500',
  'from-purple-400 to-violet-500',
  'from-orange-400 to-amber-500',
  'from-teal-400 to-cyan-500',
]

const GRADE_LABELS = ['', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5']
const GRADE_COLORS = [
  '',
  'from-green-400 to-emerald-500',
  'from-blue-400 to-cyan-500',
  'from-purple-400 to-violet-500',
  'from-orange-400 to-amber-500',
  'from-pink-400 to-rose-500',
]

function GradeSelector({ grade, setGrade }) {
  return (
    <div className="flex flex-wrap justify-center gap-3">
      {[1, 2, 3, 4, 5].map((g) => (
        <motion.button
          key={g}
          whileHover={{ scale: 1.08 }}
          whileTap={{ scale: 0.95 }}
          onClick={() => setGrade(g)}
          className={`px-5 py-2.5 rounded-full font-bold text-sm transition-all ${
            grade === g
              ? `bg-gradient-to-r ${GRADE_COLORS[g]} text-white shadow-lg`
              : 'bg-white text-gray-600 shadow-md hover:shadow-lg border border-gray-200'
          }`}
        >
          {GRADE_LABELS[g]}
        </motion.button>
      ))}
    </div>
  )
}

export default function MathPopGame() {
  const [phase, setPhase] = useState('setup') // setup | playing | gameover
  const [grade, setGrade] = useState(1)
  const [score, setScore] = useState(0)
  const [lives, setLives] = useState(3)
  const [problem, setProblem] = useState(null)
  const [bubbles, setBubbles] = useState([])
  const [correct, setCorrect] = useState(0)
  const [total, setTotal] = useState(0)
  const [flash, setFlash] = useState(null) // 'correct' | 'wrong' | null
  const [floatDuration, setFloatDuration] = useState(5)
  const missTimerRef = useRef(null)

  const nextQuestion = useCallback(() => {
    const p = generateProblem(grade)
    setProblem(p)
    // Create bubbles in spaced columns
    const cols = p.choices.length
    const newBubbles = p.choices.map((val, i) => ({
      id: Date.now() + i,
      value: val,
      col: i,
      cols,
      color: BUBBLE_COLORS[i % BUBBLE_COLORS.length],
      alive: true,
    }))
    setBubbles(newBubbles)
  }, [grade])

  const startGame = () => {
    setScore(0)
    setLives(3)
    setCorrect(0)
    setTotal(0)
    setFloatDuration(5)
    setPhase('playing')
  }

  useEffect(() => {
    if (phase === 'playing') {
      nextQuestion()
    }
    return () => {
      if (missTimerRef.current) clearTimeout(missTimerRef.current)
    }
  }, [phase, nextQuestion])

  // Timer for bubble floating away (miss)
  useEffect(() => {
    if (phase !== 'playing' || !problem) return
    if (missTimerRef.current) clearTimeout(missTimerRef.current)
    missTimerRef.current = setTimeout(() => {
      // Bubbles floated away — lose a life
      setTotal((t) => t + 1)
      setLives((l) => {
        const newLives = l - 1
        if (newLives <= 0) {
          setPhase('gameover')
        } else {
          nextQuestion()
        }
        return newLives
      })
      setFlash('wrong')
      setTimeout(() => setFlash(null), 400)
    }, floatDuration * 1000)
    return () => {
      if (missTimerRef.current) clearTimeout(missTimerRef.current)
    }
  }, [problem, phase, floatDuration, nextQuestion])

  const handleBubbleTap = (value) => {
    if (phase !== 'playing') return
    if (missTimerRef.current) clearTimeout(missTimerRef.current)

    setTotal((t) => t + 1)
    if (value === problem.answer) {
      const points = grade * 10
      setScore((s) => s + points)
      setCorrect((c) => {
        const newCorrect = c + 1
        // Speed up every 5 correct answers
        if (newCorrect % 5 === 0 && floatDuration > 2.5) {
          setFloatDuration((d) => Math.max(2.5, d - 0.3))
        }
        return newCorrect
      })
      setFlash('correct')
      setTimeout(() => {
        setFlash(null)
        nextQuestion()
      }, 350)
    } else {
      setFlash('wrong')
      setLives((l) => {
        const newLives = l - 1
        if (newLives <= 0) {
          setTimeout(() => setPhase('gameover'), 400)
        } else {
          setTimeout(() => {
            setFlash(null)
            nextQuestion()
          }, 400)
        }
        return newLives
      })
    }
  }

  // ── Setup Screen ──
  if (phase === 'setup') {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="max-w-lg mx-auto text-center"
      >
        <Link
          to="/student/play"
          className="inline-flex items-center gap-2 text-gray-500 hover:text-gray-700 mb-6 font-semibold"
        >
          <FaArrowLeft /> Back to Games
        </Link>

        <div className="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">
          <span className="text-7xl block mb-4">🫧</span>
          <h1 className="text-3xl font-extrabold text-gray-800 mb-2">Math Pop</h1>
          <p className="text-gray-500 mb-8">
            Tap the bubble with the correct answer before it floats away!
          </p>

          <div className="mb-8">
            <p className="text-sm font-bold text-gray-400 uppercase tracking-wide mb-3">
              Choose Difficulty
            </p>
            <GradeSelector grade={grade} setGrade={setGrade} />
          </div>

          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={startGame}
            className="w-full py-4 rounded-2xl bg-gradient-to-r from-purple-500 to-blue-500 text-white font-extrabold text-xl shadow-lg shadow-purple-200"
          >
            Start Game
          </motion.button>
        </div>
      </motion.div>
    )
  }

  // ── Game Over Screen ──
  if (phase === 'gameover') {
    const accuracy = total > 0 ? Math.round((correct / total) * 100) : 0
    const stars = score >= grade * 200 ? 3 : score >= grade * 100 ? 2 : 1
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="max-w-lg mx-auto text-center"
      >
        <div className="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">
          <span className="text-6xl block mb-3">🎉</span>
          <h2 className="text-3xl font-extrabold text-gray-800 mb-2">Game Over!</h2>

          {/* Stars */}
          <div className="flex justify-center gap-2 mb-6">
            {[1, 2, 3].map((s) => (
              <motion.div
                key={s}
                initial={{ scale: 0, rotate: -180 }}
                animate={{ scale: 1, rotate: 0 }}
                transition={{ delay: s * 0.2, type: 'spring' }}
              >
                <FaStar
                  className={`text-4xl ${s <= stars ? 'text-yellow-400' : 'text-gray-200'}`}
                />
              </motion.div>
            ))}
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-4 mb-8">
            <div className="bg-purple-50 rounded-2xl p-4">
              <p className="text-2xl font-extrabold text-purple-600">{score}</p>
              <p className="text-xs font-bold text-purple-400 uppercase">Score</p>
            </div>
            <div className="bg-green-50 rounded-2xl p-4">
              <p className="text-2xl font-extrabold text-green-600">{correct}</p>
              <p className="text-xs font-bold text-green-400 uppercase">Correct</p>
            </div>
            <div className="bg-blue-50 rounded-2xl p-4">
              <p className="text-2xl font-extrabold text-blue-600">{accuracy}%</p>
              <p className="text-xs font-bold text-blue-400 uppercase">Accuracy</p>
            </div>
          </div>

          <div className="flex gap-3">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => { setPhase('setup') }}
              className="flex-1 py-3 rounded-2xl bg-gradient-to-r from-purple-500 to-blue-500 text-white font-bold shadow-md flex items-center justify-center gap-2"
            >
              <FaRedo /> Play Again
            </motion.button>
            <Link
              to="/student/play"
              className="flex-1 py-3 rounded-2xl bg-gray-100 text-gray-600 font-bold text-center hover:bg-gray-200 transition-colors"
            >
              Back
            </Link>
          </div>
        </div>
      </motion.div>
    )
  }

  // ── Playing Screen ──
  return (
    <div className="max-w-2xl mx-auto">
      {/* Top bar: score + lives */}
      <div className="flex items-center justify-between mb-4">
        <div className="bg-white rounded-2xl shadow-md px-5 py-2.5 flex items-center gap-3">
          <span className="text-lg">🫧</span>
          <span className="font-extrabold text-purple-600 text-xl">{score}</span>
        </div>
        <div className="bg-white rounded-2xl shadow-md px-5 py-2.5 flex items-center gap-1.5">
          {[...Array(3)].map((_, i) => (
            <FaHeart
              key={i}
              className={`text-xl ${i < lives ? 'text-red-400' : 'text-gray-200'}`}
            />
          ))}
        </div>
      </div>

      {/* Question */}
      <motion.div
        key={problem?.question}
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        className={`text-center rounded-2xl shadow-lg p-6 mb-6 transition-colors duration-200 ${
          flash === 'correct'
            ? 'bg-green-100 border-2 border-green-400'
            : flash === 'wrong'
            ? 'bg-red-100 border-2 border-red-400'
            : 'bg-white border border-gray-100'
        }`}
      >
        <p className="text-sm font-bold text-gray-400 uppercase tracking-wide mb-1">
          What is...
        </p>
        <p className="text-4xl font-extrabold text-gray-800">{problem?.question} = ?</p>
      </motion.div>

      {/* Bubble area */}
      <div
        className="relative rounded-3xl overflow-hidden bg-gradient-to-b from-blue-50 via-purple-50 to-pink-50 border border-gray-100 shadow-inner"
        style={{ height: '380px' }}
      >
        {/* Decorative background dots */}
        <div className="absolute inset-0 opacity-10 pointer-events-none">
          {[...Array(12)].map((_, i) => (
            <div
              key={i}
              className="absolute rounded-full bg-purple-300"
              style={{
                width: `${8 + (i % 4) * 4}px`,
                height: `${8 + (i % 4) * 4}px`,
                left: `${(i * 23 + 5) % 90}%`,
                top: `${(i * 17 + 10) % 85}%`,
              }}
            />
          ))}
        </div>

        <AnimatePresence mode="popLayout">
          {bubbles.map((bubble) => {
            const colWidth = 100 / bubble.cols
            const leftPercent = colWidth * bubble.col + colWidth / 2
            return (
              <motion.button
                key={bubble.id}
                initial={{ y: 320, opacity: 0, scale: 0.5 }}
                animate={{ y: -100, opacity: 1, scale: 1 }}
                exit={{ scale: 1.5, opacity: 0 }}
                transition={{
                  y: { duration: floatDuration, ease: 'linear' },
                  opacity: { duration: 0.3 },
                  scale: { duration: 0.3 },
                }}
                onClick={() => handleBubbleTap(bubble.value)}
                className={`absolute w-18 h-18 rounded-full bg-gradient-to-br ${bubble.color}
                  text-white font-extrabold text-2xl flex items-center justify-center
                  shadow-lg cursor-pointer hover:shadow-xl select-none`}
                style={{
                  left: `calc(${leftPercent}% - 36px)`,
                  width: '72px',
                  height: '72px',
                }}
                whileHover={{ scale: 1.15 }}
                whileTap={{ scale: 0.9 }}
              >
                {/* Shine effect */}
                <div className="absolute top-2 left-3 w-4 h-4 bg-white/30 rounded-full" />
                <span className="relative z-10">{bubble.value}</span>
              </motion.button>
            )
          })}
        </AnimatePresence>
      </div>
    </div>
  )
}
