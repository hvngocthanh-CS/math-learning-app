import { useParams, Link, useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaLock, FaPlayCircle, FaCheckCircle, FaStar, FaChevronRight, FaChevronDown, FaArrowLeft } from 'react-icons/fa'
import { ImSpinner8 } from 'react-icons/im'
import { useState, useEffect } from 'react'
import toast from 'react-hot-toast'
import api from '../../../utils/api'

const GRADE_META = {
  1: { emoji: '🐣', color: 'from-green-400 to-emerald-500' },
  2: { emoji: '🐥', color: 'from-blue-400 to-cyan-500' },
  3: { emoji: '🦊', color: 'from-purple-400 to-violet-500' },
  4: { emoji: '🦁', color: 'from-orange-400 to-amber-500' },
  5: { emoji: '🦅', color: 'from-red-400 to-rose-500' },
}

const CHAPTER_EMOJIS = ['📖', '📗', '📘', '📙', '📕', '📓', '📔', '📒']
const LESSON_EMOJIS = ['🍎', '✏️', '📊', '⚖️', '🖼️', '🖐️', '🔟', '📝', '🎈', '✋', '🧩', '💡', '🚀', '🎯', '🌟']

const statusConfig = {
  completed: {
    icon: FaCheckCircle,
    color: 'text-green-500',
    bg: 'bg-green-50',
    border: 'border-green-200',
    label: 'Completed',
  },
  in_progress: {
    icon: FaPlayCircle,
    color: 'text-secondary-500',
    bg: 'bg-secondary-50',
    border: 'border-secondary-200',
    label: 'In Progress',
  },
  locked: {
    icon: FaLock,
    color: 'text-gray-300',
    bg: 'bg-gray-50',
    border: 'border-gray-200',
    label: 'Locked',
  },
}

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.08 },
  },
}

const item = {
  hidden: { opacity: 0, y: 15 },
  show: { opacity: 1, y: 0 },
}

export default function LessonList() {
  const { gradeId } = useParams()
  const navigate = useNavigate()
  const [chapters, setChapters] = useState([])
  const [gradeInfo, setGradeInfo] = useState(null)
  const [loading, setLoading] = useState(true)
  const [openChapters, setOpenChapters] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Backend already returns chapters with lessons and correct unlock status
        const [chaptersRes, gradesRes] = await Promise.all([
          api.get(`/grades/${gradeId}/chapters`),
          api.get('/grades'),
        ])

        const chaptersData = chaptersRes.data || []

        // Map backend response directly - trust backend status
        const chaptersWithMeta = chaptersData.map((chapter, chapterIndex) => ({
          ...chapter,
          emoji: CHAPTER_EMOJIS[chapterIndex % CHAPTER_EMOJIS.length],
          lessons: (chapter.lessons || []).map((lesson, lessonIndex) => ({
            ...lesson,
            starsEarned: lesson.stars_earned || 0,
            emoji: LESSON_EMOJIS[lessonIndex % LESSON_EMOJIS.length],
            xp: lesson.xp_reward || 20,
          })),
        }))

        setChapters(chaptersWithMeta)

        // Open chapters that have in-progress or first chapter
        const activeChapterIds = chaptersWithMeta
          .filter(ch => ch.lessons.some(l => l.status === 'in_progress' || l.status === 'completed'))
          .map(ch => ch.id)
        setOpenChapters(activeChapterIds.length > 0 ? activeChapterIds : chaptersWithMeta.length > 0 ? [chaptersWithMeta[0].id] : [])

        // Set grade info
        const foundGrade = gradesRes.data.find(g => g.id === gradeId)
        if (foundGrade) {
          setGradeInfo(foundGrade)
        }
      } catch (error) {
        console.error('Failed to fetch lessons:', error)
        toast.error('Failed to load lessons. Please try again!')
      } finally {
        setLoading(false)
      }
    }
    fetchData()
  }, [gradeId])

  const toggleChapter = (id) => {
    setOpenChapters(prev =>
      prev.includes(id) ? prev.filter(c => c !== id) : [...prev, id]
    )
  }

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh]">
        <ImSpinner8 className="text-5xl text-primary-500 animate-spin mb-4" />
        <p className="text-lg font-bold text-gray-500">Loading lessons...</p>
      </div>
    )
  }

  const gradeNumber = gradeInfo?.number || 1
  const meta = GRADE_META[gradeNumber] || GRADE_META[1]
  const gradeName = gradeInfo?.name || `Grade ${gradeNumber}`
  const gradeDescription = gradeInfo?.description || 'Math Lessons'

  const totalLessons = chapters.reduce((acc, ch) => acc + ch.lessons.length, 0)
  const completedLessons = chapters.reduce(
    (acc, ch) => acc + ch.lessons.filter(l => l.status === 'completed').length, 0
  )

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-4xl mx-auto"
    >
      {/* Back Button */}
      <motion.div variants={item} className="mb-6">
        <Link
          to="/student/grades"
          className="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-white border border-gray-200 text-gray-600 font-bold text-sm hover:bg-gray-50 hover:border-gray-300 transition-all shadow-sm"
        >
          <FaArrowLeft /> Back to Grades
        </Link>
      </motion.div>

      {/* Header */}
      <motion.div
        variants={item}
        className={`bg-gradient-to-br ${meta.color} rounded-3xl p-8 text-white mb-8 relative overflow-hidden`}
      >
        <div className="absolute -top-8 -right-8 w-32 h-32 bg-white/10 rounded-full" />
        <div className="absolute -bottom-6 -left-6 w-24 h-24 bg-white/10 rounded-full" />

        <div className="relative z-10 flex items-center justify-between">
          <div>
            <div className="text-5xl mb-3">{meta.emoji}</div>
            <h1 className="text-3xl font-extrabold mb-1">{gradeName}</h1>
            <p className="text-lg opacity-90 font-medium">{gradeDescription}</p>
            <div className="mt-4 flex items-center gap-4">
              <span className="bg-white/20 px-3 py-1 rounded-full text-sm font-bold">
                {totalLessons} Lessons
              </span>
              <span className="bg-white/20 px-3 py-1 rounded-full text-sm font-bold">
                {completedLessons}/{totalLessons} Done
              </span>
            </div>
          </div>

          {/* Progress circle */}
          <div className="hidden sm:block">
            <div className="w-24 h-24 bg-white/20 rounded-full flex items-center justify-center backdrop-blur-sm">
              <div className="text-center">
                <div className="text-2xl font-extrabold">
                  {totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0}%
                </div>
                <div className="text-xs font-bold opacity-80">Done</div>
              </div>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Chapters */}
      <div className="space-y-4">
        {chapters.map((chapter) => {
          const isOpen = openChapters.includes(chapter.id)
          const chapterCompleted = chapter.lessons.filter(l => l.status === 'completed').length
          const chapterTotal = chapter.lessons.length

          return (
            <motion.div
              key={chapter.id}
              variants={item}
              className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden"
            >
              {/* Chapter Header */}
              <button
                onClick={() => toggleChapter(chapter.id)}
                className="w-full flex items-center justify-between p-5 hover:bg-gray-50 transition-colors"
              >
                <div className="flex items-center gap-3">
                  <span className="text-2xl">{chapter.emoji}</span>
                  <div className="text-left">
                    <h3 className="font-extrabold text-gray-800">{chapter.title}</h3>
                    <p className="text-sm text-gray-400 font-medium">
                      {chapterCompleted}/{chapterTotal} lessons completed
                    </p>
                  </div>
                </div>
                <motion.div
                  animate={{ rotate: isOpen ? 180 : 0 }}
                  transition={{ duration: 0.2 }}
                >
                  <FaChevronDown className="text-gray-400" />
                </motion.div>
              </button>

              {/* Lessons */}
              <motion.div
                initial={false}
                animate={{
                  height: isOpen ? 'auto' : 0,
                  opacity: isOpen ? 1 : 0,
                }}
                transition={{ duration: 0.3 }}
                className="overflow-hidden"
              >
                <div className="px-5 pb-4 space-y-2">
                  {chapter.lessons.map((lesson) => {
                    const config = statusConfig[lesson.status] || statusConfig.locked
                    const StatusIcon = config.icon
                    const isLocked = lesson.status === 'locked'

                    const handleClick = () => {
                      if (!isLocked) {
                        navigate(`/student/lessons/${lesson.id}`)
                      }
                    }

                    return (
                      <motion.div
                        key={lesson.id}
                        whileHover={!isLocked ? { x: 4 } : {}}
                        onClick={handleClick}
                        className={`
                          flex items-center justify-between p-4 rounded-xl border transition-all
                          ${config.border} ${config.bg}
                          ${isLocked ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer hover:shadow-md'}
                        `}
                      >
                        <div className="flex items-center gap-3">
                          <StatusIcon className={`text-xl ${config.color}`} />
                          <span className="text-lg">{lesson.emoji}</span>
                          <div>
                            <h4 className={`font-bold ${isLocked ? 'text-gray-400' : 'text-gray-700'}`}>
                              {lesson.title}
                            </h4>
                            <span className={`text-xs font-bold ${config.color}`}>
                              {config.label}
                            </span>
                          </div>
                        </div>

                        <div className="flex items-center gap-2">
                          {lesson.status === 'completed' && lesson.starsEarned > 0 && (
                            <span className="flex items-center gap-0.5 mr-1">
                              {[1, 2, 3].map((s) => (
                                <FaStar
                                  key={s}
                                  className={`text-sm ${s <= lesson.starsEarned ? 'text-yellow-400' : 'text-gray-200'}`}
                                />
                              ))}
                            </span>
                          )}
                          <span className={`flex items-center gap-1 text-sm font-bold ${isLocked ? 'text-gray-300' : 'text-yellow-500'}`}>
                            <FaStar /> {lesson.xp} XP
                          </span>
                          {!isLocked && (
                            <FaChevronRight className="text-gray-300 text-sm" />
                          )}
                        </div>
                      </motion.div>
                    )
                  })}
                </div>
              </motion.div>
            </motion.div>
          )
        })}
      </div>
    </motion.div>
  )
}
