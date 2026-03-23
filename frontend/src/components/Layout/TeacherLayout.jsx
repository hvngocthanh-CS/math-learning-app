import { NavLink, Outlet, useLocation } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaHome, FaUsers, FaUserPlus, FaSignOutAlt } from 'react-icons/fa'
import { useAuth } from '../../features/auth'

const sidebarItems = [
  { to: '/teacher', icon: FaHome, label: 'Dashboard', end: true },
  { to: '/teacher/students', icon: FaUsers, label: 'Students' },
  { to: '/teacher/accounts', icon: FaUserPlus, label: 'Accounts' },
]

export default function TeacherLayout() {
  const { user, logout } = useAuth()
  const location = useLocation()

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
          {sidebarItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.end}
              className="group"
            >
              {({ isActive }) => (
                <motion.div
                  whileHover={{ scale: 1.1 }}
                  whileTap={{ scale: 0.95 }}
                  className={`
                    w-14 h-14 rounded-2xl flex flex-col items-center justify-center gap-0.5 transition-all duration-200
                    ${isActive
                      ? 'bg-orange-500 text-white shadow-lg shadow-orange-200'
                      : 'text-gray-400 hover:bg-gray-100 hover:text-gray-600'
                    }
                  `}
                >
                  <item.icon className="text-lg" />
                  <span className="text-[10px] font-bold">{item.label}</span>
                </motion.div>
              )}
            </NavLink>
          ))}
        </nav>

        {/* Logout */}
        <motion.button
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.95 }}
          onClick={logout}
          className="w-14 h-14 rounded-2xl flex flex-col items-center justify-center gap-0.5 text-gray-400 hover:bg-red-50 hover:text-red-500 transition-all"
          title="Logout"
        >
          <FaSignOutAlt className="text-lg" />
          <span className="text-[10px] font-bold">Logout</span>
        </motion.button>
      </aside>

      {/* Main Area */}
      <div className="flex-1 ml-20">
        {/* Top Bar */}
        <header className="fixed top-0 left-20 right-0 h-16 bg-white shadow-sm z-30 flex items-center justify-between px-6 border-b border-gray-100">
          {/* Left: Logo text */}
          <div className="flex items-center gap-2">
            <span className="text-2xl">🦉</span>
            <div>
              <h1 className="text-lg font-extrabold text-gray-800 leading-tight">MathQuest</h1>
              <p className="text-[10px] text-gray-400 font-semibold -mt-0.5">Teacher Portal</p>
            </div>
          </div>

          {/* Right: User info */}
          <div className="flex items-center gap-3">
            <span className="bg-orange-100 text-orange-600 text-xs font-bold px-3 py-1 rounded-full">
              Teacher
            </span>
            <div className="flex items-center gap-2 pl-3 border-l border-gray-200">
              <div className="w-9 h-9 rounded-full bg-gradient-to-br from-orange-400 to-amber-500 flex items-center justify-center text-white font-bold text-sm shadow-md">
                {(user?.name || 'T')[0].toUpperCase()}
              </div>
              <span className="text-sm font-bold text-gray-700 hidden lg:block">
                {user?.name || 'Teacher'}
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
