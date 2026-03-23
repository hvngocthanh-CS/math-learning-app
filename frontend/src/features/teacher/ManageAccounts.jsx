import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { FaUserPlus, FaSpinner, FaKey, FaCopy, FaCheck, FaTrash } from 'react-icons/fa'
import toast from 'react-hot-toast'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.08 },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

function generatePassword() {
  const chars = 'abcdefghijkmnpqrstuvwxyz23456789'
  let password = ''
  for (let i = 0; i < 8; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length))
  }
  return password
}

export default function ManageAccounts() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [role, setRole] = useState('student')
  const [creating, setCreating] = useState(false)

  const [users, setUsers] = useState([])
  const [loadingUsers, setLoadingUsers] = useState(true)
  const [filter, setFilter] = useState('all')
  const [copiedId, setCopiedId] = useState(null)
  const [deletingId, setDeletingId] = useState(null)

  const fetchUsers = async () => {
    setLoadingUsers(true)
    try {
      let url = '/users'
      if (filter === 'student') url = '/users?role=student'
      if (filter === 'parent') url = '/users?role=parent'
      const response = await api.get(url)
      const data = response.data
      setUsers(Array.isArray(data) ? data : data.users || [])
    } catch (err) {
      toast.error('Failed to load users')
      console.error(err)
    } finally {
      setLoadingUsers(false)
    }
  }

  useEffect(() => {
    fetchUsers()
  }, [filter])

  const handleAutoGenerate = () => {
    const generated = generatePassword()
    setPassword(generated)
    toast.success('Password generated: ' + generated)
  }

  const handleCopyCredentials = (text) => {
    navigator.clipboard.writeText(text)
    toast.success('Copied to clipboard!')
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!name.trim() || !email.trim() || !password.trim()) {
      toast.error('Please fill in all fields')
      return
    }

    setCreating(true)
    try {
      await api.post('/users/create', {
        name: name.trim(),
        email: email.trim(),
        password,
        role,
      })

      toast.success(
        (t) => (
          <div className="max-w-sm">
            <p className="font-bold text-green-700 mb-2">Account created successfully!</p>
            <div className="bg-gray-50 rounded-lg p-3 text-sm space-y-1">
              <div className="flex items-center justify-between">
                <span className="text-gray-500">Name:</span>
                <span className="font-semibold text-gray-800">{name}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-500">Email:</span>
                <span className="font-semibold text-gray-800">{email}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-500">Password:</span>
                <span className="font-semibold text-gray-800">{password}</span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-gray-500">Role:</span>
                <span className="font-semibold text-gray-800 capitalize">{role}</span>
              </div>
            </div>
            <button
              onClick={() => {
                handleCopyCredentials(
                  `Name: ${name}\nEmail: ${email}\nPassword: ${password}\nRole: ${role}`
                )
                toast.dismiss(t.id)
              }}
              className="mt-3 w-full flex items-center justify-center gap-2 bg-orange-500 text-white text-sm font-bold py-2 rounded-lg hover:bg-orange-600 transition-colors"
            >
              <FaCopy /> Copy Credentials
            </button>
          </div>
        ),
        { duration: 15000 }
      )

      // Reset form
      setName('')
      setEmail('')
      setPassword('')
      setRole('student')

      // Refresh user list
      fetchUsers()
    } catch (err) {
      const message = err.response?.data?.detail || err.response?.data?.message || 'Failed to create account'
      toast.error(message)
    } finally {
      setCreating(false)
    }
  }

  const handleDeleteUser = async (userId, userName) => {
    if (!window.confirm(`Are you sure you want to delete "${userName}"? This action cannot be undone.`)) {
      return
    }
    setDeletingId(userId)
    try {
      await api.delete(`/users/${userId}`)
      toast.success(`"${userName}" has been deleted.`)
      fetchUsers()
    } catch (err) {
      toast.error(err.response?.data?.detail || 'Failed to delete user')
    } finally {
      setDeletingId(null)
    }
  }

  const filterTabs = [
    { key: 'all', label: 'All' },
    { key: 'student', label: 'Students' },
    { key: 'parent', label: 'Parents' },
  ]

  const roleBadge = (userRole) => {
    if (userRole === 'student') {
      return (
        <span className="bg-pink-100 text-pink-600 text-xs font-bold px-2.5 py-0.5 rounded-full">
          Student
        </span>
      )
    }
    if (userRole === 'parent') {
      return (
        <span className="bg-blue-100 text-blue-600 text-xs font-bold px-2.5 py-0.5 rounded-full">
          Parent
        </span>
      )
    }
    return (
      <span className="bg-gray-100 text-gray-600 text-xs font-bold px-2.5 py-0.5 rounded-full capitalize">
        {userRole}
      </span>
    )
  }

  const formatDate = (dateStr) => {
    if (!dateStr) return '-'
    const d = new Date(dateStr)
    return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
  }

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="max-w-7xl mx-auto space-y-8"
    >
      {/* Page Header */}
      <motion.div variants={item}>
        <h1 className="text-3xl font-extrabold text-gray-800">Manage Accounts</h1>
        <p className="text-gray-500 mt-1">Create and manage student and parent accounts.</p>
      </motion.div>

      {/* Create Account Form */}
      <motion.div variants={item}>
        <div className="bg-white rounded-2xl shadow-md border border-gray-100 p-6">
          <div className="flex items-center gap-3 mb-6">
            <div className="w-10 h-10 bg-orange-100 rounded-xl flex items-center justify-center">
              <FaUserPlus className="text-orange-500" />
            </div>
            <h2 className="text-xl font-extrabold text-gray-800">Create New Account</h2>
          </div>

          <form onSubmit={handleSubmit} className="space-y-5">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
              {/* Name */}
              <div>
                <label className="block text-sm font-bold text-gray-600 mb-1.5">Full Name</label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="Enter full name"
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
                />
              </div>

              {/* Email */}
              <div>
                <label className="block text-sm font-bold text-gray-600 mb-1.5">Email</label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="Enter email address"
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
                />
              </div>

              {/* Password */}
              <div>
                <label className="block text-sm font-bold text-gray-600 mb-1.5">Password</label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Enter password"
                    className="flex-1 px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
                  />
                  <motion.button
                    type="button"
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={handleAutoGenerate}
                    className="px-4 py-3 bg-gray-100 hover:bg-gray-200 rounded-xl text-sm font-bold text-gray-600 transition-colors flex items-center gap-2 whitespace-nowrap"
                  >
                    <FaKey className="text-xs" /> Auto
                  </motion.button>
                </div>
              </div>

              {/* Role */}
              <div>
                <label className="block text-sm font-bold text-gray-600 mb-1.5">Role</label>
                <select
                  value={role}
                  onChange={(e) => setRole(e.target.value)}
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium bg-white"
                >
                  <option value="student">Student</option>
                  <option value="parent">Parent</option>
                </select>
              </div>
            </div>

            <motion.button
              type="submit"
              disabled={creating}
              whileHover={{ scale: creating ? 1 : 1.02 }}
              whileTap={{ scale: creating ? 1 : 0.98 }}
              className="flex items-center justify-center gap-2 bg-orange-500 hover:bg-orange-600 disabled:bg-orange-300 text-white font-bold px-8 py-3 rounded-xl shadow-md shadow-orange-200 transition-colors"
            >
              {creating ? (
                <>
                  <FaSpinner className="animate-spin" /> Creating...
                </>
              ) : (
                <>
                  <FaUserPlus /> Create Account
                </>
              )}
            </motion.button>
          </form>
        </div>
      </motion.div>

      {/* User List */}
      <motion.div variants={item}>
        <div className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden">
          {/* Header + Filter Tabs */}
          <div className="p-6 pb-0">
            <h2 className="text-xl font-extrabold text-gray-800 mb-4">User List</h2>
            <div className="flex gap-1 border-b border-gray-100">
              {filterTabs.map((tab) => (
                <button
                  key={tab.key}
                  onClick={() => setFilter(tab.key)}
                  className={`px-5 py-2.5 text-sm font-bold transition-all border-b-2 -mb-px ${
                    filter === tab.key
                      ? 'border-orange-500 text-orange-600'
                      : 'border-transparent text-gray-400 hover:text-gray-600'
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>
          </div>

          {/* Table */}
          <div className="p-6 pt-4">
            {loadingUsers ? (
              <div className="flex items-center justify-center py-16">
                <FaSpinner className="animate-spin text-3xl text-orange-400" />
              </div>
            ) : users.length === 0 ? (
              <div className="text-center py-16">
                <div className="text-5xl mb-4">📋</div>
                <p className="text-gray-400 font-semibold">No users found</p>
                <p className="text-gray-300 text-sm mt-1">Create an account above to get started</p>
              </div>
            ) : (
              <div className="overflow-x-auto">
                <table className="w-full">
                  <thead>
                    <tr className="text-left">
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Name</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Email</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Role</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Level</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Stars</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Created</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-50">
                    {users.map((u) => (
                      <motion.tr
                        key={u._id || u.id}
                        whileHover={{ backgroundColor: 'rgba(249,250,251,1)' }}
                        className="transition-colors"
                      >
                        <td className="py-3.5">
                          <div className="flex items-center gap-3">
                            <div className="w-9 h-9 rounded-full bg-gradient-to-br from-orange-300 to-amber-400 flex items-center justify-center text-white font-bold text-sm">
                              {(u.name || '?')[0].toUpperCase()}
                            </div>
                            <span className="font-semibold text-gray-700 text-sm">{u.name}</span>
                          </div>
                        </td>
                        <td className="py-3.5 text-sm text-gray-500">{u.email}</td>
                        <td className="py-3.5">{roleBadge(u.role)}</td>
                        <td className="py-3.5 text-sm font-bold text-gray-600">{u.level ?? '-'}</td>
                        <td className="py-3.5 text-sm font-bold text-yellow-600">{u.stars ?? '-'}</td>
                        <td className="py-3.5 text-sm text-gray-400">{formatDate(u.createdAt || u.created_at)}</td>
                        <td className="py-3.5 text-right">
                          {u.role !== 'teacher' && (
                            <motion.button
                              whileHover={{ scale: 1.1 }}
                              whileTap={{ scale: 0.9 }}
                              onClick={() => handleDeleteUser(u.id || u._id, u.name)}
                              disabled={deletingId === (u.id || u._id)}
                              className="text-gray-300 hover:text-red-500 transition-colors disabled:opacity-50 p-2 rounded-lg hover:bg-red-50"
                              title={`Delete ${u.name}`}
                            >
                              {deletingId === (u.id || u._id) ? (
                                <FaSpinner className="animate-spin text-sm" />
                              ) : (
                                <FaTrash className="text-sm" />
                              )}
                            </motion.button>
                          )}
                        </td>
                      </motion.tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </motion.div>
    </motion.div>
  )
}
