import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import toast from 'react-hot-toast'
import { useAuth } from './AuthContext'

export default function Login() {
  const navigate = useNavigate()
  const { login } = useAuth()
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!email.trim()) {
      toast.error('Please enter your email address.')
      return
    }
    if (!password.trim()) {
      toast.error('Please enter your password.')
      return
    }

    setLoading(true)

    try {
      const user = await login(email, password)
      toast.success(`Welcome back! Let's learn! 🎉`)
      const redirectPath = `/${user.role || 'student'}`
      navigate(redirectPath)
    } catch (err) {
      toast.error(err.response?.data?.detail || 'Login failed. Please try again!')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex relative overflow-hidden">
      {/* Background math pattern */}
      <div className="absolute inset-0 math-pattern" />

      {/* Floating math symbols */}
      <div className="absolute top-10 left-[10%] text-6xl opacity-5 animate-float text-primary-500">+</div>
      <div className="absolute top-[30%] right-[15%] text-5xl opacity-5 animate-float text-secondary-500" style={{ animationDelay: '1s' }}>x</div>
      <div className="absolute bottom-[20%] left-[20%] text-4xl opacity-5 animate-float text-accent-400" style={{ animationDelay: '2s' }}>=</div>
      <div className="absolute top-[60%] right-[30%] text-3xl opacity-5 animate-float text-purple-500" style={{ animationDelay: '0.5s' }}>%</div>
      <div className="absolute bottom-10 right-[10%] text-5xl opacity-5 animate-float text-kid-green" style={{ animationDelay: '1.5s' }}>3</div>
      <div className="absolute top-[20%] left-[40%] text-4xl opacity-5 animate-float text-kid-yellow" style={{ animationDelay: '0.8s' }}>7</div>

      {/* Left Side - Hero */}
      <div className="hidden lg:flex lg:w-1/2 gradient-hero flex-col justify-between p-12 text-white relative overflow-hidden">
        {/* Decorative circles */}
        <div className="absolute -top-20 -left-20 w-60 h-60 bg-white/10 rounded-full" />
        <div className="absolute -bottom-32 -right-32 w-80 h-80 bg-white/5 rounded-full" />

        {/* Logo */}
        <div className="relative z-10">
          <Link to="/" className="flex items-center gap-3">
            <span className="text-4xl">🦉</span>
            <div>
              <h1 className="text-3xl font-extrabold">MathQuest</h1>
              <p className="text-sm opacity-80 font-semibold">Learn. Play. Win!</p>
            </div>
          </Link>
        </div>

        {/* Main Content */}
        <div className="relative z-10">
          <h2 className="text-5xl font-extrabold mb-4 leading-tight">
            Welcome Back,
            <br />
            Math Hero! 🦸
          </h2>
          <p className="text-xl opacity-90 mb-10 max-w-md leading-relaxed">
            Your math adventure is waiting! Jump back in and keep your streak alive!
          </p>

          {/* Features */}
          <div className="space-y-4">
            <div className="flex items-center gap-4 p-4 bg-white/10 backdrop-blur-sm rounded-xl">
              <span className="text-2xl">🎯</span>
              <span className="font-bold">Complete daily missions for bonus rewards</span>
            </div>
            <div className="flex items-center gap-4 p-4 bg-white/10 backdrop-blur-sm rounded-xl">
              <span className="text-2xl">🏆</span>
              <span className="font-bold">Climb the leaderboard and earn trophies</span>
            </div>
            <div className="flex items-center gap-4 p-4 bg-white/10 backdrop-blur-sm rounded-xl">
              <span className="text-2xl">⭐</span>
              <span className="font-bold">Unlock new levels and achievements</span>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="relative z-10 text-sm opacity-60">
          MathQuest - Making Math Fun Since 2024
        </div>
      </div>

      {/* Right Side - Login Form */}
      <div className="w-full lg:w-1/2 flex items-center justify-center p-6 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full max-w-md"
        >
          <div className="bg-white rounded-3xl shadow-2xl p-8 border border-gray-100">
            {/* Mobile logo */}
            <div className="lg:hidden text-center mb-6">
              <span className="text-5xl">🦉</span>
              <h1 className="text-2xl font-extrabold gradient-text mt-2">MathQuest</h1>
            </div>

            {/* Header */}
            <h2 className="text-3xl font-extrabold text-gray-900 mb-1">
              Welcome Back! 👋
            </h2>
            <p className="text-gray-500 mb-8 font-medium">
              Log in to continue your math adventure
            </p>

            {/* Form */}
            <form onSubmit={handleSubmit} noValidate className="space-y-5">
              {/* Email */}
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2">
                  Email Address
                </label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="your@email.com"
                  className="input"
                  required
                />
              </div>

              {/* Password */}
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2">
                  Password
                </label>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter your password"
                  className="input"
                  required
                />
              </div>

              {/* Forgot password */}
              <div className="flex items-center justify-end">
                <a href="#" className="text-sm text-primary-500 hover:text-primary-600 font-bold">
                  Forgot password?
                </a>
              </div>

              {/* Submit */}
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                type="submit"
                disabled={loading}
                className="w-full bg-gradient-to-r from-primary-400 via-purple-500 to-secondary-500 text-white font-extrabold py-3.5 rounded-xl shadow-lg shadow-primary-200 hover:shadow-xl transition-all disabled:opacity-50 text-lg"
              >
                {loading ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="animate-spin">🌀</span> Logging in...
                  </span>
                ) : (
                  'Log In 🚀'
                )}
              </motion.button>
            </form>

            {/* Teacher register link */}
            <div className="mt-6 text-center">
              <span className="text-gray-500 font-medium">Are you a teacher? </span>
              <Link to="/register" className="text-accent-500 hover:text-accent-600 font-extrabold">
                Register here
              </Link>
            </div>

            {/* Note for students/parents */}
            <p className="mt-3 text-center text-xs text-gray-400 font-medium">
              🔒 Students & parents: please ask your teacher for login credentials.
            </p>
          </div>
        </motion.div>
      </div>
    </div>
  )
}
