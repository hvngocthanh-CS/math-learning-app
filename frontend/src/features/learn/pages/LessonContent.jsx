import { useState, useEffect } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { motion, AnimatePresence } from 'framer-motion'
import { FaChevronRight, FaArrowLeft } from 'react-icons/fa'
import { ImSpinner8 } from 'react-icons/im'
import toast from 'react-hot-toast'
import api from '../../../utils/api'
import useLessonContent from '../hooks/useLessonContent'
import LearnTab from '../components/LearnTab'
import PracticeTab from '../components/PracticeTab'
import QuizTab from '../components/QuizTab'
import LessonComplete from '../components/LessonComplete'

const TABS = [
  { id: 'learn', label: 'Learn', emoji: '📚' },
  { id: 'practice', label: 'Practice', emoji: '✏️' },
  { id: 'quiz', label: 'Quiz', emoji: '🎯' },
]

export default function LessonContent() {
  const { lessonId } = useParams()
  const navigate = useNavigate()
  const { lesson, content, loading, error } = useLessonContent(lessonId)

  const [activeTab, setActiveTab] = useState('learn')
  const [completionData, setCompletionData] = useState(null)

  // Reset state when navigating to a different lesson
  useEffect(() => {
    setActiveTab('learn')
    setCompletionData(null)
  }, [lessonId])

  // ---------- Handlers ----------

  const handleLearnComplete = () => {
    setActiveTab('practice')
    toast.success("Awesome! Now let's practice! ✏️", { icon: '🎉' })
  }

  const handlePracticeComplete = (score) => {
    toast.success(`Practice done! ${score}/5 correct. Time for the Quiz! 🎯`, { icon: '🏆' })
    setActiveTab('quiz')
  }

  const handleQuizComplete = async (quizScore, answers = []) => {
    const totalQuestions = 5
    try {
      const res = await api.post(`/lessons/${lessonId}/complete`, {
        quiz_score: quizScore,
        total_questions: totalQuestions,
        answers: answers.length > 0 ? answers : undefined,
      })
      const data = res.data
      setCompletionData({
        score: quizScore,
        totalQuestions,
        xpEarned: data.xp_earned ?? quizScore * 20,
        starsEarned: data.stars_earned ?? (quizScore >= 5 ? 3 : quizScore >= 4 ? 2 : quizScore >= 3 ? 1 : 0),
        coinsEarned: data.coins_earned ?? quizScore * 5,
        levelUp: data.level_up ?? false,
        nextLessonId: data.next_lesson_id ?? null,
      })
    } catch {
      // Fallback: show results even if API fails
      const stars = quizScore >= 5 ? 3 : quizScore >= 4 ? 2 : quizScore >= 3 ? 1 : 0
      setCompletionData({
        score: quizScore,
        totalQuestions,
        xpEarned: quizScore * 20,
        starsEarned: stars,
        coinsEarned: quizScore * 5,
        levelUp: false,
        nextLessonId: null,
      })
      toast.error('Could not save progress, but here are your results!')
    }
  }

  const handleRetake = () => {
    setCompletionData(null)
    setActiveTab('quiz')
  }

  // ---------- Loading / Error states ----------

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <ImSpinner8 className="text-5xl text-primary-500 animate-spin mb-4" />
        <p className="text-lg font-bold text-gray-500">Loading lesson...</p>
      </div>
    )
  }

  if (error === 'not_found' || (!lesson && !loading)) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <div className="text-6xl mb-4">😕</div>
        <h2 className="text-2xl font-bold text-gray-700 mb-2">
          {error === 'not_found' ? 'Content not available' : 'Lesson not found'}
        </h2>
        <Link to="/student/grades" className="text-primary-500 font-bold hover:underline">
          <FaArrowLeft className="inline mr-2" /> Back to Grades
        </Link>
      </div>
    )
  }

  // ---------- Render ----------

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="max-w-6xl mx-auto">
      {/* Breadcrumb */}
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex items-center gap-2 text-sm font-bold text-gray-400 mb-6 flex-wrap"
      >
        <Link to="/student/grades" className="hover:text-primary-500 transition-colors">
          Grades
        </Link>
        <FaChevronRight className="text-xs" />
        <span className="text-gray-700">{lesson?.title || 'Lesson'}</span>
      </motion.div>

      {/* Tab Navigation */}
      {!completionData && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          className="flex gap-2 mb-6"
        >
          {TABS.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex-1 py-3 px-4 rounded-2xl font-extrabold text-sm sm:text-base transition-all ${
                activeTab === tab.id
                  ? 'bg-gradient-to-r from-pink-500 via-purple-500 to-blue-500 text-white shadow-lg scale-105'
                  : 'bg-white text-gray-500 border border-gray-200 hover:border-gray-300'
              }`}
            >
              <span className="mr-1">{tab.emoji}</span> {tab.label}
            </button>
          ))}
        </motion.div>
      )}

      {/* Tab Content */}
      <AnimatePresence mode="wait">
        {completionData ? (
          <motion.div key="complete" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
            <LessonComplete
              score={completionData.score}
              totalQuestions={completionData.totalQuestions}
              xpEarned={completionData.xpEarned}
              starsEarned={completionData.starsEarned}
              coinsEarned={completionData.coinsEarned}
              levelUp={completionData.levelUp}
              onRetake={handleRetake}
              onNext={completionData.nextLessonId ? () => navigate(`/student/lessons/${completionData.nextLessonId}`) : null}
              onBackToGrades={() => navigate('/student/grades')}
            />
          </motion.div>
        ) : activeTab === 'learn' ? (
          <motion.div key="learn" initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: 20 }}>
            <LearnTab content={content?.learn} onComplete={handleLearnComplete} />
          </motion.div>
        ) : activeTab === 'practice' ? (
          <motion.div key="practice" initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: 20 }}>
            <PracticeTab problems={content?.practice} onComplete={handlePracticeComplete} />
          </motion.div>
        ) : (
          <motion.div key="quiz" initial={{ opacity: 0, x: -20 }} animate={{ opacity: 1, x: 0 }} exit={{ opacity: 0, x: 20 }}>
            <QuizTab problems={content?.quiz} onComplete={handleQuizComplete} />
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  )
}
