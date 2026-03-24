"""
Grade 3 curriculum for MathQuest.
4 chapters, 13 lessons total.
Builds on Grade 2 (numbers to 100, basic ×, +/− to 100) and extends to 1000.
"""

from app.features.learn.generators.common.helpers import fraction_svg

GRADE3_CHAPTERS = [
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 1: Numbers to 1000
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Numbers to 1000",
        "description": "Explore three-digit numbers: hundreds, tens, ones, and comparing",
        "order": 1,
        "lessons": [
            {
                "title": "Counting by 100s",
                "description": "Learn to count by hundreds up to 1000",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Counting by 100s is like counting by 10s but with bigger jumps! Instead of jumping 10 at a time, we jump 100: 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000.\n\nThink of it like stacking 100-dollar bills. Each stack has exactly 100 dollars, so you just count the stacks!\n\nWhen you count by 100s, every number ends in two zeros (00). This makes them easy to spot!",
                    "examples": [
                        {"visual": "💯 → 100", "text": "One group of one hundred. That is 100."},
                        {"visual": "💯💯💯 → 300", "text": "Three groups of one hundred. That is 300."},
                        {"visual": "💯💯💯💯💯 → 500", "text": "Five groups of one hundred. That is 500. Half of 1000!"},
                        {"visual": "💯💯💯💯💯💯💯💯💯💯 → 1000", "text": "Ten groups of one hundred. That is 1000!"},
                    ],
                    "steps": [
                        "Start at 100.",
                        "Add 100 each time: 100, 200, 300, 400...",
                        "Keep going until you reach 1000.",
                        "Notice: every number ends in 00!",
                        "Use your fingers — each finger is one group of 100.",
                    ],
                    "fun_fact": "There are 100 centimeters in 1 meter, and 1000 meters in 1 kilometer! When you walk about 10 blocks, that is roughly 1 kilometer.",
                    "problem_config": {
                        "type": "skip_counting",
                        "params": {"step": 100, "max": 1000},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Place Value: Hundreds, Tens, and Ones",
                "description": "Understand hundreds, tens, and ones in three-digit numbers",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Every three-digit number is made of HUNDREDS, TENS, and ONES. The first digit tells how many hundreds, the second tells how many tens, and the third tells how many ones.\n\nFor example, 365 has 3 hundreds, 6 tens, and 5 ones. That means 300 + 60 + 5 = 365.\n\nThink of it like money: 3 hundred-dollar bills, 6 ten-dollar bills, and 5 one-dollar coins!",
                    "examples": [
                        {"visual": "247 = 2️⃣ hundreds + 4️⃣ tens + 7️⃣ ones", "text": "247 = 200 + 40 + 7. Two hundreds, four tens, seven ones."},
                        {"visual": "508 = 5️⃣ hundreds + 0️⃣ tens + 8️⃣ ones", "text": "508 = 500 + 0 + 8. Five hundreds, zero tens, eight ones."},
                        {"visual": "730 = 7️⃣ hundreds + 3️⃣ tens + 0️⃣ ones", "text": "730 = 700 + 30 + 0. Seven hundreds, three tens, zero ones."},
                        {"visual": "999 = 9️⃣ hundreds + 9️⃣ tens + 9️⃣ ones", "text": "999 = 900 + 90 + 9. The biggest three-digit number!"},
                    ],
                    "steps": [
                        "Look at the three-digit number.",
                        "The FIRST (left) digit is the hundreds place.",
                        "The MIDDLE digit is the tens place.",
                        "The LAST (right) digit is the ones place.",
                        "Example: 426 → 4 hundreds (400) + 2 tens (20) + 6 ones (6) = 426.",
                    ],
                    "fun_fact": "The ancient Romans did not use place value like we do! They used letters like I, V, X, C, and M. The number 365 would be written as CCCLXV. Our system is much easier!",
                    "problem_config": {
                        "type": "place_value_hundreds",
                        "params": {"min": 101, "max": 999},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Comparing Numbers to 1000",
                "description": "Learn to compare three-digit numbers using > < and =",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Comparing three-digit numbers is just like comparing two-digit numbers, but we start by looking at the HUNDREDS first!\n\nRule 1: Compare hundreds first. 500 is always bigger than 400.\nRule 2: If hundreds are the same, compare tens. 350 > 320.\nRule 3: If hundreds AND tens are the same, compare ones. 351 > 350.\n\nRemember: > means 'greater than' and < means 'less than'.",
                    "examples": [
                        {"visual": "500 > 300", "text": "5 hundreds is more than 3 hundreds. 500 is greater!"},
                        {"visual": "472 < 489", "text": "Both have 4 hundreds. Tens: 7 < 8. So 472 < 489."},
                        {"visual": "635 > 631", "text": "Same hundreds (6) and tens (3). Ones: 5 > 1. So 635 > 631."},
                        {"visual": "250 = 250", "text": "Same hundreds, tens, and ones. They are equal!"},
                    ],
                    "steps": [
                        "Compare the HUNDREDS digit first.",
                        "If one has more hundreds, that number is bigger.",
                        "If hundreds are the same, compare TENS.",
                        "If tens are also the same, compare ONES.",
                        "Write > (greater), < (less), or = (equal).",
                    ],
                    "fun_fact": "The > and < symbols were invented by Thomas Harriot in 1631. He was a mathematician who also explored America with Sir Walter Raleigh!",
                    "problem_config": {
                        "type": "comparison_hundreds",
                        "params": {"min": 100, "max": 999},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 2: Addition and Subtraction to 1000
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Addition and Subtraction to 1000",
        "description": "Add and subtract three-digit numbers step by step",
        "order": 2,
        "lessons": [
            {
                "title": "Adding Three-Digit Numbers",
                "description": "Add two three-digit numbers without regrouping",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Adding three-digit numbers works the same as two-digit — just add each column from right to left!\n\nFor example: 324 + 251\nOnes: 4 + 1 = 5\nTens: 2 + 5 = 7\nHundreds: 3 + 2 = 5\nAnswer: 575!\n\nSometimes you need to carry (regroup). If ones add to 10 or more, carry 1 to tens. If tens add to 10 or more, carry 1 to hundreds.",
                    "examples": [
                        {"visual": "123 + 456 = 579", "text": "Ones: 3+6=9. Tens: 2+5=7. Hundreds: 1+4=5. Answer: 579."},
                        {"visual": "340 + 250 = 590", "text": "Ones: 0+0=0. Tens: 4+5=9. Hundreds: 3+2=5. Answer: 590."},
                        {"visual": "215 + 368 = 583", "text": "Ones: 5+8=13 (write 3, carry 1). Tens: 1+6+1=8. Hundreds: 2+3=5. Answer: 583."},
                        {"visual": "450 + 350 = 800", "text": "Ones: 0+0=0. Tens: 5+5=10 (write 0, carry 1). Hundreds: 4+3+1=8. Answer: 800."},
                    ],
                    "steps": [
                        "Line up the numbers by place value (ones under ones, etc.).",
                        "Add the ONES column first.",
                        "If the total is 10 or more, write the ones digit and carry 1.",
                        "Add the TENS column (include any carry).",
                        "Add the HUNDREDS column (include any carry).",
                    ],
                    "fun_fact": "The method of adding columns from right to left was developed by the ancient Indians and spread through the Arab world to Europe. It is over 1,500 years old!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 100, "max_a": 500, "min_b": 100, "max_b": 499, "max_sum": 999},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Subtracting Three-Digit Numbers",
                "description": "Subtract three-digit numbers with and without borrowing",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Subtracting three-digit numbers follows the same rules as smaller numbers. Start from the ones and work left!\n\nFor example: 587 - 234\nOnes: 7 - 4 = 3\nTens: 8 - 3 = 5\nHundreds: 5 - 2 = 3\nAnswer: 353!\n\nIf a digit on top is smaller, borrow from the next column: 403 - 158. Ones: 3 - 8? Borrow! 13 - 8 = 5. Tens: 9 - 5 = 4. Hundreds: 3 - 1 = 2. Answer: 245.",
                    "examples": [
                        {"visual": "789 - 456 = 333", "text": "Ones: 9-6=3. Tens: 8-5=3. Hundreds: 7-4=3. Answer: 333."},
                        {"visual": "500 - 200 = 300", "text": "5 hundreds - 2 hundreds = 3 hundreds = 300."},
                        {"visual": "634 - 218 = 416", "text": "Ones: 4-8? Borrow! 14-8=6. Tens: 2-1=1. Hundreds: 6-2=4. Answer: 416."},
                        {"visual": "900 - 350 = 550", "text": "Ones: 0-0=0. Tens: 0-5? Borrow! 10-5=5. Hundreds: 8-3=5. Answer: 550."},
                    ],
                    "steps": [
                        "Line up the numbers by place value.",
                        "Start with the ONES column.",
                        "If the top digit is smaller, borrow 1 from the tens.",
                        "Subtract the TENS column (remember if you borrowed!).",
                        "Subtract the HUNDREDS column.",
                    ],
                    "fun_fact": "Subtraction was one of the hardest operations for early computers! The first computers in the 1940s used a trick called 'complement arithmetic' to subtract, which is still used in computers today.",
                    "problem_config": {
                        "type": "subtraction",
                        "params": {"min_start": 200, "max_start": 999},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Rounding to the Nearest 10 and 100",
                "description": "Learn to round numbers to make estimation easier",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Rounding makes numbers simpler! Instead of saying exactly 247, you can round to 250 (nearest 10) or 200 (nearest 100).\n\nRounding to nearest 10: Look at the ones digit. If it is 0-4, round DOWN. If it is 5-9, round UP.\n247 → ones is 7 (5 or more) → round up → 250.\n\nRounding to nearest 100: Look at the tens digit. If it is 0-4, round DOWN. If it is 5-9, round UP.\n247 → tens is 4 (less than 5) → round down → 200.",
                    "examples": [
                        {"visual": "247 → 250 (nearest 10)", "text": "Ones digit is 7 (5 or more). Round UP to 250."},
                        {"visual": "123 → 120 (nearest 10)", "text": "Ones digit is 3 (less than 5). Round DOWN to 120."},
                        {"visual": "367 → 400 (nearest 100)", "text": "Tens digit is 6 (5 or more). Round UP to 400."},
                        {"visual": "820 → 800 (nearest 100)", "text": "Tens digit is 2 (less than 5). Round DOWN to 800."},
                    ],
                    "steps": [
                        "Decide: are you rounding to the nearest 10 or 100?",
                        "Look at the digit to the RIGHT of the place you are rounding to.",
                        "If that digit is 0, 1, 2, 3, or 4 → round DOWN.",
                        "If that digit is 5, 6, 7, 8, or 9 → round UP.",
                        "Replace all digits after the rounding place with zeros.",
                    ],
                    "fun_fact": "Scientists use rounding all the time! When NASA launches a rocket, they round many measurements to make quick calculations. But for the final launch, they use exact numbers!",
                    "problem_config": {
                        "type": "rounding",
                        "params": {"min": 101, "max": 999},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Word Problems to 1000",
                "description": "Solve real-life addition and subtraction stories with bigger numbers",
                "order": 4,
                "xp_reward": 30,
                "content": {
                    "explanation": "Word problems with bigger numbers work just the same! Read carefully, find the numbers, and decide whether to ADD or SUBTRACT.\n\nRemember the clue words:\nADDITION: 'in total', 'altogether', 'combined', 'how many in all'.\nSUBTRACTION: 'left', 'remaining', 'fewer', 'how many more', 'difference'.\n\nThe numbers are bigger, but the strategy is the same!",
                    "examples": [
                        {"visual": "📚", "text": "A library has 350 books. They buy 120 more. How many books now? → 350 + 120 = 470 books."},
                        {"visual": "🎈", "text": "A store had 500 balloons. They sold 175. How many are left? → 500 - 175 = 325 balloons."},
                        {"visual": "⭐", "text": "Emma collected 234 stickers. Liam collected 189. How many altogether? → 234 + 189 = 423 stickers."},
                        {"visual": "🍎", "text": "A farm picked 800 apples. 350 were sold. How many remain? → 800 - 350 = 450 apples."},
                    ],
                    "steps": [
                        "Read the story carefully — twice if needed!",
                        "Find the important numbers.",
                        "Look for clue words to decide: add or subtract?",
                        "Write the math equation and solve.",
                        "Check: does the answer make sense in the story?",
                    ],
                    "fun_fact": "The word 'problem' comes from the Greek word 'problema', which means 'something thrown forward'. Ancient Greek students had to solve math problems too!",
                    "problem_config": {
                        "type": "word_problem",
                        "params": {"min": 50, "max": 500, "max_result": 999},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 3: Multiplication Facts
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Multiplication Facts",
        "description": "Master multiplication tables and solve multiplication word problems",
        "order": 3,
        "lessons": [
            {
                "title": "Multiplication Tables: 2, 3, 4, 5",
                "description": "Learn multiplication facts for 2, 3, 4, and 5",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Multiplication is a shortcut for adding equal groups! Instead of writing 4 + 4 + 4, you write 3 × 4 = 12.\n\nThe × sign means 'groups of'. So 3 × 4 means '3 groups of 4'.\n\nTips: × 2 is just doubling! × 4 is double-double! × 5 always ends in 0 or 5!",
                    "examples": [
                        {"visual": "📋 Table of 2", "text": "2 × 1 = 2\n2 × 2 = 4\n2 × 3 = 6\n2 × 4 = 8\n2 × 5 = 10\n2 × 6 = 12\n2 × 7 = 14\n2 × 8 = 16\n2 × 9 = 18\n2 × 10 = 20"},
                        {"visual": "📋 Table of 3", "text": "3 × 1 = 3\n3 × 2 = 6\n3 × 3 = 9\n3 × 4 = 12\n3 × 5 = 15\n3 × 6 = 18\n3 × 7 = 21\n3 × 8 = 24\n3 × 9 = 27\n3 × 10 = 30"},
                        {"visual": "📋 Table of 4", "text": "4 × 1 = 4\n4 × 2 = 8\n4 × 3 = 12\n4 × 4 = 16\n4 × 5 = 20\n4 × 6 = 24\n4 × 7 = 28\n4 × 8 = 32\n4 × 9 = 36\n4 × 10 = 40"},
                        {"visual": "📋 Table of 5", "text": "5 × 1 = 5\n5 × 2 = 10\n5 × 3 = 15\n5 × 4 = 20\n5 × 5 = 25\n5 × 6 = 30\n5 × 7 = 35\n5 × 8 = 40\n5 × 9 = 45\n5 × 10 = 50"},
                    ],
                    "steps": [
                        "Read the multiplication: A × B means A groups of B.",
                        "You can skip count: for 4 × 3, count by 3s four times: 3, 6, 9, 12.",
                        "Or use repeated addition: 3 + 3 + 3 + 3 = 12.",
                        "Tip: Multiplying by 2 is the same as doubling!",
                        "Tip: Multiplying by 5 always ends in 0 or 5!",
                    ],
                    "fun_fact": "The multiplication symbol × was first used by William Oughtred in 1631. Before that, people used words or just wrote numbers next to each other!",
                    "problem_config": {
                        "type": "multiplication",
                        "params": {"tables": [2, 3, 4, 5], "max_factor": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Multiplication Tables: 6, 7, 8, 9, 10",
                "description": "Learn multiplication facts for 6 through 10",
                "order": 2,
                "xp_reward": 30,
                "content": {
                    "explanation": "Now let's learn the bigger multiplication tables! Remember: 6 × 3 is the same as 3 × 6, so you already know half the answers!\n\nTips: × 10 just adds a 0! × 9 digits always add to 9 (e.g. 9×3=27, 2+7=9)!",
                    "examples": [
                        {"visual": "📋 Table of 6", "text": "6 × 1 = 6\n6 × 2 = 12\n6 × 3 = 18\n6 × 4 = 24\n6 × 5 = 30\n6 × 6 = 36\n6 × 7 = 42\n6 × 8 = 48\n6 × 9 = 54\n6 × 10 = 60"},
                        {"visual": "📋 Table of 7", "text": "7 × 1 = 7\n7 × 2 = 14\n7 × 3 = 21\n7 × 4 = 28\n7 × 5 = 35\n7 × 6 = 42\n7 × 7 = 49\n7 × 8 = 56\n7 × 9 = 63\n7 × 10 = 70"},
                        {"visual": "📋 Table of 8", "text": "8 × 1 = 8\n8 × 2 = 16\n8 × 3 = 24\n8 × 4 = 32\n8 × 5 = 40\n8 × 6 = 48\n8 × 7 = 56\n8 × 8 = 64\n8 × 9 = 72\n8 × 10 = 80"},
                        {"visual": "📋 Table of 9", "text": "9 × 1 = 9\n9 × 2 = 18\n9 × 3 = 27\n9 × 4 = 36\n9 × 5 = 45\n9 × 6 = 54\n9 × 7 = 63\n9 × 8 = 72\n9 × 9 = 81\n9 × 10 = 90"},
                        {"visual": "📋 Table of 10", "text": "10 × 1 = 10\n10 × 2 = 20\n10 × 3 = 30\n10 × 4 = 40\n10 × 5 = 50\n10 × 6 = 60\n10 × 7 = 70\n10 × 8 = 80\n10 × 9 = 90\n10 × 10 = 100"},
                    ],
                    "steps": [
                        "For × 10: just add a 0 to the other number.",
                        "For × 9: the tens digit is one less, and digits add to 9.",
                        "For × 6, 7, 8: use facts you already know (flip the order!).",
                        "Example: 7 × 8 = 56. Think: 8 × 7. Count by 8s: 8, 16, 24, 32, 40, 48, 56.",
                        "Practice these facts — they will help you a lot in math!",
                    ],
                    "fun_fact": "The finger trick for 9s: hold up all 10 fingers. To find 9 × 3, put down finger #3. You see 2 fingers on the left and 7 on the right. The answer is 27!",
                    "problem_config": {
                        "type": "multiplication",
                        "params": {"tables": [6, 7, 8, 9, 10], "max_factor": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Multiplication Word Problems",
                "description": "Solve real-life stories using multiplication",
                "order": 3,
                "xp_reward": 30,
                "content": {
                    "explanation": "Multiplication word problems are about EQUAL GROUPS in real life!\n\nLook for clue words: 'each', 'every', 'per', 'groups of'.\n\nExample: 'There are 4 bags with 6 oranges each. How many oranges in total?'\nThis is 4 × 6 = 24 oranges!\n\nAnother clue: if the problem talks about ROWS and COLUMNS (like seats in a classroom), that is multiplication too! 5 rows of 8 seats = 5 × 8 = 40 seats.",
                    "examples": [
                        {"visual": "🍪", "text": "There are 3 plates with 7 cookies each. How many cookies? → 3 × 7 = 21 cookies."},
                        {"visual": "📚", "text": "A shelf has 5 rows of 8 books. How many books? → 5 × 8 = 40 books."},
                        {"visual": "🚗", "text": "Each car has 4 wheels. How many wheels on 6 cars? → 6 × 4 = 24 wheels."},
                        {"visual": "🎁", "text": "9 children each get 3 gifts. How many gifts in all? → 9 × 3 = 27 gifts."},
                    ],
                    "steps": [
                        "Read the story and find the two numbers.",
                        "Ask: Is this about equal groups?",
                        "Look for words like 'each', 'every', 'per', 'rows of'.",
                        "Write the multiplication: groups × items per group.",
                        "Solve and check your answer!",
                    ],
                    "fun_fact": "Multiplication is used to calculate the area of a room! A room that is 4 meters long and 3 meters wide has an area of 4 × 3 = 12 square meters.",
                    "problem_config": {
                        "type": "multiplication_word_problem",
                        "params": {"min_factor": 2, "max_factor": 10},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 4: Fractions and Geometry
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Fractions and Geometry",
        "description": "Discover fractions and learn about perimeter",
        "order": 4,
        "lessons": [
            {
                "title": "Introduction to Fractions",
                "description": "Learn about halves, thirds, and fourths",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "A fraction is a PART of a whole! When you cut a pizza into equal slices, each slice is a fraction of the whole pizza.\n\nA fraction has two numbers:\n- The TOP number (numerator) tells how many parts you HAVE.\n- The BOTTOM number (denominator) tells how many EQUAL parts the whole is divided into.\n\n1/2 = one half (cut into 2 equal pieces, take 1)\n1/3 = one third (cut into 3 equal pieces, take 1)\n1/4 = one fourth or one quarter (cut into 4 equal pieces, take 1)",
                    "examples": [
                        {"visual": fraction_svg(1, 2), "text": "Cut a pizza into 2 equal parts. Each part is 1/2 (one half)."},
                        {"visual": fraction_svg(2, 3), "text": "3 equal parts, 2 are colored. That is 2/3 (two thirds)."},
                        {"visual": fraction_svg(1, 4), "text": "4 equal parts, 1 is colored. That is 1/4 (one quarter)."},
                        {"visual": fraction_svg(3, 4), "text": "4 equal parts, 3 are colored. That is 3/4 (three quarters)."},
                    ],
                    "steps": [
                        "Count how many EQUAL parts the whole is divided into → that is the denominator (bottom).",
                        "Count how many parts are shaded or taken → that is the numerator (top).",
                        "Write it as: numerator / denominator.",
                        "1/2 means 1 out of 2 parts.",
                        "2/3 means 2 out of 3 parts.",
                    ],
                    "fun_fact": "The word 'fraction' comes from the Latin word 'fractio', which means 'to break'. Fractions are literally broken numbers!",
                    "problem_config": {
                        "type": "fraction_identify",
                        "params": {"denominators": [2, 3, 4]},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Comparing Fractions",
                "description": "Learn which fractions are bigger or smaller",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Comparing fractions is easy when the denominators are the same! Just compare the numerators.\n\n3/4 vs 1/4: Same denominator (4). 3 > 1, so 3/4 > 1/4. More slices = bigger fraction!\n\nWhen denominators are DIFFERENT, think about the size of each piece:\n1/2 vs 1/3: Half of a pizza is BIGGER than one third of a pizza. Fewer pieces means each piece is bigger! So 1/2 > 1/3.\n\nSmaller denominator = bigger pieces. Bigger denominator = smaller pieces.",
                    "examples": [
                        {"visual": fraction_svg(2, 4) + fraction_svg(3, 4), "text": "Same denominator. 2 < 3, so 2/4 < 3/4. Three quarters is more!"},
                        {"visual": fraction_svg(1, 2) + fraction_svg(1, 3), "text": "Half a pizza is bigger than a third. 1/2 > 1/3."},
                        {"visual": fraction_svg(2, 3) + fraction_svg(2, 4), "text": "Same numerator (2). Thirds are bigger than fourths. So 2/3 > 2/4."},
                        {"visual": fraction_svg(1, 4) + fraction_svg(1, 2), "text": "A quarter is smaller than a half. 1/4 < 1/2."},
                    ],
                    "steps": [
                        "If denominators are the SAME: compare numerators. Bigger numerator = bigger fraction.",
                        "If numerators are the SAME: compare denominators. Smaller denominator = bigger fraction.",
                        "Think of pizza! 1/2 of a pizza is more food than 1/4 of a pizza.",
                        "Fewer total slices → each slice is bigger.",
                        "Use > (greater than), < (less than), or = (equal).",
                    ],
                    "fun_fact": "The ancient Egyptians only used fractions with 1 on top (called unit fractions)! They would write 2/3 as 1/2 + 1/6. It was much harder!",
                    "problem_config": {
                        "type": "fraction_compare",
                        "params": {"denominators": [2, 3, 4, 6, 8]},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Perimeter of Shapes",
                "description": "Learn to find the distance around a shape",
                "order": 3,
                "xp_reward": 30,
                "content": {
                    "explanation": "The PERIMETER is the total distance around a shape. Imagine walking along the edges of a playground — the total distance you walk is the perimeter!\n\nTo find the perimeter, ADD UP all the sides.\n\nSquare: All 4 sides are equal. Perimeter = 4 × side.\nRectangle: 2 long sides + 2 short sides. Perimeter = 2 × length + 2 × width.\nTriangle: Add all 3 sides together.",
                    "examples": [
                        {"visual": "⬜ side = 5", "text": "Square with side 5. Perimeter = 5 + 5 + 5 + 5 = 20. Or 4 × 5 = 20."},
                        {"visual": "📱 6 × 4", "text": "Rectangle: length 6, width 4. Perimeter = 6 + 4 + 6 + 4 = 20. Or 2×6 + 2×4 = 20."},
                        {"visual": "🔺 3, 4, 5", "text": "Triangle with sides 3, 4, and 5. Perimeter = 3 + 4 + 5 = 12."},
                        {"visual": "⬜ side = 10", "text": "Square with side 10. Perimeter = 4 × 10 = 40."},
                    ],
                    "steps": [
                        "Identify the shape and its sides.",
                        "For a square: Perimeter = 4 × side length.",
                        "For a rectangle: Perimeter = 2 × length + 2 × width.",
                        "For a triangle: Perimeter = side1 + side2 + side3.",
                        "Add all the sides together to get the perimeter!",
                    ],
                    "fun_fact": "The word 'perimeter' comes from Greek: 'peri' means 'around' and 'meter' means 'measure'. So perimeter literally means 'measure around'!",
                    "problem_config": {
                        "type": "perimeter",
                        "params": {"shapes": ["square", "rectangle", "triangle"], "min_side": 2, "max_side": 15},
                        "count": 5,
                    },
                },
            },
        ],
    },
]
