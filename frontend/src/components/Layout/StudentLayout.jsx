import { NavLink, Outlet, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaHome, FaBook, FaGamepad, FaTrophy } from 'react-icons/fa'
import { useAuth } from '../../features/auth'

const sidebarItems = [
  { to: '/student', icon: FaHome, label: 'Home', end: true, matchPaths: ['/student'] },
  { to: '/student/grades', icon: FaBook, label: 'Learn', matchPaths: ['/student/grades', '/student/lessons'] },
  { to: '/student/play', icon: FaGamepad, label: 'Play', matchPaths: ['/student/play'] },
  { to: '/student/rank', icon: FaTrophy, label: 'Rank', matchPaths: ['/student/rank'] },
]

// Mock user stats (replace with real API data)
const mockStats = {
  level: 12,
  xp: 2340,
  xpMax: 3000,
  streak: 7,
  stars: 456,
  coins: 1280,
}

const decoItems = [
  // Row 1
  { emoji: '🌈', top: '5%', left: '8%', size: '1.6rem', delay: '0s' },
  { emoji: '⭐', top: '3%', left: '25%', size: '1.2rem', delay: '0.5s' },
  { emoji: '🐱', top: '8%', left: '45%', size: '1.4rem', delay: '1s' },
  { emoji: '🌟', top: '4%', left: '65%', size: '1.3rem', delay: '1.5s' },
  { emoji: '🌈', top: '7%', left: '82%', size: '1.5rem', delay: '0.3s' },
  // Row 2
  { emoji: '🐰', top: '18%', left: '12%', size: '1.4rem', delay: '2s' },
  { emoji: '✨', top: '22%', left: '35%', size: '1.1rem', delay: '0.8s' },
  { emoji: '🌸', top: '20%', left: '55%', size: '1.3rem', delay: '1.2s' },
  { emoji: '🐣', top: '16%', left: '75%', size: '1.4rem', delay: '0.6s' },
  { emoji: '💫', top: '24%', left: '92%', size: '1.2rem', delay: '1.8s' },
  // Row 3
  { emoji: '🌻', top: '35%', left: '5%', size: '1.5rem', delay: '1.3s' },
  { emoji: '🐧', top: '38%', left: '22%', size: '1.3rem', delay: '0.4s' },
  { emoji: '⭐', top: '33%', left: '42%', size: '1.1rem', delay: '2.2s' },
  { emoji: '🌈', top: '40%', left: '60%', size: '1.5rem', delay: '0.9s' },
  { emoji: '🐶', top: '36%', left: '78%', size: '1.4rem', delay: '1.6s' },
  // Row 4
  { emoji: '✨', top: '50%', left: '10%', size: '1.2rem', delay: '0.7s' },
  { emoji: '🦊', top: '55%', left: '30%', size: '1.4rem', delay: '1.1s' },
  { emoji: '🌟', top: '52%', left: '50%', size: '1.3rem', delay: '2.5s' },
  { emoji: '🐻', top: '48%', left: '70%', size: '1.4rem', delay: '0.2s' },
  { emoji: '🌸', top: '53%', left: '88%', size: '1.3rem', delay: '1.4s' },
  // Row 5
  { emoji: '🐱', top: '65%', left: '6%', size: '1.3rem', delay: '1.7s' },
  { emoji: '💫', top: '68%', left: '25%', size: '1.1rem', delay: '0.5s' },
  { emoji: '🌈', top: '62%', left: '45%', size: '1.5rem', delay: '2.1s' },
  { emoji: '⭐', top: '70%', left: '65%', size: '1.2rem', delay: '0.8s' },
  { emoji: '🌈', top: '66%', left: '85%', size: '1.5rem', delay: '1.9s' },
  // Row 6
  { emoji: '🐰', top: '80%', left: '15%', size: '1.4rem', delay: '1.0s' },
  { emoji: '🌻', top: '82%', left: '38%', size: '1.3rem', delay: '2.3s' },
  { emoji: '✨', top: '78%', left: '55%', size: '1.1rem', delay: '0.3s' },
  { emoji: '🐣', top: '85%', left: '72%', size: '1.4rem', delay: '1.5s' },
  { emoji: '🌟', top: '83%', left: '90%', size: '1.2rem', delay: '0.6s' },
]

export default function StudentLayout() {
  const { user, logout } = useAuth()
  const location = useLocation()
  const stats = mockStats
  const xpPercent = Math.round((stats.xp / stats.xpMax) * 100)

  return (
    <div className="min-h-screen bg-app flex">
      {/* Cute floating decorations */}
      <div className="bg-deco" aria-hidden="true">
        {decoItems.map((item, i) => (
          <span
            key={i}
            className="bg-deco-item"
            style={{
              top: item.top,
              left: item.left,
              animationDelay: item.delay,
            }}
          >
            {item.emoji}
          </span>
        ))}
      </div>
      {/* Left Sidebar */}
      <aside className="fixed left-0 top-0 bottom-0 w-20 bg-gradient-to-b from-white via-purple-50/40 to-blue-50/40 shadow-lg z-40 flex flex-col items-center py-6 border-r border-purple-100/50">
        {/* Logo */}
        <div className="text-3xl mb-8 cursor-pointer hover:scale-110 transition-transform">
          🦉
        </div>

        {/* Nav Items */}
        <nav className="flex-1 flex flex-col items-center gap-2">
          {sidebarItems.map((item) => {
            const active = item.end
              ? location.pathname === item.to
              : item.matchPaths.some((p) => location.pathname.startsWith(p))
            return (
              <NavLink
                key={item.to}
                to={item.to}
                className="group"
              >
                {() => (
                  <motion.div
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.95 }}
                    className={`
                      w-16 h-16 rounded-2xl flex flex-col items-center justify-center gap-1 transition-all duration-200
                      ${active
                        ? 'bg-gradient-to-br from-purple-500 to-blue-500 text-white shadow-lg shadow-purple-300 ring-2 ring-purple-300'
                        : 'text-gray-400 hover:bg-gray-100 hover:text-gray-600'
                      }
                    `}
                  >
                    <item.icon className="text-xl" />
                    <span className="text-[11px] font-bold">{item.label}</span>
                  </motion.div>
                )}
              </NavLink>
            )
          })}
        </nav>

        {/* Logout */}
        <motion.button
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.95 }}
          onClick={logout}
          className="w-16 h-16 rounded-2xl flex flex-col items-center justify-center gap-1 text-gray-400 hover:bg-red-50 hover:text-red-500 transition-all"
          title="Logout"
        >
          <span className="text-lg">🚪</span>
          <span className="text-[10px] font-bold">Exit</span>
        </motion.button>
      </aside>

      {/* Main Area */}
      <div className="flex-1 ml-20">
        {/* Top Bar */}
        <header className="fixed top-0 left-20 right-0 h-16 bg-white/80 backdrop-blur-md shadow-sm z-30 flex items-center px-6 border-b border-purple-100/40">
          {/* Left: Logo text */}
          <div className="flex items-center gap-2 mr-8">
            <span className="text-2xl">🦉</span>
            <div>
              <h1 className="text-lg font-extrabold gradient-text leading-tight">MathQuest</h1>
              <p className="text-[10px] text-gray-400 font-semibold -mt-0.5">Learn. Play. Win!</p>
            </div>
          </div>

          {/* Center: Level + XP Bar */}
          <div className="flex-1 flex items-center justify-center max-w-md mx-auto">
            <div className="flex items-center gap-3 w-full">
              <div className="bg-gradient-to-r from-secondary-500 to-secondary-600 text-white text-xs font-extrabold px-3 py-1 rounded-full shadow-md whitespace-nowrap">
                LVL {stats.level}
              </div>
              <div className="flex-1">
                <div className="h-4 bg-gray-100 rounded-full overflow-hidden relative">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${xpPercent}%` }}
                    transition={{ duration: 1, ease: 'easeOut' }}
                    className="h-full bg-gradient-to-r from-secondary-400 to-purple-500 rounded-full relative"
                  >
                    <div className="absolute inset-0 bg-white/20 rounded-full" style={{
                      background: 'repeating-linear-gradient(90deg, transparent, transparent 8px, rgba(255,255,255,0.15) 8px, rgba(255,255,255,0.15) 16px)'
                    }} />
                  </motion.div>
                  <span className="absolute inset-0 flex items-center justify-center text-[10px] font-bold text-gray-600">
                    {stats.xp} / {stats.xpMax} XP
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Right: Stats + Avatar */}
          <div className="flex items-center gap-3 ml-8">
            {/* Streak */}
            <motion.div
              whileHover={{ scale: 1.1 }}
              className="flex items-center gap-1.5 bg-orange-50 text-orange-600 px-3 py-1.5 rounded-full font-bold text-sm cursor-default"
            >
              <span className="text-base">🔥</span>
              <span>{stats.streak}</span>
            </motion.div>

            {/* Stars */}
            <motion.div
              whileHover={{ scale: 1.1 }}
              className="flex items-center gap-1.5 bg-yellow-50 text-yellow-600 px-3 py-1.5 rounded-full font-bold text-sm cursor-default"
            >
              <span className="text-base">⭐</span>
              <span>{stats.stars}</span>
            </motion.div>

            {/* Coins */}
            <motion.div
              whileHover={{ scale: 1.1 }}
              className="flex items-center gap-1.5 bg-pink-50 text-pink-600 px-3 py-1.5 rounded-full font-bold text-sm cursor-default"
            >
              <span className="text-base">🪙</span>
              <span>{stats.coins}</span>
            </motion.div>

            {/* Avatar */}
            <div className="flex items-center gap-2 ml-2 pl-3 border-l border-gray-200">
              <div className="w-9 h-9 rounded-full bg-gradient-to-br from-primary-400 to-secondary-500 flex items-center justify-center text-white font-bold text-sm shadow-md">
                {(user?.name || 'S')[0].toUpperCase()}
              </div>
              <span className="text-sm font-bold text-gray-700 hidden lg:block">
                {user?.name || 'Student'}
              </span>
            </div>
          </div>
        </header>

        {/* Page Content */}
        <main className="pt-20 pb-8 px-6 relative z-10">
          <motion.div
            key={location.pathname}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.2 }}
          >
            <Outlet />
          </motion.div>
        </main>
      </div>
    </div>
  )
}
