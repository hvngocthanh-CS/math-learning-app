import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { motion } from 'framer-motion'
import toast from 'react-hot-toast'
import { useAuth } from './AuthContext'

export default function Register() {
  const navigate = useNavigate()
  const { register } = useAuth()
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [teacherCode, setTeacherCode] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (password !== confirmPassword) {
      toast.error('Passwords do not match!')
      return
    }

    if (password.length < 6) {
      toast.error('Password must be at least 6 characters!')
      return
    }

    if (!teacherCode.trim()) {
      toast.error('Please enter the teacher registration code!')
      return
    }

    setLoading(true)

    try {
      await register(name, email, password, 'teacher', teacherCode)
      toast.success('Account created! Please log in.')
      navigate('/login')
    } catch (err) {
      toast.error(err.response?.data?.detail || 'Registration failed. Please try again!')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex relative overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 math-pattern" />

      {/* Floating decorations */}
      <div className="absolute top-10 right-[10%] text-6xl opacity-5 animate-float text-primary-500">+</div>
      <div className="absolute bottom-[20%] left-[15%] text-5xl opacity-5 animate-float text-secondary-500" style={{ animationDelay: '1s' }}>x</div>

      {/* Left Side - Hero */}
      <div className="hidden lg:flex lg:w-5/12 gradient-hero flex-col justify-between p-12 text-white relative overflow-hidden">
        <div className="absolute -top-20 -left-20 w-60 h-60 bg-white/10 rounded-full" />
        <div className="absolute -bottom-32 -right-32 w-80 h-80 bg-white/5 rounded-full" />

        <div className="relative z-10">
          <Link to="/" className="flex items-center gap-3">
            <span className="text-4xl">🦉</span>
            <div>
              <h1 className="text-3xl font-extrabold">MathQuest</h1>
              <p className="text-sm opacity-80 font-semibold">Learn. Play. Win!</p>
            </div>
          </Link>
        </div>

        <div className="relative z-10">
          <h2 className="text-5xl font-extrabold mb-4 leading-tight">
            Teacher
            <br />
            Registration
          </h2>
          <p className="text-xl opacity-90 mb-10 max-w-md leading-relaxed">
            Create your teacher account to manage classes and create student & parent accounts.
          </p>

          <div className="space-y-4">
            <div className="flex items-center gap-4 p-4 bg-white/10 backdrop-blur-sm rounded-xl">
              <span className="text-2xl">👩‍🏫</span>
              <span className="font-bold">Create & manage student accounts</span>
            </div>
            <div className="flex items-center gap-4 p-4 bg-white/10 backdrop-blur-sm rounded-xl">
              <span className="text-2xl">👨‍👩‍👧</span>
              <span className="font-bold">Create & manage parent accounts</span>
            </div>
            <div className="flex items-center gap-4 p-4 bg-white/10 backdrop-blur-sm rounded-xl">
              <span className="text-2xl">📊</span>
              <span className="font-bold">Track student progress & performance</span>
            </div>
          </div>
        </div>

        <div className="relative z-10 text-sm opacity-60">
          MathQuest - Making Math Fun Since 2024
        </div>
      </div>

      {/* Right Side - Register Form */}
      <div className="w-full lg:w-7/12 flex items-center justify-center p-6 relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full max-w-lg"
        >
          <div className="bg-white rounded-3xl shadow-2xl p-8 border border-gray-100">
            {/* Mobile logo */}
            <div className="lg:hidden text-center mb-6">
              <span className="text-5xl">🦉</span>
              <h1 className="text-2xl font-extrabold gradient-text mt-2">MathQuest</h1>
            </div>

            {/* Header */}
            <h2 className="text-3xl font-extrabold text-gray-900 mb-1">
              Teacher Registration 👩‍🏫
            </h2>
            <p className="text-gray-500 mb-6 font-medium">
              Create your teacher account to get started
            </p>

            {/* Info box */}
            <div className="mb-6 p-4 bg-accent-50 rounded-xl border border-accent-200">
              <p className="text-sm font-bold text-accent-600">
                Only teachers can register here with a valid registration code. After registering, you can create accounts for your students and parents.
              </p>
            </div>

            {/* Form */}
            <form onSubmit={handleSubmit} className="space-y-4">
              {/* Name */}
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2">
                  Full Name
                </label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Enter your name"
                  className="input"
                  required
                />
              </div>

              {/* Teacher Code */}
              <div>
                <label className="block text-sm font-bold text-gray-700 mb-2">
                  Teacher Registration Code
                </label>
                <input
                  type="text"
                  value={teacherCode}
                  onChange={(e) => setTeacherCode(e.target.value)}
                  placeholder="Enter code provided by your school"
                  className="input"
                  required
                />
              </div>

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
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-sm font-bold text-gray-700 mb-2">
                    Password
                  </label>
                  <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Min 6 characters"
                    className="input"
                    required
                    minLength={6}
                  />
                </div>
                <div>
                  <label className="block text-sm font-bold text-gray-700 mb-2">
                    Confirm Password
                  </label>
                  <input
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    placeholder="Repeat password"
                    className="input"
                    required
                    minLength={6}
                  />
                </div>
              </div>

              {/* Submit */}
              <motion.button
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
                type="submit"
                disabled={loading}
                className="w-full bg-gradient-to-r from-accent-400 via-orange-500 to-primary-500 text-white font-extrabold py-3.5 rounded-xl shadow-lg shadow-accent-200 hover:shadow-xl transition-all disabled:opacity-50 text-lg"
              >
                {loading ? (
                  <span className="flex items-center justify-center gap-2">
                    <span className="animate-spin">🌀</span> Creating account...
                  </span>
                ) : (
                  'Create Teacher Account 👩‍🏫'
                )}
              </motion.button>
            </form>

            {/* Login Link */}
            <div className="mt-6 text-center">
              <span className="text-gray-500 font-medium">Already have an account? </span>
              <Link to="/login" className="text-primary-500 hover:text-primary-600 font-extrabold">
                Log In!
              </Link>
            </div>

            {/* Note */}
            <p className="mt-4 text-center text-xs text-gray-400 font-medium">
              🔒 Students & parents: please ask your teacher for login credentials.
            </p>
          </div>
        </motion.div>
      </div>
    </div>
  )
}
