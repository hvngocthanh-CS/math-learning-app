"""
Grade 4 curriculum for MathQuest.
3 chapters, 12 lessons total.
Builds on Grade 3 (numbers to 1000, multiplication facts, intro fractions).
"""

from app.features.learn.generators.common.helpers import fraction_svg

GRADE4_CHAPTERS = [
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 1: Roman Numerals and Word Problems
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Roman Numerals and Word Problems",
        "description": "Learn Roman numerals and solve word problems that make you think",
        "order": 1,
        "lessons": [
            {
                "title": "Roman Numerals: I, V, X",
                "description": "Learn the first three Roman numeral symbols",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Roman numerals are an ancient number system still used today — on clocks and in book chapters!\n\nLet's start with just three symbols:\nI = 1, V = 5, X = 10\n\nTo write numbers, put symbols side by side and ADD them:\nII = 1 + 1 = 2\nVII = 5 + 1 + 1 = 7\nXI = 10 + 1 = 11\nXV = 10 + 5 = 15\n\nSpecial trick: when I comes BEFORE V or X, you SUBTRACT it:\nIV = 5 - 1 = 4\nIX = 10 - 1 = 9",
                    "examples": [
                        {"visual": "III = 3", "text": "Three I's in a row. 1 + 1 + 1 = 3."},
                        {"visual": "VI = 6", "text": "V + I = 5 + 1 = 6."},
                        {"visual": "IV = 4", "text": "I before V means subtract: 5 - 1 = 4."},
                        {"visual": "XII = 12", "text": "X + I + I = 10 + 1 + 1 = 12."},
                    ],
                    "steps": [
                        "Learn just 3 symbols: I=1, V=5, X=10.",
                        "Read left to right. Add the values together.",
                        "If I comes BEFORE V or X → subtract it.",
                        "IV = 4 and IX = 9 — remember these two!",
                        "Example: VIII = 5 + 1 + 1 + 1 = 8.",
                    ],
                    "fun_fact": "Look at a clock with Roman numerals — the numbers I to XII are all written using just I, V, and X! That is the first 12 numbers.",
                    "problem_config": {
                        "type": "roman_numerals",
                        "params": {"min_val": 1, "max_val": 20},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Roman Numerals: L and C",
                "description": "Learn L=50 and C=100 to write bigger Roman numerals",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Now let's add two more symbols:\nL = 50, C = 100\n\nCombine them with I, V, X that you already know:\nLI = 50 + 1 = 51\nLX = 50 + 10 = 60\nLXXV = 50 + 10 + 10 + 5 = 75\n\nSubtraction rules:\nXL = 50 - 10 = 40 (X before L)\nXC = 100 - 10 = 90 (X before C)\n\nExample: XCIX = 90 + 9 = 99.",
                    "examples": [
                        {"visual": "L = 50", "text": "Just the letter L by itself means 50!"},
                        {"visual": "LV = 55", "text": "L + V = 50 + 5 = 55."},
                        {"visual": "XL = 40", "text": "X before L means subtract: 50 - 10 = 40."},
                        {"visual": "C = 100", "text": "Just the letter C by itself means 100!"},
                    ],
                    "steps": [
                        "Remember all 5 symbols: I=1, V=5, X=10, L=50, C=100.",
                        "Read from left to right and add the values.",
                        "XL = 40 (X before L = subtract).",
                        "XC = 90 (X before C = subtract).",
                        "Example: LXII = 50 + 10 + 2 = 62.",
                    ],
                    "fun_fact": "The year 2024 in Roman numerals is MMXXIV. Movie credits often show the year in Roman numerals — see if you can read them next time!",
                    "problem_config": {
                        "type": "roman_numerals",
                        "params": {"min_val": 1, "max_val": 100},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Addition Word Problems",
                "description": "Solve story problems that need careful thinking with addition",
                "order": 3,
                "xp_reward": 30,
                "content": {
                    "explanation": "Word problems need you to READ carefully and THINK before you calculate!\n\nTips for tricky word problems:\n1. Read the WHOLE problem first — do not start calculating immediately.\n2. Underline the important numbers.\n3. Ask: What is the question really asking?\n4. Some problems have extra information you do NOT need!\n5. Some problems need TWO steps to solve.\n\nExample: Ben has 45 stickers. He gets 20 from Mom and 15 from Dad. How many now?\nStep 1: Read and understand — we need the TOTAL stickers.\nStep 2: 45 + 20 + 15 = 80 stickers.",
                    "examples": [
                        {"visual": "📚", "text": "A library has 35 books on one shelf and 48 on another. 12 more arrive. Total? 35 + 48 + 12 = 95 books."},
                        {"visual": "🏫", "text": "There are 24 boys and 18 girls in a class. 7 new students join. How many now? 24 + 18 + 7 = 49 students."},
                        {"visual": "⭐", "text": "Mia earns 15 stars Monday, 22 Tuesday, and 18 Wednesday. Total? 15 + 22 + 18 = 55 stars."},
                        {"visual": "🍎", "text": "A farm picks 60 apples and 45 oranges. 30 more apples are picked. How many apples? Just 60 + 30 = 90 (ignore the oranges!)."},
                    ],
                    "steps": [
                        "Read the entire problem carefully.",
                        "Identify what the question is asking for.",
                        "Find the numbers that are relevant (ignore extra info!).",
                        "Decide: do you need one step or two?",
                        "Calculate, then re-read the question to make sure your answer makes sense.",
                    ],
                    "fun_fact": "Word problems have been used in math education for over 4,000 years! Ancient Egyptian students solved problems about bread, beer, and pyramid building.",
                    "problem_config": {
                        "type": "word_problem_think",
                        "params": {"min": 10, "max": 80, "ops": ["add"]},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Subtraction Word Problems",
                "description": "Solve story problems that need careful thinking with subtraction",
                "order": 4,
                "xp_reward": 30,
                "content": {
                    "explanation": "Subtraction word problems can be tricky because the clue words are not always obvious!\n\nCommon clue words:\n- 'left', 'remaining' → subtract\n- 'how many more' → subtract to find the difference\n- 'gave away', 'lost', 'spent' → subtract\n\nTwo-step problems:\nEmma has 80 stickers. She gives 25 to Liam and 15 to Mia. How many left?\nStep 1: 80 - 25 = 55\nStep 2: 55 - 15 = 40 stickers left.\n\nOr do it in one step: 80 - 25 - 15 = 40.",
                    "examples": [
                        {"visual": "🍪", "text": "A bakery has 90 cookies. They sell 35 in the morning and 28 in the afternoon. Left? 90 - 35 - 28 = 27 cookies."},
                        {"visual": "💰", "text": "Noah has $75. He spends $30 on a toy and $20 on books. Left? $75 - $30 - $20 = $25."},
                        {"visual": "🚌", "text": "A bus has 50 passengers. 18 get off at the first stop, 12 at the second. How many are still on? 50 - 18 - 12 = 20."},
                        {"visual": "🃏", "text": "Ava has 60 cards. She buys 25 more but gives 30 to a friend. How many now? 60 + 25 - 30 = 55 cards."},
                    ],
                    "steps": [
                        "Read the problem and find ALL the numbers.",
                        "Decide what to do with EACH number (add or subtract?).",
                        "Watch for two-step problems: solve one part at a time.",
                        "Mixed problems: some numbers are added, others subtracted.",
                        "Always check: does the answer make sense in the story?",
                    ],
                    "fun_fact": "The word 'subtract' comes from Latin: 'sub' means 'under' and 'trahere' means 'to pull'. So subtract literally means 'to pull from under' — you are pulling a number away!",
                    "problem_config": {
                        "type": "word_problem_think",
                        "params": {"min": 15, "max": 90, "ops": ["subtract", "mixed"]},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 2: Multiplication and Division
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Multiplication and Division",
        "description": "Multiply bigger numbers, learn division, and solve word problems",
        "order": 2,
        "lessons": [
            {
                "title": "Multiplying by 1-Digit Numbers",
                "description": "Multiply a two-digit number by a one-digit number",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "To multiply a two-digit number by a one-digit number, break the big number apart!\n\n23 × 4:\nBreak 23 into 20 + 3.\n20 × 4 = 80\n3 × 4 = 12\n80 + 12 = 92!\n\nThis trick works because multiplication distributes over addition. You can also do it column by column, just like addition.",
                    "examples": [
                        {"visual": "23 × 4 = 92", "text": "20×4=80, 3×4=12. Then 80+12=92."},
                        {"visual": "15 × 6 = 90", "text": "10×6=60, 5×6=30. Then 60+30=90."},
                        {"visual": "34 × 7 = 238", "text": "30×7=210, 4×7=28. Then 210+28=238."},
                        {"visual": "48 × 3 = 144", "text": "40×3=120, 8×3=24. Then 120+24=144."},
                    ],
                    "steps": [
                        "Break the two-digit number into tens and ones.",
                        "Multiply the tens part by the one-digit number.",
                        "Multiply the ones part by the one-digit number.",
                        "Add the two results together.",
                        "Example: 36 × 5 → 30×5=150, 6×5=30 → 150+30=180.",
                    ],
                    "fun_fact": "The method of breaking apart numbers to multiply is called the 'distributive property'. It was first described by ancient Greek mathematicians over 2,000 years ago!",
                    "problem_config": {
                        "type": "multi_digit_multiply",
                        "params": {"min_two": 11, "max_two": 49, "min_one": 2, "max_one": 9},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Basic Division",
                "description": "Divide numbers evenly with no remainders",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Division is splitting into equal groups. 24 ÷ 6 means: how many groups of 6 fit into 24?\n\nThink of it as the opposite of multiplication:\n6 × ? = 24 → 6 × 4 = 24 → so 24 ÷ 6 = 4!\n\nThe three parts of division:\n- Dividend: the number being divided (24)\n- Divisor: the number you divide by (6)\n- Quotient: the answer (4)",
                    "examples": [
                        {"visual": "24 ÷ 6 = 4", "text": "6 × 4 = 24, so 24 ÷ 6 = 4."},
                        {"visual": "45 ÷ 9 = 5", "text": "9 × 5 = 45, so 45 ÷ 9 = 5."},
                        {"visual": "72 ÷ 8 = 9", "text": "8 × 9 = 72, so 72 ÷ 8 = 9."},
                        {"visual": "56 ÷ 7 = 8", "text": "7 × 8 = 56, so 56 ÷ 7 = 8."},
                    ],
                    "steps": [
                        "Read the division: Dividend ÷ Divisor = Quotient.",
                        "Think: Divisor × ? = Dividend.",
                        "Use your multiplication facts to find the answer.",
                        "Check: multiply the quotient by the divisor. You should get the dividend!",
                        "Example: 63 ÷ 7 → think 7 × ? = 63 → 7 × 9 = 63 → answer is 9.",
                    ],
                    "fun_fact": "The ÷ symbol was first used in 1659 by a Swiss mathematician named Johann Rahn. Before that, people used a horizontal line (like a fraction) to show division!",
                    "problem_config": {
                        "type": "division_basic",
                        "params": {"max_divisor": 9, "max_quotient": 12},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Division with Remainders",
                "description": "Understand what happens when division is not exact",
                "order": 3,
                "xp_reward": 30,
                "content": {
                    "explanation": "Sometimes numbers do not divide evenly. The leftover is called a REMAINDER.\n\nLet's learn the vocabulary first:\n• QUOTIENT = the whole number answer (how many full groups you can make)\n• REMAINDER = the leftover (what does not fit into a full group)\n\nExample: 17 ÷ 5\nStep 1: How many full groups of 5 fit into 17? → 5 × 3 = 15. So the QUOTIENT is 3.\nStep 2: What is left over? → 17 - 15 = 2. So the REMAINDER is 2.\nWe write: 17 ÷ 5 = 3 R 2 (quotient 3, remainder 2).\n\nImportant rules:\n• The remainder is ALWAYS smaller than the divisor.\n• If the remainder equals or exceeds the divisor, increase the quotient by 1!",
                    "examples": [
                        {"visual": "17 ÷ 5 = 3 R 2", "text": "Quotient = 3 (because 5 × 3 = 15). Remainder = 17 - 15 = 2."},
                        {"visual": "23 ÷ 4 = 5 R 3", "text": "Quotient = 5 (because 4 × 5 = 20). Remainder = 23 - 20 = 3."},
                        {"visual": "29 ÷ 6 = 4 R 5", "text": "Quotient = 4 (because 6 × 4 = 24). Remainder = 29 - 24 = 5."},
                        {"visual": "10 ÷ 3 = 3 R 1", "text": "Quotient = 3 (because 3 × 3 = 9). Remainder = 10 - 9 = 1."},
                    ],
                    "steps": [
                        "The QUOTIENT is the whole number answer — how many full groups fit.",
                        "Find the biggest multiple of the divisor that fits into the dividend. That is the quotient.",
                        "The REMAINDER is the leftover: Dividend - (Divisor × Quotient) = Remainder.",
                        "The remainder must be LESS than the divisor. If not, increase the quotient!",
                        "Write: Dividend ÷ Divisor = Quotient R Remainder. Example: 17 ÷ 5 = 3 R 2.",
                    ],
                    "fun_fact": "Remainders are used in computer science for many things! For example, to check if a number is even, computers divide by 2 and check if the remainder is 0.",
                    "problem_config": {
                        "type": "division_remainder",
                        "params": {"max_divisor": 9, "max_dividend": 80},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Multiply & Divide Word Problems",
                "description": "Solve real-life stories using multiplication and division",
                "order": 4,
                "xp_reward": 30,
                "content": {
                    "explanation": "Word problems use multiplication and division in real-life situations!\n\nMultiplication clues: 'each', 'every', 'per', 'times', 'groups of'.\nDivision clues: 'share equally', 'split into', 'how many in each', 'how many groups'.\n\nExample (multiply): 8 bags, 12 apples each → 8 × 12 = 96 apples.\nExample (divide): 48 stickers shared among 6 friends → 48 ÷ 6 = 8 stickers each.",
                    "examples": [
                        {"visual": "🧁", "text": "A bakery makes 6 trays with 12 cupcakes each. Total? 6 × 12 = 72 cupcakes."},
                        {"visual": "🍬", "text": "60 candies shared among 5 kids. Each gets? 60 ÷ 5 = 12 candies."},
                        {"visual": "📖", "text": "Liam reads 8 pages per day for 9 days. Total pages? 8 × 9 = 72 pages."},
                        {"visual": "🪑", "text": "36 chairs arranged in rows of 4. How many rows? 36 ÷ 4 = 9 rows."},
                    ],
                    "steps": [
                        "Read the problem carefully — find the numbers.",
                        "Look for clue words: 'each/every/per' = multiply, 'share/split' = divide.",
                        "Decide: Are we finding a total (multiply) or splitting into groups (divide)?",
                        "Write the equation and solve.",
                        "Check: does your answer make sense in the story?",
                    ],
                    "fun_fact": "Shopkeepers use multiplication and division every day! When a store orders 24 boxes of 50 pencils, they multiply to know they have 1,200 pencils. When those pencils are shared among 30 shelves, they divide: 1,200 ÷ 30 = 40 per shelf.",
                    "problem_config": {
                        "type": "multiply_divide_word",
                        "params": {"min_factor": 3, "max_factor": 12},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 3: Fractions and Decimals
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Fractions and Decimals",
        "description": "Explore equivalent fractions, fraction operations, and introduction to decimals",
        "order": 3,
        "lessons": [
            {
                "title": "Equivalent Fractions",
                "description": "Find fractions that represent the same amount",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Equivalent fractions look different but mean the SAME amount!\n\n1/2 = 2/4 = 3/6 = 4/8 — they all mean half!\n\nThe secret: multiply (or divide) the top AND bottom by the SAME number.\n1/2 → multiply both by 2 → 2/4\n1/2 → multiply both by 3 → 3/6\n\nIf you cut a pizza in half, you get 1 out of 2 slices. But if you cut each half again, you get 2 out of 4 slices — still the same amount of pizza!",
                    "examples": [
                        {"visual": fraction_svg(1, 2) + fraction_svg(2, 4), "text": "1/2 = 2/4. Multiply top and bottom by 2."},
                        {"visual": fraction_svg(1, 3) + fraction_svg(2, 6), "text": "1/3 = 2/6. Multiply top and bottom by 2."},
                        {"visual": fraction_svg(2, 3) + fraction_svg(4, 6), "text": "2/3 = 4/6. Multiply top and bottom by 2."},
                        {"visual": fraction_svg(3, 4) + fraction_svg(6, 8), "text": "3/4 = 6/8. Multiply top and bottom by 2."},
                    ],
                    "steps": [
                        "Look at the two fractions.",
                        "Find what number you multiply the denominator by to get the other denominator.",
                        "Multiply the numerator by the SAME number.",
                        "Check: the two fractions should be equal!",
                        "Example: 1/3 = ?/6 → 3×2=6, so 1×2=2 → answer is 2/6.",
                    ],
                    "fun_fact": "The ancient Egyptians only used fractions with 1 on top (unit fractions). To write 2/5, they had to write it as 1/3 + 1/15. Equivalent fractions make our lives much easier!",
                    "problem_config": {
                        "type": "equivalent_fractions",
                        "params": {},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Adding Fractions (Same Denominator)",
                "description": "Add and subtract fractions with the same bottom number",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "When fractions have the SAME denominator, adding and subtracting is easy!\n\nJust add (or subtract) the numerators. The denominator stays the same.\n\n1/4 + 2/4 = 3/4 (1+2=3, keep the 4)\n5/6 - 2/6 = 3/6 (5-2=3, keep the 6)\n\nThink of it like pizza slices: if you have 1 slice out of 4, then someone gives you 2 more slices (same size), you now have 3 slices out of 4!",
                    "examples": [
                        {"visual": fraction_svg(1, 4) + fraction_svg(2, 4), "text": "1/4 + 2/4 = 3/4. Add numerators: 1+2=3. Keep denominator: 4."},
                        {"visual": fraction_svg(2, 6) + fraction_svg(3, 6), "text": "2/6 + 3/6 = 5/6. Add numerators: 2+3=5. Keep denominator: 6."},
                        {"visual": fraction_svg(5, 8) + fraction_svg(2, 8), "text": "5/8 - 2/8 = 3/8. Subtract numerators: 5-2=3. Keep denominator: 8."},
                        {"visual": fraction_svg(3, 4) + fraction_svg(1, 4), "text": "3/4 - 1/4 = 2/4. Subtract numerators: 3-1=2. Keep denominator: 4."},
                    ],
                    "steps": [
                        "Check: do both fractions have the SAME denominator?",
                        "If yes: add (or subtract) the numerators.",
                        "Keep the denominator the same — do NOT add the denominators!",
                        "Write the answer: new numerator / same denominator.",
                        "Example: 3/8 + 4/8 = 7/8 (NOT 7/16!).",
                    ],
                    "fun_fact": "Fractions are used in music! A whole note lasts 4 beats. A half note (1/2) lasts 2 beats. A quarter note (1/4) lasts 1 beat. Musicians add and subtract fractions to create rhythms!",
                    "problem_config": {
                        "type": "fraction_add_sub",
                        "params": {"denominators": [2, 3, 4, 6, 8]},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Introduction to Decimals",
                "description": "Learn about tenths and how to write decimals",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Decimals are another way to write fractions! The decimal point separates whole numbers from parts.\n\nThe first digit after the decimal point is the TENTHS place.\n0.1 = 1/10 (one tenth)\n0.5 = 5/10 = 1/2 (five tenths = one half)\n2.3 = 2 and 3/10 (two and three tenths)\n\nThink of money: $2.50 means 2 dollars and 50 cents. The decimal point separates the dollars from the cents!",
                    "examples": [
                        {"visual": "0.1 = 1/10", "text": "One tenth. Like 1 slice of a bar divided into 10 equal parts."},
                        {"visual": "0.5 = 5/10", "text": "Five tenths. That is the same as 1/2 (one half)!"},
                        {"visual": "2.7 = 2 + 7/10", "text": "Two whole ones and seven tenths."},
                        {"visual": "3.0 = 3", "text": "Three and zero tenths. The .0 means there are no extra parts."},
                    ],
                    "steps": [
                        "Look at the number before the decimal point — that is the whole number part.",
                        "Look at the digit after the decimal point — that is the tenths.",
                        "1 tenth = 1/10 = 0.1",
                        "To convert a fraction to a decimal: 3/10 = 0.3",
                        "To convert a decimal to a fraction: 0.7 = 7/10",
                    ],
                    "fun_fact": "The decimal system was invented in ancient India and brought to Europe by Arab traders. The decimal point itself was first used by John Napier in 1617!",
                    "problem_config": {
                        "type": "decimals_identify",
                        "params": {"max_whole": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Comparing Decimals",
                "description": "Learn which decimals are bigger or smaller",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "Comparing decimals is like comparing whole numbers, but you go one step further!\n\nStep 1: Compare the whole number parts first.\n3.4 vs 2.8 → 3 > 2, so 3.4 > 2.8. Done!\n\nStep 2: If whole parts are the same, compare the tenths.\n5.3 vs 5.7 → same whole (5), but 3 < 7, so 5.3 < 5.7.\n\nRemember: 0.9 > 0.2 even though 9 and 2 are both less than 10!",
                    "examples": [
                        {"visual": "3.4 > 2.8", "text": "3 > 2 (whole parts). So 3.4 is bigger!"},
                        {"visual": "5.3 < 5.7", "text": "Same whole (5). Tenths: 3 < 7. So 5.3 < 5.7."},
                        {"visual": "1.0 < 1.5", "text": "Same whole (1). Tenths: 0 < 5. So 1.0 < 1.5."},
                        {"visual": "7.2 > 7.1", "text": "Same whole (7). Tenths: 2 > 1. So 7.2 > 7.1."},
                    ],
                    "steps": [
                        "Compare the WHOLE NUMBER parts first.",
                        "If one is bigger, that decimal is bigger. Done!",
                        "If whole parts are the SAME, compare the TENTHS digit.",
                        "Bigger tenths = bigger decimal.",
                        "Use > (greater), < (less), or = (equal).",
                    ],
                    "fun_fact": "Athletes are compared using decimals! In the 100-meter sprint, the difference between gold and silver can be just 0.01 seconds — that is one hundredth of a second!",
                    "problem_config": {
                        "type": "decimal_compare",
                        "params": {"max_whole": 9},
                        "count": 5,
                    },
                },
            },
        ],
    },
]
