import { useState, useEffect, useRef, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Link } from 'react-router-dom'
import { FaArrowLeft, FaStar, FaRedo, FaEye } from 'react-icons/fa'
import { generateProblem } from '../utils/problemGenerator'

const GRADE_LABELS = ['', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5']
const GRADE_COLORS = [
  '',
  'from-green-400 to-emerald-500',
  'from-blue-400 to-cyan-500',
  'from-purple-400 to-violet-500',
  'from-orange-400 to-amber-500',
  'from-pink-400 to-rose-500',
]


const PAIR_COUNTS = { easy: 4, medium: 6, hard: 8 }
const MODE_LABELS = { easy: 'Easy (4 pairs)', medium: 'Medium (6 pairs)', hard: 'Hard (8 pairs)' }
const MODE_COLS = { easy: 4, medium: 4, hard: 4 }

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

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

function generateCards(grade, pairCount) {
  const pairs = []
  const seenQuestions = new Set()
  const seenAnswers = new Set()
  let attempts = 0
  while (pairs.length < pairCount && attempts < 500) {
    const p = generateProblem(grade)
    const answerKey = String(p.answer)
    // Ensure both unique questions AND unique answers
    if (!seenQuestions.has(p.question) && !seenAnswers.has(answerKey)) {
      seenQuestions.add(p.question)
      seenAnswers.add(answerKey)
      pairs.push({ question: p.question, answer: p.answer })
    }
    attempts++
  }

  // Create card pairs: one card with the question, one with the answer
  const cards = []
  pairs.forEach((pair, i) => {
    cards.push({
      id: `q-${i}`,
      pairId: i,
      display: pair.question,
      type: 'question',
      answer: String(pair.answer),
    })
    cards.push({
      id: `a-${i}`,
      pairId: i,
      display: String(pair.answer),
      type: 'answer',
      answer: String(pair.answer),
    })
  })
  return shuffle(cards)
}

export default function MathMemoryGame() {
  const [phase, setPhase] = useState('setup') // setup | playing | complete
  const [grade, setGrade] = useState(1)
  const [mode, setMode] = useState('easy')
  const [cards, setCards] = useState([])
  const [flipped, setFlipped] = useState([])       // indices of currently flipped (max 2)
  const [matched, setMatched] = useState(new Set()) // pairIds that are matched
  const [moves, setMoves] = useState(0)
  const [time, setTime] = useState(0)
  const [peeking, setPeeking] = useState(false)
  const timerRef = useRef(null)
  const lockRef = useRef(false)

  const totalPairs = PAIR_COUNTS[mode]

  const startGame = () => {
    const newCards = generateCards(grade, totalPairs)
    setCards(newCards)
    setFlipped([])
    setMatched(new Set())
    setMoves(0)
    setTime(0)
    setPeeking(false)
    lockRef.current = false
    setPhase('playing')
  }

  // Timer
  useEffect(() => {
    if (phase !== 'playing') return
    timerRef.current = setInterval(() => setTime((t) => t + 1), 1000)
    return () => clearInterval(timerRef.current)
  }, [phase])

  // Check for match when 2 cards flipped
  useEffect(() => {
    if (flipped.length !== 2) return
    lockRef.current = true
    const [i1, i2] = flipped
    const c1 = cards[i1]
    const c2 = cards[i2]

    if (c1.answer === c2.answer && c1.type !== c2.type) {
      // Match found!
      setTimeout(() => {
        setMatched((prev) => {
          const next = new Set(prev)
          next.add(c1.pairId)
          if (c1.pairId !== c2.pairId) next.add(c2.pairId)
          // Check win
          if (next.size === totalPairs) {
            clearInterval(timerRef.current)
            setTimeout(() => setPhase('complete'), 400)
          }
          return next
        })
        setFlipped([])
        lockRef.current = false
      }, 500)
    } else {
      // No match — flip back
      setTimeout(() => {
        setFlipped([])
        lockRef.current = false
      }, 800)
    }
  }, [flipped, cards, totalPairs])

  const handleCardClick = (index) => {
    if (phase !== 'playing' || lockRef.current || peeking) return
    if (flipped.includes(index)) return
    if (matched.has(cards[index].pairId)) return
    if (flipped.length >= 2) return

    setFlipped((prev) => [...prev, index])
    if (flipped.length === 0) {
      // First card of a pair — count as a move
      setMoves((m) => m + 1)
    }
  }

  const handlePeek = () => {
    if (peeking) return
    setPeeking(true)
    setMoves((m) => m + 2) // Penalty: +2 moves
    setTimeout(() => setPeeking(false), 1500)
  }

  const formatTime = (s) => {
    const m = Math.floor(s / 60)
    const sec = s % 60
    return `${m}:${sec.toString().padStart(2, '0')}`
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
          <span className="text-7xl block mb-4">🃏</span>
          <h1 className="text-3xl font-extrabold text-gray-800 mb-2">Math Memory</h1>
          <p className="text-gray-500 mb-8">
            Flip cards to match math problems with their answers!
            <br />
            Find all pairs with the fewest moves.
          </p>

          <div className="mb-6">
            <p className="text-sm font-bold text-gray-400 uppercase tracking-wide mb-3">
              Difficulty (Grade)
            </p>
            <GradeSelector grade={grade} setGrade={setGrade} />
          </div>

          <div className="mb-8">
            <p className="text-sm font-bold text-gray-400 uppercase tracking-wide mb-3">
              Board Size
            </p>
            <div className="flex justify-center gap-3">
              {Object.entries(MODE_LABELS).map(([key, label]) => (
                <motion.button
                  key={key}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  onClick={() => setMode(key)}
                  className={`px-4 py-2 rounded-full font-bold text-sm transition-all ${
                    mode === key
                      ? 'bg-gradient-to-r from-orange-400 to-amber-500 text-white shadow-lg'
                      : 'bg-white text-gray-600 shadow-md border border-gray-200'
                  }`}
                >
                  {label}
                </motion.button>
              ))}
            </div>
          </div>

          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={startGame}
            className="w-full py-4 rounded-2xl bg-gradient-to-r from-orange-500 to-amber-500 text-white font-extrabold text-xl shadow-lg shadow-orange-200"
          >
            Start Game
          </motion.button>
        </div>
      </motion.div>
    )
  }

  // ── Complete Screen ──
  if (phase === 'complete') {
    const perfectMoves = totalPairs // Best possible = 1 move per pair
    const stars = moves <= perfectMoves + 2 ? 3 : moves <= perfectMoves * 2 ? 2 : 1
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="max-w-lg mx-auto text-center"
      >
        <div className="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">
          <span className="text-6xl block mb-3">🎉</span>
          <h2 className="text-3xl font-extrabold text-gray-800 mb-2">All Pairs Found!</h2>

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
            <div className="bg-orange-50 rounded-2xl p-4">
              <p className="text-2xl font-extrabold text-orange-600">{moves}</p>
              <p className="text-xs font-bold text-orange-400 uppercase">Moves</p>
            </div>
            <div className="bg-blue-50 rounded-2xl p-4">
              <p className="text-2xl font-extrabold text-blue-600">{formatTime(time)}</p>
              <p className="text-xs font-bold text-blue-400 uppercase">Time</p>
            </div>
            <div className="bg-green-50 rounded-2xl p-4">
              <p className="text-2xl font-extrabold text-green-600">{totalPairs}</p>
              <p className="text-xs font-bold text-green-400 uppercase">Pairs</p>
            </div>
          </div>

          <div className="flex gap-3">
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => setPhase('setup')}
              className="flex-1 py-3 rounded-2xl bg-gradient-to-r from-orange-500 to-amber-500 text-white font-bold shadow-md flex items-center justify-center gap-2"
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
      {/* Top bar */}
      <div className="flex items-center justify-between mb-5">
        <div className="bg-white rounded-2xl shadow-md px-5 py-2.5 flex items-center gap-2">
          <span className="text-lg">🃏</span>
          <span className="font-extrabold text-orange-600">{moves} moves</span>
        </div>
        <div className="bg-white rounded-2xl shadow-md px-5 py-2.5 flex items-center gap-2">
          <span className="text-lg">⏱️</span>
          <span className="font-extrabold text-blue-600">{formatTime(time)}</span>
        </div>
        <div className="bg-white rounded-2xl shadow-md px-5 py-2.5 flex items-center gap-2">
          <span className="font-extrabold text-green-600">
            {matched.size}/{totalPairs}
          </span>
          <span className="text-sm text-gray-400">pairs</span>
        </div>
      </div>

      {/* Peek button */}
      <div className="text-center mb-4">
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={handlePeek}
          disabled={peeking}
          className={`inline-flex items-center gap-2 px-4 py-2 rounded-full text-sm font-bold transition-all ${
            peeking
              ? 'bg-yellow-200 text-yellow-700'
              : 'bg-white text-gray-500 shadow-md hover:shadow-lg border border-gray-200'
          }`}
        >
          <FaEye /> {peeking ? 'Peeking... (+2 moves)' : 'Peek (costs 2 moves)'}
        </motion.button>
      </div>

      {/* Card grid */}
      <div
        className="grid gap-3"
        style={{
          gridTemplateColumns: `repeat(${MODE_COLS[mode]}, 1fr)`,
        }}
      >
        {cards.map((card, index) => {
          const isFlipped = flipped.includes(index)
          const isMatched = matched.has(card.pairId)
          const showFace = isFlipped || isMatched || peeking

          return (
            <motion.button
              key={card.id}
              onClick={() => handleCardClick(index)}
              whileHover={!showFace ? { scale: 1.05 } : {}}
              whileTap={!showFace ? { scale: 0.95 } : {}}
              className="relative aspect-[3/4] rounded-2xl cursor-pointer select-none"
              style={{ perspective: '600px' }}
            >
              <motion.div
                animate={{ rotateY: showFace ? 180 : 0 }}
                transition={{ duration: 0.4, ease: 'easeInOut' }}
                className="absolute inset-0"
                style={{ transformStyle: 'preserve-3d' }}
              >
                {/* Card Back — all cards same color */}
                <div
                  className="absolute inset-0 rounded-2xl bg-gradient-to-br from-indigo-400 to-purple-500
                    flex items-center justify-center shadow-lg border-2 border-white/30"
                  style={{ backfaceVisibility: 'hidden' }}
                >
                  <span className="text-3xl opacity-80">?</span>
                  <div className="absolute top-3 left-3 w-6 h-6 bg-white/20 rounded-full" />
                </div>

                {/* Card Face */}
                <div
                  className={`absolute inset-0 rounded-2xl flex flex-col items-center justify-center
                    shadow-lg border-2 p-2 ${
                    isMatched
                      ? 'bg-green-50 border-green-300'
                      : 'bg-white border-gray-200'
                  }`}
                  style={{
                    backfaceVisibility: 'hidden',
                    transform: 'rotateY(180deg)',
                  }}
                >
                  {card.type === 'question' ? (
                    <>
                      <p className="text-xs font-bold text-gray-400 uppercase mb-1">Problem</p>
                      <p className="text-lg font-extrabold text-gray-800 leading-tight text-center">
                        {card.display}
                      </p>
                    </>
                  ) : (
                    <>
                      <p className="text-xs font-bold text-gray-400 uppercase mb-1">Answer</p>
                      <p className="text-2xl font-extrabold text-blue-600">{card.display}</p>
                    </>
                  )}
                  {isMatched && (
                    <span className="absolute top-1 right-1 text-green-500 text-sm">✓</span>
                  )}
                </div>
              </motion.div>
            </motion.button>
          )
        })}
      </div>
    </div>
  )
}
