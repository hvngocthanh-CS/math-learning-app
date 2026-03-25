import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FaBook, FaGamepad, FaTrophy, FaStar, FaHeart, FaUsers } from 'react-icons/fa'

const features = [
  {
    icon: <FaBook className="text-3xl" />,
    emoji: '📚',
    title: 'Learn',
    description: 'Fun, interactive math lessons designed for kids. Step-by-step guides with colorful visuals!',
    color: 'from-pink-400 to-rose-500',
    bg: 'bg-pink-50',
  },
  {
    icon: <FaGamepad className="text-3xl" />,
    emoji: '🎮',
    title: 'Play',
    description: 'Math games that make learning feel like play! Challenge friends and earn rewards.',
    color: 'from-secondary-400 to-purple-500',
    bg: 'bg-indigo-50',
  },
  {
    icon: <FaTrophy className="text-3xl" />,
    emoji: '🏆',
    title: 'Achieve',
    description: 'Earn stars, unlock badges, and climb the leaderboard. Every step counts!',
    color: 'from-accent-400 to-yellow-500',
    bg: 'bg-orange-50',
  },
  {
    icon: <FaUsers className="text-3xl" />,
    emoji: '👨‍👩‍👧‍👦',
    title: 'Parent Tracking',
    description: 'Parents can monitor and track their children\'s learning progress, scores, and achievements in real time.',
    color: 'from-teal-400 to-cyan-500',
    bg: 'bg-teal-50',
  },
]

const stats = [
  { value: '10K+', label: 'Happy Students', emoji: '😊' },
  { value: '500+', label: 'Fun Lessons', emoji: '📖' },
  { value: '50+', label: 'Math Games', emoji: '🎯' },
  { value: '98%', label: 'Love It!', emoji: '❤️' },
]

export default function Landing() {
  return (
    <div className="min-h-screen bg-white">
      {/* Navbar */}
      <nav className="fixed top-0 left-0 right-0 bg-white/80 backdrop-blur-md z-50 border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <Link to="/" className="flex items-center gap-2">
            <span className="text-3xl">🦉</span>
            <span className="text-2xl font-extrabold gradient-text">MathQuest</span>
          </Link>
          <div className="flex items-center gap-4">
            <Link
              to="/login"
              className="text-gray-600 hover:text-gray-900 font-semibold transition-colors"
            >
              Log In
            </Link>
            <Link
              to="/register"
              className="btn btn-primary text-sm !py-2 !px-5"
            >
              Get Started
            </Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="pt-32 pb-20 relative overflow-hidden">
        {/* Background decorations */}
        <div className="absolute inset-0 math-pattern" />
        <div className="absolute top-20 left-10 text-6xl opacity-10 animate-float">+</div>
        <div className="absolute top-40 right-20 text-5xl opacity-10 animate-float" style={{ animationDelay: '1s' }}>x</div>
        <div className="absolute bottom-20 left-1/4 text-4xl opacity-10 animate-float" style={{ animationDelay: '2s' }}>=</div>
        <div className="absolute top-32 right-1/3 text-3xl opacity-10 animate-float" style={{ animationDelay: '0.5s' }}>%</div>

        <div className="max-w-7xl mx-auto px-6 relative">
          <div className="flex flex-col lg:flex-row items-center gap-12">
            {/* Left: Text */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6 }}
              className="flex-1 text-center lg:text-left"
            >
              <div className="inline-flex items-center gap-2 bg-primary-50 text-primary-500 px-4 py-2 rounded-full font-bold text-sm mb-6">
                <FaStar className="text-yellow-400" />
                #1 Math Learning App for Kids
              </div>
              <h1 className="text-5xl lg:text-7xl font-extrabold mb-6 leading-tight">
                Make Math{' '}
                <span className="gradient-text">Fun</span>
                <br />
                & <span className="gradient-text">Magical!</span>{' '}
                <span className="inline-block animate-wiggle">✨</span>
              </h1>
              <p className="text-xl text-gray-500 mb-8 max-w-lg mx-auto lg:mx-0 leading-relaxed">
                Join thousands of kids who love learning math with MathQuest!
                Interactive lessons, exciting games, and awesome rewards.
              </p>
              <div className="flex flex-col sm:flex-row items-center gap-4 justify-center lg:justify-start">
                <Link to="/register">
                  <motion.button
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    className="btn btn-primary text-lg !px-8 !py-4"
                  >
                    Start Learning Free 🚀
                  </motion.button>
                </Link>
                <a href="#features">
                  <motion.button
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    className="btn bg-white text-gray-700 border-2 border-gray-200 hover:border-primary-300 hover:text-primary-500 text-lg !px-8 !py-4"
                  >
                    Learn More 📖
                  </motion.button>
                </a>
              </div>
            </motion.div>

            {/* Right: Hero visual */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ duration: 0.6, delay: 0.2 }}
              className="flex-1 flex justify-center"
            >
              <div className="relative">
                <div className="w-80 h-80 lg:w-96 lg:h-96 gradient-hero rounded-3xl flex items-center justify-center shadow-2xl shadow-primary-200">
                  <div className="text-center text-white">
                    <div className="text-8xl lg:text-9xl mb-4 animate-float">🦉</div>
                    <p className="text-2xl font-extrabold">MathQuest</p>
                    <p className="text-sm opacity-80 mt-1">Learn. Play. Win!</p>
                  </div>
                </div>
                {/* Floating badges */}
                <motion.div
                  animate={{ y: [-5, 5, -5] }}
                  transition={{ duration: 2, repeat: Infinity }}
                  className="absolute -top-4 -right-4 bg-white rounded-2xl shadow-lg p-3 flex items-center gap-2"
                >
                  <span className="text-2xl">⭐</span>
                  <span className="font-bold text-gray-700">+50 XP</span>
                </motion.div>
                <motion.div
                  animate={{ y: [5, -5, 5] }}
                  transition={{ duration: 2.5, repeat: Infinity }}
                  className="absolute -bottom-4 -left-4 bg-white rounded-2xl shadow-lg p-3 flex items-center gap-2"
                >
                  <span className="text-2xl">🔥</span>
                  <span className="font-bold text-gray-700">7 Day Streak!</span>
                </motion.div>
                <motion.div
                  animate={{ y: [-3, 3, -3] }}
                  transition={{ duration: 3, repeat: Infinity }}
                  className="absolute top-1/2 -right-8 bg-white rounded-2xl shadow-lg p-3 flex items-center gap-2"
                >
                  <span className="text-2xl">🏆</span>
                  <span className="font-bold text-gray-700">#1</span>
                </motion.div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Stats Bar */}
      <section className="py-12 bg-gradient-to-r from-secondary-600 to-purple-600">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {stats.map((stat, i) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
                className="text-center text-white"
              >
                <div className="text-3xl mb-2">{stat.emoji}</div>
                <div className="text-3xl lg:text-4xl font-extrabold">{stat.value}</div>
                <div className="text-sm opacity-80 font-semibold mt-1">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center mb-16">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="text-4xl lg:text-5xl font-extrabold mb-4">
                Why Kids <span className="gradient-text">Love</span> MathQuest{' '}
                <FaHeart className="inline text-red-400" />
              </h2>
              <p className="text-xl text-gray-500 max-w-2xl mx-auto">
                We turned boring math into an exciting adventure! Here's how:
              </p>
            </motion.div>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, i) => (
              <motion.div
                key={feature.title}
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.15 }}
                whileHover={{ y: -8 }}
                className="bg-white rounded-3xl p-8 shadow-lg border border-gray-100 text-center group cursor-default"
              >
                <div className={`w-20 h-20 ${feature.bg} rounded-2xl flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform`}>
                  <span className="text-4xl">{feature.emoji}</span>
                </div>
                <h3 className="text-2xl font-extrabold mb-3 text-gray-800">{feature.title}</h3>
                <p className="text-gray-500 leading-relaxed">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            className="gradient-hero rounded-3xl p-12 lg:p-16 text-white relative overflow-hidden"
          >
            <div className="absolute top-4 left-8 text-4xl opacity-20 animate-float">+</div>
            <div className="absolute bottom-8 right-12 text-3xl opacity-20 animate-float" style={{ animationDelay: '1s' }}>x</div>
            <div className="relative z-10">
              <h2 className="text-4xl lg:text-5xl font-extrabold mb-4">
                Ready to Start? 🚀
              </h2>
              <p className="text-xl opacity-90 mb-8 max-w-xl mx-auto">
                Join MathQuest today and turn math into your superpower!
                It's free to get started.
              </p>
              <Link to="/register">
                <motion.button
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                  className="bg-white text-primary-500 font-extrabold text-lg px-10 py-4 rounded-2xl shadow-xl hover:shadow-2xl transition-all"
                >
                  Create Free Account ✨
                </motion.button>
              </Link>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-400 py-12">
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex flex-col md:flex-row items-center justify-between gap-6">
            <div className="flex items-center gap-2">
              <span className="text-2xl">🦉</span>
              <span className="text-xl font-extrabold text-white">MathQuest</span>
            </div>
            <div className="flex items-center gap-6 text-sm font-semibold">
              <a href="#" className="hover:text-white transition-colors">About</a>
              <a href="#" className="hover:text-white transition-colors">Privacy</a>
              <a href="#" className="hover:text-white transition-colors">Terms</a>
              <a href="#" className="hover:text-white transition-colors">Contact</a>
            </div>
            <p className="text-sm">Made with <FaHeart className="inline text-red-400" /> for kids everywhere</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
