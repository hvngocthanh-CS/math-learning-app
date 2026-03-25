import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  FaTrophy, FaStar, FaSpinner, FaCheckCircle, FaTimesCircle, FaFire,
} from 'react-icons/fa'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.06 } },
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function TeacherRanking() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.get('/teacher/ranking')
      .then((res) => setData(res.data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[60vh]">
        <FaSpinner className="animate-spin text-4xl text-orange-400" />
      </div>
    )
  }

  const rankings = data?.rankings || []

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-4xl mx-auto space-y-6"
    >
      <motion.div variants={item}>
        <h1 className="text-3xl font-extrabold text-gray-800">Student Rankings</h1>
        <p className="text-gray-500 mt-1">
          Overall ranking of all {data?.total_students || 0} students.
        </p>
      </motion.div>

      {rankings.length === 0 ? (
        <motion.div variants={item} className="text-center py-20">
          <div className="text-6xl mb-4">🏆</div>
          <p className="text-gray-400 font-bold">No students yet</p>
        </motion.div>
      ) : (
        <motion.div variants={item} className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="bg-gray-50 text-left">
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase w-12">Rank</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase">Student</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Level</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Stars</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Lessons</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Avg Score</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Correct</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Incorrect</th>
                  <th className="px-4 py-3 text-xs font-bold text-gray-400 uppercase text-center">Streak</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-50">
                {rankings.map((entry) => {
                  const rankBadge = entry.rank === 1 ? '🥇' : entry.rank === 2 ? '🥈' : entry.rank === 3 ? '🥉' : entry.rank

                  return (
                    <motion.tr
                      key={entry.student_id}
                      variants={item}
                      whileHover={{ backgroundColor: 'rgba(249,250,251,1)' }}
                      className="transition-colors"
                    >
                      <td className="px-4 py-3 text-center">
                        <span className={`text-lg ${entry.rank <= 3 ? '' : 'font-extrabold text-gray-300'}`}>
                          {rankBadge}
                        </span>
                      </td>
                      <td className="px-4 py-3">
                        <Link to={`/teacher/students/${entry.student_id}`} className="hover:text-orange-500 transition-colors">
                          <span className="font-bold text-gray-700 text-sm">{entry.name}</span>
                        </Link>
                      </td>
                      <td className="px-4 py-3 text-center text-sm font-bold text-gray-600">{entry.level}</td>
                      <td className="px-4 py-3 text-center">
                        <span className="inline-flex items-center gap-1 text-sm font-bold text-yellow-600">
                          <FaStar className="text-yellow-400 text-xs" /> {entry.stars}
                        </span>
                      </td>
                      <td className="px-4 py-3 text-center text-sm font-bold text-blue-600">{entry.lessons_completed}</td>
                      <td className="px-4 py-3 text-center text-sm font-bold text-purple-600">{entry.average_score}%</td>
                      <td className="px-4 py-3 text-center">
                        <span className="inline-flex items-center gap-1 text-sm font-bold text-green-600">
                          <FaCheckCircle className="text-xs" /> {entry.total_correct}
                        </span>
                      </td>
                      <td className="px-4 py-3 text-center">
                        <span className="inline-flex items-center gap-1 text-sm font-bold text-red-500">
                          <FaTimesCircle className="text-xs" /> {entry.total_incorrect}
                        </span>
                      </td>
                      <td className="px-4 py-3 text-center">
                        <span className="inline-flex items-center gap-1 text-sm font-bold text-orange-600">
                          <FaFire className="text-xs" /> {entry.streak}
                        </span>
                      </td>
                    </motion.tr>
                  )
                })}
              </tbody>
            </table>
          </div>
        </motion.div>
      )}
    </motion.div>
  )
}
