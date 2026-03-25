import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { FaUserPlus, FaSpinner, FaKey, FaCopy, FaTrash, FaEdit, FaTimes, FaSave } from 'react-icons/fa'
import toast from 'react-hot-toast'
import api from '../../utils/api'

const container = {
  hidden: { opacity: 0 },
  show: { opacity: 1, transition: { staggerChildren: 0.08 } },
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

/* ── Edit Parent Modal ── */
function EditParentModal({ parent, students, allUsers, onClose, onSaved }) {
  const [editName, setEditName] = useState(parent.name)
  const [editEmail, setEditEmail] = useState(parent.email)
  const [editPassword, setEditPassword] = useState('')
  const [selectedStudentIds, setSelectedStudentIds] = useState([])
  const [saving, setSaving] = useState(false)

  // Students already linked to this parent
  const linkedStudents = allUsers.filter(
    (u) => u.role === 'student' && u.parent_id === parent.id
  )
  // Students not yet linked to any parent (available to add)
  const availableStudents = students.filter(
    (s) => !s.parent_id || s.parent_id === parent.id
  ).filter(
    (s) => !linkedStudents.some((ls) => ls.id === s.id)
  )

  const toggleStudent = (sid) => {
    setSelectedStudentIds((prev) =>
      prev.includes(sid) ? prev.filter((id) => id !== sid) : [...prev, sid]
    )
  }

  const handleSave = async () => {
    setSaving(true)
    try {
      const payload = {}
      if (editName.trim() !== parent.name) payload.name = editName.trim()
      if (editEmail.trim() !== parent.email) payload.email = editEmail.trim()
      if (editPassword.trim()) payload.password = editPassword.trim()
      if (selectedStudentIds.length > 0) payload.add_student_ids = selectedStudentIds

      if (Object.keys(payload).length === 0) {
        toast('No changes to save')
        onClose()
        return
      }

      await api.put(`/users/${parent.id}`, payload)
      toast.success('Parent updated successfully!')
      onSaved()
      onClose()
    } catch (err) {
      toast.error(err.response?.data?.detail || 'Failed to update')
    } finally {
      setSaving(false)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 bg-black/40 z-50 flex items-center justify-center p-4"
      onClick={onClose}
    >
      <motion.div
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        onClick={(e) => e.stopPropagation()}
        className="bg-white rounded-2xl shadow-2xl w-full max-w-lg max-h-[90vh] overflow-y-auto"
      >
        {/* Header */}
        <div className="flex items-center justify-between p-6 pb-4 border-b border-gray-100">
          <h2 className="text-xl font-extrabold text-gray-800">Edit Parent</h2>
          <button onClick={onClose} className="text-gray-300 hover:text-gray-500 transition-colors">
            <FaTimes className="text-lg" />
          </button>
        </div>

        <div className="p-6 space-y-5">
          {/* Name */}
          <div>
            <label className="block text-sm font-bold text-gray-600 mb-1.5">Name</label>
            <input
              type="text"
              value={editName}
              onChange={(e) => setEditName(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
            />
          </div>

          {/* Email */}
          <div>
            <label className="block text-sm font-bold text-gray-600 mb-1.5">Email</label>
            <input
              type="email"
              value={editEmail}
              onChange={(e) => setEditEmail(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
            />
          </div>

          {/* Password */}
          <div>
            <label className="block text-sm font-bold text-gray-600 mb-1.5">
              New Password <span className="text-gray-400 font-normal">(leave empty to keep current)</span>
            </label>
            <div className="flex gap-2">
              <input
                type="text"
                value={editPassword}
                onChange={(e) => setEditPassword(e.target.value)}
                placeholder="Enter new password"
                className="flex-1 px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium"
              />
              <button
                type="button"
                onClick={() => { const p = generatePassword(); setEditPassword(p); toast.success('Generated: ' + p) }}
                className="px-4 py-3 bg-gray-100 hover:bg-gray-200 rounded-xl text-sm font-bold text-gray-600 transition-colors flex items-center gap-2 whitespace-nowrap"
              >
                <FaKey className="text-xs" /> Auto
              </button>
            </div>
          </div>

          {/* Currently linked students */}
          {linkedStudents.length > 0 && (
            <div>
              <label className="block text-sm font-bold text-gray-600 mb-2">Linked Students</label>
              <div className="space-y-1.5">
                {linkedStudents.map((s) => (
                  <div key={s.id} className="flex items-center gap-2 px-3 py-2 bg-green-50 rounded-lg border border-green-100">
                    <div className="w-7 h-7 rounded-full bg-green-400 flex items-center justify-center text-white text-xs font-bold">
                      {s.name[0].toUpperCase()}
                    </div>
                    <span className="text-sm font-semibold text-gray-700 flex-1">{s.name}</span>
                    <span className="text-xs text-gray-400">{s.email}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Add more students */}
          {availableStudents.length > 0 && (
            <div>
              <label className="block text-sm font-bold text-gray-600 mb-2">Add Students</label>
              <div className="space-y-1.5 max-h-48 overflow-y-auto">
                {availableStudents.map((s) => {
                  const isSelected = selectedStudentIds.includes(s.id)
                  return (
                    <label
                      key={s.id}
                      className={`flex items-center gap-3 px-3 py-2.5 rounded-lg border cursor-pointer transition-all ${
                        isSelected
                          ? 'bg-orange-50 border-orange-300'
                          : 'bg-white border-gray-100 hover:border-gray-200'
                      }`}
                    >
                      <input
                        type="checkbox"
                        checked={isSelected}
                        onChange={() => toggleStudent(s.id)}
                        className="w-4 h-4 accent-orange-500 rounded"
                      />
                      <div className="w-7 h-7 rounded-full bg-gradient-to-br from-blue-400 to-cyan-400 flex items-center justify-center text-white text-xs font-bold">
                        {s.name[0].toUpperCase()}
                      </div>
                      <div className="flex-1 min-w-0">
                        <span className="text-sm font-semibold text-gray-700">{s.name}</span>
                        <span className="text-xs text-gray-400 ml-2">{s.email}</span>
                      </div>
                    </label>
                  )
                })}
              </div>
            </div>
          )}

          {availableStudents.length === 0 && linkedStudents.length === 0 && (
            <p className="text-sm text-gray-400 text-center py-4">No students available to link.</p>
          )}
        </div>

        {/* Footer */}
        <div className="flex items-center justify-end gap-3 p-6 pt-4 border-t border-gray-100">
          <button
            onClick={onClose}
            className="px-5 py-2.5 rounded-xl text-sm font-bold text-gray-500 hover:bg-gray-100 transition-colors"
          >
            Cancel
          </button>
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={handleSave}
            disabled={saving}
            className="flex items-center gap-2 px-6 py-2.5 bg-orange-500 hover:bg-orange-600 disabled:bg-orange-300 text-white font-bold text-sm rounded-xl shadow-md transition-colors"
          >
            {saving ? <FaSpinner className="animate-spin" /> : <FaSave />}
            {saving ? 'Saving...' : 'Save Changes'}
          </motion.button>
        </div>
      </motion.div>
    </motion.div>
  )
}

/* ── Main Component ── */
export default function ManageAccounts() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [role, setRole] = useState('student')
  const [studentIds, setStudentIds] = useState([])
  const [creating, setCreating] = useState(false)

  const [users, setUsers] = useState([])
  const [allUsers, setAllUsers] = useState([])
  const [students, setStudents] = useState([])
  const [loadingUsers, setLoadingUsers] = useState(true)
  const [filter, setFilter] = useState('all')
  const [deletingId, setDeletingId] = useState(null)
  const [editingParent, setEditingParent] = useState(null)

  const fetchStudents = () => {
    api.get('/users?role=student')
      .then((res) => {
        const data = res.data
        setStudents(Array.isArray(data) ? data : data.users || [])
      })
      .catch(() => {})
  }

  useEffect(() => { fetchStudents() }, [])

  const fetchUsers = async () => {
    setLoadingUsers(true)
    try {
      // Always fetch all users for parent-child linking info
      const allRes = await api.get('/users')
      const allData = allRes.data
      const all = Array.isArray(allData) ? allData : allData.users || []
      setAllUsers(all)

      if (filter === 'all') {
        setUsers(all)
      } else {
        setUsers(all.filter((u) => u.role === filter))
      }
    } catch (err) {
      toast.error('Failed to load users')
      console.error(err)
    } finally {
      setLoadingUsers(false)
    }
  }

  useEffect(() => { fetchUsers() }, [filter])

  const handleAutoGenerate = () => {
    const generated = generatePassword()
    setPassword(generated)
    toast.success('Password generated: ' + generated)
  }

  const handleCopyCredentials = (text) => {
    navigator.clipboard.writeText(text)
    toast.success('Copied to clipboard!')
  }

  const toggleCreateStudent = (sid) => {
    setStudentIds((prev) =>
      prev.includes(sid) ? prev.filter((id) => id !== sid) : [...prev, sid]
    )
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!name.trim() || !email.trim() || !password.trim()) {
      toast.error('Please fill in all fields')
      return
    }
    if (role === 'parent' && studentIds.length === 0) {
      toast.error('Please select at least one student to link with this parent')
      return
    }

    setCreating(true)
    try {
      const payload = {
        name: name.trim(),
        email: email.trim(),
        password,
        role,
      }
      if (role === 'parent' && studentIds.length > 0) {
        payload.student_ids = studentIds
      }
      await api.post('/users/create', payload)

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

      setName('')
      setEmail('')
      setPassword('')
      setRole('student')
      setStudentIds([])

      fetchUsers()
      fetchStudents()
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
      fetchStudents()
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
      return <span className="bg-pink-100 text-pink-600 text-xs font-bold px-2.5 py-0.5 rounded-full">Student</span>
    }
    if (userRole === 'parent') {
      return <span className="bg-blue-100 text-blue-600 text-xs font-bold px-2.5 py-0.5 rounded-full">Parent</span>
    }
    return <span className="bg-gray-100 text-gray-600 text-xs font-bold px-2.5 py-0.5 rounded-full capitalize">{userRole}</span>
  }

  const formatDate = (dateStr) => {
    if (!dateStr) return '-'
    return new Date(dateStr).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
  }

  // Get children names for a parent
  const getChildrenNames = (parentId) => {
    return allUsers
      .filter((u) => u.role === 'student' && u.parent_id === parentId)
      .map((u) => u.name)
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
              <div>
                <label className="block text-sm font-bold text-gray-600 mb-1.5">Role</label>
                <select
                  value={role}
                  onChange={(e) => { setRole(e.target.value); setStudentIds([]); }}
                  className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-orange-400 focus:ring-2 focus:ring-orange-100 outline-none transition-all text-sm font-medium bg-white"
                >
                  <option value="student">Student</option>
                  <option value="parent">Parent</option>
                </select>
              </div>
            </div>

            {/* Multi-select students when creating parent */}
            {role === 'parent' && (
              <div>
                <label className="block text-sm font-bold text-gray-600 mb-2">
                  Link to Students <span className="text-gray-400 font-normal">(select at least 1)</span>
                </label>
                {students.length === 0 ? (
                  <p className="text-sm text-gray-400">No students available. Create a student account first.</p>
                ) : (
                  <div className="space-y-1.5 max-h-48 overflow-y-auto border border-gray-100 rounded-xl p-3">
                    {students.filter((s) => !s.parent_id).map((s) => {
                      const isSelected = studentIds.includes(s.id)
                      return (
                        <label
                          key={s.id}
                          className={`flex items-center gap-3 px-3 py-2.5 rounded-lg border cursor-pointer transition-all ${
                            isSelected
                              ? 'bg-orange-50 border-orange-300'
                              : 'bg-white border-gray-50 hover:border-gray-200'
                          }`}
                        >
                          <input
                            type="checkbox"
                            checked={isSelected}
                            onChange={() => toggleCreateStudent(s.id)}
                            className="w-4 h-4 accent-orange-500 rounded"
                          />
                          <span className="text-sm font-semibold text-gray-700">{s.name}</span>
                          <span className="text-xs text-gray-400">({s.email})</span>
                        </label>
                      )
                    })}
                  </div>
                )}
              </div>
            )}

            <motion.button
              type="submit"
              disabled={creating}
              whileHover={{ scale: creating ? 1 : 1.02 }}
              whileTap={{ scale: creating ? 1 : 0.98 }}
              className="flex items-center justify-center gap-2 bg-orange-500 hover:bg-orange-600 disabled:bg-orange-300 text-white font-bold px-8 py-3 rounded-xl shadow-md shadow-orange-200 transition-colors"
            >
              {creating ? (
                <><FaSpinner className="animate-spin" /> Creating...</>
              ) : (
                <><FaUserPlus /> Create Account</>
              )}
            </motion.button>
          </form>
        </div>
      </motion.div>

      {/* User List */}
      <motion.div variants={item}>
        <div className="bg-white rounded-2xl shadow-md border border-gray-100 overflow-hidden">
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
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Children / Parent</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider">Created</th>
                      <th className="pb-3 text-xs font-bold text-gray-400 uppercase tracking-wider text-right">Actions</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-50">
                    {users.map((u) => {
                      const childrenNames = u.role === 'parent' ? getChildrenNames(u.id) : []
                      const parentUser = u.role === 'student' && u.parent_id
                        ? allUsers.find((p) => p.id === u.parent_id)
                        : null

                      return (
                        <motion.tr
                          key={u.id}
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
                          <td className="py-3.5 text-sm">
                            {u.role === 'parent' && childrenNames.length > 0 && (
                              <span className="text-blue-600 font-semibold">
                                {childrenNames.join(', ')}
                              </span>
                            )}
                            {u.role === 'parent' && childrenNames.length === 0 && (
                              <span className="text-gray-300 text-xs">No children linked</span>
                            )}
                            {u.role === 'student' && parentUser && (
                              <span className="text-green-600 font-semibold">{parentUser.name}</span>
                            )}
                            {u.role === 'student' && !parentUser && (
                              <span className="text-gray-300 text-xs">No parent</span>
                            )}
                            {u.role === 'teacher' && <span className="text-gray-300">-</span>}
                          </td>
                          <td className="py-3.5 text-sm text-gray-400">{formatDate(u.created_at)}</td>
                          <td className="py-3.5 text-right">
                            {u.role !== 'teacher' && (
                              <div className="flex items-center justify-end gap-1">
                                {u.role === 'parent' && (
                                  <motion.button
                                    whileHover={{ scale: 1.1 }}
                                    whileTap={{ scale: 0.9 }}
                                    onClick={() => setEditingParent(u)}
                                    className="text-gray-300 hover:text-blue-500 transition-colors p-2 rounded-lg hover:bg-blue-50"
                                    title={`Edit ${u.name}`}
                                  >
                                    <FaEdit className="text-sm" />
                                  </motion.button>
                                )}
                                <motion.button
                                  whileHover={{ scale: 1.1 }}
                                  whileTap={{ scale: 0.9 }}
                                  onClick={() => handleDeleteUser(u.id, u.name)}
                                  disabled={deletingId === u.id}
                                  className="text-gray-300 hover:text-red-500 transition-colors disabled:opacity-50 p-2 rounded-lg hover:bg-red-50"
                                  title={`Delete ${u.name}`}
                                >
                                  {deletingId === u.id ? (
                                    <FaSpinner className="animate-spin text-sm" />
                                  ) : (
                                    <FaTrash className="text-sm" />
                                  )}
                                </motion.button>
                              </div>
                            )}
                          </td>
                        </motion.tr>
                      )
                    })}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        </div>
      </motion.div>

      {/* Edit Parent Modal */}
      <AnimatePresence>
        {editingParent && (
          <EditParentModal
            parent={editingParent}
            students={students}
            allUsers={allUsers}
            onClose={() => setEditingParent(null)}
            onSaved={() => { fetchUsers(); fetchStudents(); }}
          />
        )}
      </AnimatePresence>
    </motion.div>
  )
}
