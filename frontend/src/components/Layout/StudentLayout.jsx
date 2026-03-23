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

export default function StudentLayout() {
  const { user, logout } = useAuth()
  const location = useLocation()
  const stats = mockStats
  const xpPercent = Math.round((stats.xp / stats.xpMax) * 100)

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Left Sidebar */}
      <aside className="fixed left-0 top-0 bottom-0 w-20 bg-white shadow-lg z-40 flex flex-col items-center py-6 border-r border-gray-100">
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
        <header className="fixed top-0 left-20 right-0 h-16 bg-white shadow-sm z-30 flex items-center px-6 border-b border-gray-100">
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
        <main className="pt-20 pb-8 px-6">
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
