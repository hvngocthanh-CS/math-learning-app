/**
 * Client-side math problem generator for Play games.
 * Generates grade-appropriate problems with multiple-choice answers.
 */

function randInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min
}

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

function makeChoices(answer, count = 4, minVal = 0, spread = 5) {
  const choices = new Set([answer])
  let attempts = 0
  while (choices.size < count && attempts < 50) {
    const offset = randInt(1, spread) * (Math.random() < 0.5 ? -1 : 1)
    const val = answer + offset
    if (val >= minVal && val !== answer) choices.add(val)
    attempts++
  }
  // fallback
  let fallback = 1
  while (choices.size < count) {
    if (answer + fallback >= minVal) choices.add(answer + fallback)
    if (choices.size < count && answer - fallback >= minVal) choices.add(answer - fallback)
    fallback++
  }
  return shuffle([...choices].slice(0, count))
}

// ── Grade 1: addition/subtraction within 20 ──
function grade1() {
  const ops = ['+', '-']
  const op = ops[randInt(0, 1)]
  let a, b, answer
  if (op === '+') {
    a = randInt(1, 10)
    b = randInt(1, 10)
    answer = a + b
  } else {
    a = randInt(5, 18)
    b = randInt(1, a)
    answer = a - b
  }
  return { question: `${a} ${op} ${b}`, answer, choices: makeChoices(answer, 4, 0, 4) }
}

// ── Grade 2: +/- within 100, simple multiplication ──
function grade2() {
  const r = Math.random()
  let a, b, answer, question
  if (r < 0.4) {
    a = randInt(10, 50)
    b = randInt(5, 40)
    answer = a + b
    question = `${a} + ${b}`
  } else if (r < 0.7) {
    a = randInt(20, 80)
    b = randInt(5, a)
    answer = a - b
    question = `${a} - ${b}`
  } else {
    a = randInt(2, 5)
    b = randInt(2, 9)
    answer = a * b
    question = `${a} × ${b}`
  }
  return { question, answer, choices: makeChoices(answer, 4, 0, 8) }
}

// ── Grade 3: all 4 ops within 100, multi-digit addition ──
function grade3() {
  const r = Math.random()
  let a, b, answer, question
  if (r < 0.25) {
    a = randInt(50, 500)
    b = randInt(50, 400)
    answer = a + b
    question = `${a} + ${b}`
  } else if (r < 0.5) {
    a = randInt(100, 800)
    b = randInt(50, a)
    answer = a - b
    question = `${a} - ${b}`
  } else if (r < 0.75) {
    a = randInt(2, 9)
    b = randInt(2, 9)
    answer = a * b
    question = `${a} × ${b}`
  } else {
    b = randInt(2, 9)
    answer = randInt(2, 10)
    a = b * answer
    question = `${a} ÷ ${b}`
  }
  return { question, answer, choices: makeChoices(answer, 4, 0, 10) }
}

// ── Grade 4: multi-digit multiply, division with remainder, larger numbers ──
function grade4() {
  const r = Math.random()
  let a, b, answer, question
  if (r < 0.3) {
    a = randInt(11, 30)
    b = randInt(2, 9)
    answer = a * b
    question = `${a} × ${b}`
  } else if (r < 0.55) {
    b = randInt(3, 9)
    answer = randInt(5, 12)
    a = b * answer
    question = `${a} ÷ ${b}`
  } else if (r < 0.8) {
    a = randInt(100, 500)
    b = randInt(50, 300)
    answer = a + b
    question = `${a} + ${b}`
  } else {
    a = randInt(200, 800)
    b = randInt(50, a - 10)
    answer = a - b
    question = `${a} - ${b}`
  }
  return { question, answer, choices: makeChoices(answer, 4, 0, 15) }
}

// ── Grade 5: mixed ops, larger multiply/divide, percentages ──
function grade5() {
  const r = Math.random()
  let a, b, answer, question
  if (r < 0.25) {
    a = randInt(12, 25)
    b = randInt(3, 12)
    answer = a * b
    question = `${a} × ${b}`
  } else if (r < 0.45) {
    b = randInt(3, 12)
    answer = randInt(5, 20)
    a = b * answer
    question = `${a} ÷ ${b}`
  } else if (r < 0.65) {
    a = randInt(200, 999)
    b = randInt(100, 500)
    answer = a + b
    question = `${a} + ${b}`
  } else if (r < 0.85) {
    a = randInt(300, 999)
    b = randInt(100, a - 10)
    answer = a - b
    question = `${a} - ${b}`
  } else {
    // simple percentage
    const pct = [10, 20, 25, 50][randInt(0, 3)]
    const base = pct === 25 ? randInt(2, 10) * 4 : pct === 50 ? randInt(2, 20) * 2 : randInt(2, 15) * 10
    answer = base * pct / 100
    question = `${pct}% of ${base}`
  }
  return { question, answer, choices: makeChoices(answer, 4, 0, 15) }
}

const generators = { 1: grade1, 2: grade2, 3: grade3, 4: grade4, 5: grade5 }

export function generateProblem(grade = 1) {
  const gen = generators[grade] || grade1
  return gen()
}

export function generateProblems(grade, count = 10) {
  return Array.from({ length: count }, () => generateProblem(grade))
}
