import { motion } from 'framer-motion'

/**
 * SVG analog clock face with clear numbers, hour hand, and minute hand.
 * @param {number} hour - 1-12
 * @param {number} minute - 0 or 30
 * @param {number} size - pixel size (default 220)
 */
export default function ClockFace({ hour = 12, minute = 0, size = 220 }) {
  const cx = 100
  const cy = 100
  const radius = 88

  // Calculate hand angles (12 o'clock = 0 degrees, clockwise)
  const minuteAngle = (minute / 60) * 360
  // Hour hand moves continuously: at 3:30 it's between 3 and 4
  const hourAngle = ((hour % 12) / 12) * 360 + (minute / 60) * 30

  // Hand endpoints
  const hourLength = 50
  const minuteLength = 70
  const hourEnd = polarToXY(cx, cy, hourAngle, hourLength)
  const minuteEnd = polarToXY(cx, cy, minuteAngle, minuteLength)

  return (
    <motion.div
      initial={{ scale: 0.5, rotate: -15 }}
      animate={{ scale: 1, rotate: 0 }}
      transition={{ type: 'spring', stiffness: 200 }}
      className="inline-block"
    >
      <svg
        width={size}
        height={size}
        viewBox="0 0 200 200"
        className="drop-shadow-xl"
      >
        {/* Clock body */}
        <circle cx={cx} cy={cy} r={radius + 6} fill="#6366f1" />
        <circle cx={cx} cy={cy} r={radius} fill="white" stroke="#e5e7eb" strokeWidth="2" />

        {/* Tick marks */}
        {Array.from({ length: 60 }).map((_, i) => {
          const isHour = i % 5 === 0
          const angle = (i / 60) * 360
          const outerR = radius - 4
          const innerR = isHour ? radius - 14 : radius - 8
          const p1 = polarToXY(cx, cy, angle, outerR)
          const p2 = polarToXY(cx, cy, angle, innerR)
          return (
            <line
              key={i}
              x1={p1.x} y1={p1.y}
              x2={p2.x} y2={p2.y}
              stroke={isHour ? '#374151' : '#d1d5db'}
              strokeWidth={isHour ? 2.5 : 1}
              strokeLinecap="round"
            />
          )
        })}

        {/* Numbers */}
        {Array.from({ length: 12 }).map((_, i) => {
          const num = i + 1
          const angle = (num / 12) * 360
          const pos = polarToXY(cx, cy, angle, radius - 26)
          return (
            <text
              key={num}
              x={pos.x}
              y={pos.y}
              textAnchor="middle"
              dominantBaseline="central"
              className="select-none"
              style={{
                fontSize: '16px',
                fontWeight: 800,
                fill: '#1f2937',
                fontFamily: 'Nunito, sans-serif',
              }}
            >
              {num}
            </text>
          )
        })}

        {/* Minute hand */}
        <line
          x1={cx} y1={cy}
          x2={minuteEnd.x} y2={minuteEnd.y}
          stroke="#6366f1"
          strokeWidth="3.5"
          strokeLinecap="round"
        />

        {/* Hour hand */}
        <line
          x1={cx} y1={cy}
          x2={hourEnd.x} y2={hourEnd.y}
          stroke="#1f2937"
          strokeWidth="5"
          strokeLinecap="round"
        />

        {/* Center dot */}
        <circle cx={cx} cy={cy} r="5" fill="#6366f1" />
        <circle cx={cx} cy={cy} r="2.5" fill="white" />
      </svg>
    </motion.div>
  )
}

function polarToXY(cx, cy, angleDeg, r) {
  // 0 degrees = 12 o'clock, clockwise
  const rad = ((angleDeg - 90) * Math.PI) / 180
  return {
    x: cx + r * Math.cos(rad),
    y: cy + r * Math.sin(rad),
  }
}
