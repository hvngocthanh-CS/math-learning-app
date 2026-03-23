"""
Grade 2 curriculum for MathQuest.
4 chapters, 17 lessons total.
Builds on Grade 1 (numbers to 20, basic +/−) and extends to 100.
"""

GRADE2_CHAPTERS = [
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 1: Numbers to 100
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Numbers to 100",
        "description": "Explore bigger numbers: skip counting, place value, even & odd",
        "order": 1,
        "lessons": [
            {
                "title": "Counting by 10s",
                "description": "Learn to count by tens up to 100",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Counting by 10s is like taking big jumps on the number line! Instead of counting 1, 2, 3... we jump: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.\n\nWhen you count by 10s, you add 10 each time. This is called skip counting. It helps you count big groups of things really fast!\n\nThink of it like counting stacks of 10 blocks. Each stack has exactly 10 blocks, so you just count the stacks!",
                    "examples": [
                        {"visual": "🔟 → 10", "text": "One group of ten. That is 10."},
                        {"visual": "🔟🔟🔟 → 30", "text": "Three groups of ten. That is 30."},
                        {"visual": "🔟🔟🔟🔟🔟 → 50", "text": "Five groups of ten. That is 50. Half of 100!"},
                        {"visual": "🔟🔟🔟🔟🔟🔟🔟🔟🔟🔟 → 100", "text": "Ten groups of ten. That is 100!"},
                    ],
                    "steps": [
                        "Start at 10.",
                        "Add 10 each time: 10, 20, 30, 40...",
                        "Keep going until you reach 100.",
                        "Notice: every number ends in 0!",
                        "Use your fingers - each finger is one group of 10.",
                    ],
                    "fun_fact": "There are exactly 100 cents in one dollar! When you count 10 dimes, you count by 10s: 10, 20, 30... up to 100 cents.",
                    "problem_config": {
                        "type": "skip_counting",
                        "params": {"step": 10, "max": 100},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Counting by 2s and 5s",
                "description": "Learn to skip count by 2s and 5s",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "We already know how to count by 10s. Now let's learn to count by 2s and 5s all the way up to 100!\n\nCounting by 2s: 2, 4, 6, 8, 10... all the way to 98, 100! We skip every other number. This is great for counting pairs like shoes or socks!\n\nCounting by 5s: 5, 10, 15, 20, 25... up to 95, 100! This is like counting the fingers on each hand. One hand = 5, two hands = 10!",
                    "examples": [
                        {"visual": "2, 4, 6, 8, 10", "text": "Counting by 2s from the start. Each number is 2 more than the last."},
                        {"visual": "40, 42, 44, 46, 48, 50", "text": "Counting by 2s with bigger numbers! Same rule: add 2 each time."},
                        {"visual": "5, 10, 15, 20, 25", "text": "Counting by 5s. Each number is 5 more than the last."},
                        {"visual": "55, 60, 65, 70, 75, 80", "text": "Counting by 5s with bigger numbers! Works the same way up to 100."},
                        {"visual": "96, 98, 100", "text": "Counting by 2s can reach 100! 96 + 2 = 98, 98 + 2 = 100."},
                        {"visual": "85, 90, 95, 100", "text": "Counting by 5s can reach 100 too! 85, 90, 95, 100."},
                    ],
                    "steps": [
                        "For counting by 2s: start at 2 and add 2 each time.",
                        "By 2s: 2, 4, 6, 8, 10... 50... 98, 100.",
                        "For counting by 5s: start at 5 and add 5 each time.",
                        "By 5s: 5, 10, 15, 20... 50... 95, 100.",
                        "Notice: counting by 5s always ends in 0 or 5!",
                    ],
                    "fun_fact": "When you look at a clock, the minute marks are counted by 5s! At the 1 it is 5 minutes, at the 2 it is 10 minutes, at the 3 it is 15 minutes.",
                    "problem_config": {
                        "type": "skip_counting",
                        "params": {"steps": [2, 5], "max": 100},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Place Value: Tens and Ones",
                "description": "Understand tens and ones in numbers up to 99",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Every two-digit number is made of tens and ones. The left digit tells you how many TENS, and the right digit tells you how many ONES.\n\nFor example, the number 35 has 3 tens and 5 ones. That means 30 + 5 = 35. The number 70 has 7 tens and 0 ones.\n\nUnderstanding place value is like a superpower - it helps you add and subtract big numbers!",
                    "examples": [
                        {"visual": "42 = 4️⃣ tens + 2️⃣ ones", "text": "42 has 4 tens (40) and 2 ones (2). 40 + 2 = 42."},
                        {"visual": "56 = 5️⃣ tens + 6️⃣ ones", "text": "56 has 5 tens (50) and 6 ones (6). 50 + 6 = 56."},
                        {"visual": "80 = 8️⃣ tens + 0️⃣ ones", "text": "80 has 8 tens and 0 ones. It is a round number!"},
                        {"visual": "99 = 9️⃣ tens + 9️⃣ ones", "text": "99 has 9 tens (90) and 9 ones (9). The biggest two-digit number!"},
                    ],
                    "steps": [
                        "Look at the two-digit number.",
                        "The LEFT digit is the tens place.",
                        "The RIGHT digit is the ones place.",
                        "Multiply the left digit by 10, then add the right digit.",
                        "Example: 73 → 7 tens (70) + 3 ones (3) = 73.",
                    ],
                    "fun_fact": "The number system we use is called 'base 10' because we group things in tens. Some ancient cultures counted in base 20 - using both fingers and toes!",
                    "problem_config": {
                        "type": "place_value",
                        "params": {"min": 21, "max": 99},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Even and Odd Numbers",
                "description": "Learn which numbers are even and which are odd",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "Numbers come in two types: EVEN and ODD.\n\nImagine you have some apples and TWO baskets 🧺🧺. Try putting one apple in each basket, taking turns. If every apple has a pair and both baskets have the same amount, the number is EVEN! If there is one apple left over with no basket to go to, the number is ODD.\n\nEven numbers can be split into 2 equal groups with nothing left over. The even numbers are: 2, 4, 6, 8, 10, 12, 14...\n\nOdd numbers always have 1 left over when you try to split them in half. The odd numbers are: 1, 3, 5, 7, 9, 11, 13...\n\nHere is an easy trick: look at the LAST digit. If it ends in 0, 2, 4, 6, or 8, it is even. If it ends in 1, 3, 5, 7, or 9, it is odd!",
                    "examples": [
                        {"visual": "🧺🍎🍎 🧺🍎🍎 → 4 is EVEN", "text": "4 apples are shared equally into 2 baskets. Each basket has 2. No apples left. 4 is even!"},
                        {"visual": "🧺🍎🍎 🧺🍎🍎 🍎❓ → 5 is ODD", "text": "5 apples are shared into 2 baskets. Each gets 2, but 1 is left. Not equal. 5 is odd!"},
                        {"visual": "🧺🍎🍎🍎 🧺🍎🍎🍎 → 6 is EVEN", "text": "6 apples are shared equally into 2 baskets. Each has 3. No apples left. 6 is even!"},
                        {"visual": "16 → ends in 6 → EVEN", "text": "16 ends in 6. Numbers ending in 0, 2, 4, 6, 8 are even."},
                        {"visual": "25 → ends in 5 → ODD", "text": "25 ends in 5. Numbers ending in 1, 3, 5, 7, 9 are odd."},
                        {"visual": "78 → ends in 8 → EVEN", "text": "78 ends in 8. Even! This trick works for big numbers too."},
                        {"visual": "93 → ends in 3 → ODD", "text": "93 ends in 3. Odd! Just look at the last digit."},
                        {"visual": "100 → ends in 0 → EVEN", "text": "100 ends in 0. Even! The biggest number we know so far is even."},
                    ],
                    "steps": [
                        "Look at the last digit of the number.",
                        "If the last digit is 0, 2, 4, 6, or 8 → the number is EVEN.",
                        "If the last digit is 1, 3, 5, 7, or 9 → the number is ODD.",
                        "This works for ALL numbers, even big ones like 78 or 99!",
                        "Even numbers can be shared equally between 2 people.",
                    ],
                    "fun_fact": "Zero is an even number! You can split 0 into two groups of 0 with nothing left over. Even mathematicians debated this for a long time!",
                    "problem_config": {
                        "type": "even_odd",
                        "params": {"min": 1, "max": 100},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 2: Addition and Subtraction to 100
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Addition and Subtraction to 100",
        "description": "Add and subtract bigger numbers with and without regrouping",
        "order": 2,
        "lessons": [
            {
                "title": "Adding Tens",
                "description": "Learn to add multiples of 10",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Adding tens is easy when you think of groups! If you know 3 + 2 = 5, then you also know 30 + 20 = 50. Just add a zero!\n\nThink of each ten as a bundle of 10 sticks. 30 is 3 bundles, and 20 is 2 bundles. Together that is 5 bundles, which is 50!\n\nThis works for any tens: 40 + 30 = 70 (because 4 + 3 = 7).",
                    "examples": [
                        {"visual": "10 + 20 = 30", "text": "1 ten + 2 tens = 3 tens = 30."},
                        {"visual": "30 + 40 = 70", "text": "3 tens + 4 tens = 7 tens = 70."},
                        {"visual": "50 + 50 = 100", "text": "5 tens + 5 tens = 10 tens = 100!"},
                        {"visual": "20 + 60 = 80", "text": "2 tens + 6 tens = 8 tens = 80."},
                    ],
                    "steps": [
                        "Look at the tens: 30 + 40.",
                        "Take away the zeros: 3 + 4.",
                        "Add the small numbers: 3 + 4 = 7.",
                        "Put the zero back: 70!",
                        "So 30 + 40 = 70.",
                    ],
                    "fun_fact": "Adding tens is the same trick calculators use to add big numbers - they break them into parts and add each part separately!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 10, "max_a": 90, "min_b": 10, "max_b": 90, "max_sum": 100, "tens_only": True},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Two-Digit + One-Digit",
                "description": "Add a one-digit number to a two-digit number",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Now let's add a small number to a big number! For example: 23 + 4.\n\nThe trick is to only change the ones place. The tens stay the same!\n23 + 4: The tens digit (2) stays. The ones: 3 + 4 = 7. So the answer is 27!\n\nBut be careful! Sometimes the ones add up to more than 9. For example: 27 + 5 = 32. The ones (7 + 5 = 12) carry over to the tens!",
                    "examples": [
                        {"visual": "34 + 5 = 39", "text": "Tens stay at 3. Ones: 4 + 5 = 9. Answer: 39."},
                        {"visual": "51 + 6 = 57", "text": "Tens stay at 5. Ones: 1 + 6 = 7. Answer: 57."},
                        {"visual": "45 + 8 = 53", "text": "Ones: 5 + 8 = 13. Write 3, carry 1 ten. 4 + 1 = 5 tens. Answer: 53."},
                        {"visual": "68 + 7 = 75", "text": "Ones: 8 + 7 = 15. Write 5, carry 1 ten. 6 + 1 = 7 tens. Answer: 75."},
                    ],
                    "steps": [
                        "Write the two-digit number and the one-digit number.",
                        "Add the ones digits together.",
                        "If the ones total is less than 10, the tens stay the same.",
                        "If the ones total is 10 or more, carry 1 to the tens.",
                        "Write the final answer!",
                    ],
                    "fun_fact": "The word 'carry' in math comes from how merchants used to move beads on an abacus - they literally carried a bead to the next column!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 11, "max_a": 89, "min_b": 2, "max_b": 9, "max_sum": 99},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Two-Digit + Two-Digit",
                "description": "Add two two-digit numbers together",
                "order": 3,
                "xp_reward": 30,
                "content": {
                    "explanation": "Adding two big numbers is like adding in two steps: first the ones, then the tens!\n\nFor example: 34 + 25.\nStep 1: Add the ones: 4 + 5 = 9.\nStep 2: Add the tens: 3 + 2 = 5.\nAnswer: 59!\n\nWhen the ones add up to 10 or more, remember to carry! 47 + 36: Ones: 7 + 6 = 13 (write 3, carry 1). Tens: 4 + 3 + 1 = 8. Answer: 83!",
                    "examples": [
                        {"visual": "23 + 15 = 38", "text": "Ones: 3+5=8. Tens: 2+1=3. Answer: 38."},
                        {"visual": "41 + 32 = 73", "text": "Ones: 1+2=3. Tens: 4+3=7. Answer: 73."},
                        {"visual": "36 + 47 = 83", "text": "Ones: 6+7=13 (write 3, carry 1). Tens: 3+4+1=8. Answer: 83."},
                        {"visual": "55 + 28 = 83", "text": "Ones: 5+8=13 (write 3, carry 1). Tens: 5+2+1=8. Answer: 83."},
                    ],
                    "steps": [
                        "Line up the two numbers by place value.",
                        "Add the ones column first.",
                        "If ones total ≥ 10, write the ones digit and carry 1 to tens.",
                        "Add the tens column (don't forget the carry!).",
                        "Write the final answer.",
                    ],
                    "fun_fact": "Before calculators were invented, people used to add big numbers on paper using the same carry method you just learned. This method is over 1,000 years old!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 11, "max_a": 60, "min_b": 11, "max_b": 50, "max_sum": 99},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Subtraction Within 100",
                "description": "Subtract one-digit and two-digit numbers from two-digit numbers",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "Subtraction with bigger numbers works just like with small numbers, but we go place by place!\n\nFor 58 − 23: Ones: 8 − 3 = 5. Tens: 5 − 2 = 3. Answer: 35!\n\nFor 74 − 6: Ones: 4 − 6... we can't! So we borrow 1 ten: 14 − 6 = 8. Tens: 7 − 1 = 6. Answer: 68.",
                    "examples": [
                        {"visual": "47 − 5 = 42", "text": "Ones: 7−5=2. Tens stay: 4. Answer: 42."},
                        {"visual": "86 − 34 = 52", "text": "Ones: 6−4=2. Tens: 8−3=5. Answer: 52."},
                        {"visual": "65 − 28 = 37", "text": "Ones: 5−8? Borrow! 15−8=7. Tens: 6−1−2=3. Answer: 37."},
                        {"visual": "90 − 40 = 50", "text": "9 tens − 4 tens = 5 tens = 50. Easy!"},
                    ],
                    "steps": [
                        "Start with the ones column.",
                        "If you can subtract, do it.",
                        "If the top number is smaller, borrow 1 ten (makes it +10 ones).",
                        "Now subtract the tens column (remember if you borrowed!).",
                        "Write the answer.",
                    ],
                    "fun_fact": "Ancient Egyptian mathematicians used subtraction to help build the pyramids! They calculated exactly how many stone blocks they needed by subtracting what they already had.",
                    "problem_config": {
                        "type": "subtraction",
                        "params": {"min_start": 20, "max_start": 99},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Word Problems",
                "description": "Solve real-life addition and subtraction stories",
                "order": 5,
                "xp_reward": 30,
                "content": {
                    "explanation": "Word problems are math stories! You need to read the story carefully, find the numbers, and decide whether to ADD or SUBTRACT.\n\nClue words for ADDITION: 'in total', 'altogether', 'more', 'how many in all', 'combined'.\n\nClue words for SUBTRACTION: 'left', 'remaining', 'fewer', 'how many more', 'took away'.\n\nAlways ask yourself: Is the answer getting BIGGER or SMALLER?",
                    "examples": [
                        {"visual": "🍎", "text": "Emma has 15 apples. Liam gives her 8 more. How many apples does Emma have now? → 15 + 8 = 23 apples."},
                        {"visual": "🎈", "text": "Noah has 24 balloons. 9 fly away. How many are left? → 24 − 9 = 15 balloons."},
                        {"visual": "📚", "text": "There are 32 books on one shelf and 18 on another. How many books altogether? → 32 + 18 = 50 books."},
                        {"visual": "🍬", "text": "Sophie had 40 candies. She gave 15 to friends. How many are left? → 40 − 15 = 25 candies."},
                    ],
                    "steps": [
                        "Read the story carefully.",
                        "Find the important numbers.",
                        "Look for clue words: 'more' and 'total' = add, 'left' and 'away' = subtract.",
                        "Write the math equation.",
                        "Solve and check: does the answer make sense?",
                    ],
                    "fun_fact": "Math word problems were used in ancient Babylon over 4,000 years ago! They wrote problems on clay tablets about sharing grain and building temples.",
                    "problem_config": {
                        "type": "word_problem",
                        "params": {"min": 2, "max": 50, "max_result": 80},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 3: Measurement and Time
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Measurement and Time",
        "description": "Compare sizes and learn to read clocks",
        "order": 3,
        "lessons": [
            {
                "title": "Comparing Sizes",
                "description": "Learn about bigger, smaller, taller, and shorter",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "We compare things every day! Is your toy car bigger or smaller than a real car? Is a giraffe taller or shorter than a cat?\n\nWhen we compare sizes, we use special words: bigger and smaller for overall size, taller and shorter for height, and longer and shorter for length.\n\nTo compare two things, put them side by side and look carefully. Which one takes up more space? That one is bigger!",
                    "examples": [
                        {"visual": "🐘 vs 🐭", "text": "An elephant is BIGGER than a mouse. A mouse is SMALLER."},
                        {"visual": "🌲 vs 🌱", "text": "A tree is TALLER than a seedling. A seedling is SHORTER."},
                        {"visual": "🚂 vs 🚗", "text": "A train is LONGER than a car. A car is SHORTER."},
                        {"visual": "🏀 vs ⚾", "text": "A basketball is BIGGER than a baseball."},
                    ],
                    "steps": [
                        "Look at both objects you want to compare.",
                        "Think about which one takes up more space.",
                        "The one that takes up more space is BIGGER.",
                        "The one that reaches higher is TALLER.",
                        "Use the right comparing word: bigger/smaller, taller/shorter, longer/shorter.",
                    ],
                    "fun_fact": "The tallest animal in the world is the giraffe! A baby giraffe is already about 6 feet tall when it is born - taller than most adult humans!",
                    "problem_config": {
                        "type": "size_comparison",
                        "params": {},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Telling Time: Hours",
                "description": "Learn to read a clock to the hour",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "A clock helps us know what time it is! A clock has two hands: a short hand and a long hand. The short hand tells us the HOUR, and the long hand tells us the MINUTES.\n\nWhen the long hand points straight up to the 12, it means the time is exactly on the hour. We look at where the short hand is pointing to know which hour it is.\n\nFor example, if the short hand points to 3 and the long hand points to 12, it is 3 o'clock!",
                    "examples": [
                        {"visual": "🕐 1:00", "text": "Short hand on 1, long hand on 12. It is 1 o'clock!"},
                        {"visual": "🕒 3:00", "text": "Short hand on 3, long hand on 12. It is 3 o'clock!"},
                        {"visual": "🕕 6:00", "text": "Short hand on 6, long hand on 12. It is 6 o'clock!"},
                        {"visual": "🕛 12:00", "text": "Both hands point to 12. It is 12 o'clock!"},
                    ],
                    "steps": [
                        "Look at the clock and find the two hands.",
                        "The SHORT hand is the hour hand.",
                        "The LONG hand is the minute hand.",
                        "If the long hand points to 12, it is exactly on the hour.",
                        "Read the number the short hand points to - that is the hour!",
                    ],
                    "fun_fact": "The oldest working clock in the world is in Salisbury Cathedral in England. It was built in the year 1386 - over 600 years ago!",
                    "problem_config": {
                        "type": "time_reading",
                        "params": {"hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Telling Time: Half Hours",
                "description": "Learn to read a clock at half past the hour",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Now that you can read the hour, let's learn about HALF PAST!\n\nWhen the long hand points straight down to the 6, it means half past the hour. Half an hour is 30 minutes - exactly halfway around the clock.\n\nAt half past 3 (3:30), the short hand is between 3 and 4, and the long hand points to 6. We write this as 3:30 and say 'three thirty' or 'half past three'.",
                    "examples": [
                        {"visual": "🕜 1:30", "text": "Long hand on 6, short hand between 1 and 2. It is 1:30 (half past 1)!"},
                        {"visual": "🕞 3:30", "text": "Long hand on 6, short hand between 3 and 4. It is 3:30!"},
                        {"visual": "🕡 6:30", "text": "Long hand on 6, short hand between 6 and 7. It is 6:30!"},
                        {"visual": "🕤 9:30", "text": "Long hand on 6, short hand between 9 and 10. It is 9:30!"},
                    ],
                    "steps": [
                        "Look at the LONG hand first.",
                        "If it points to 12 → the time is on the hour (:00).",
                        "If it points to 6 → the time is half past (:30).",
                        "Then look at the SHORT hand to find the hour.",
                        "Write the time: hour:00 or hour:30.",
                    ],
                    "fun_fact": "The word 'clock' comes from the Latin word 'clocca' which means 'bell'. The first clocks did not have faces - they just rang bells to tell the time!",
                    "problem_config": {
                        "type": "time_half_hour",
                        "params": {"hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 4: Patterns and Introduction to Multiplication
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Patterns and Introduction to Multiplication",
        "description": "Discover patterns and learn about groups and repeated addition",
        "order": 4,
        "lessons": [
            {
                "title": "Pattern Recognition",
                "description": "Find and continue ABAB patterns",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Patterns are things that repeat over and over! When you see something repeating in the same order, that is a pattern.\n\nThe simplest pattern is ABAB. This means two things take turns: red, blue, red, blue. Or circle, square, circle, square.\n\nLearning patterns helps your brain think about math in a special way. When you see a pattern, you can predict what comes next!",
                    "examples": [
                        {"visual": "🔴🔵🔴🔵🔴🔵", "text": "Red, Blue, Red, Blue - this is an ABAB pattern! Next is Red."},
                        {"visual": "⭐🌙⭐🌙⭐🌙", "text": "Star, Moon, Star, Moon - ABAB pattern! Next is Star."},
                        {"visual": "🍎🍌🍎🍌🍎", "text": "Apple, Banana, Apple, Banana, Apple - next is Banana!"},
                        {"visual": "🔺⬜🔺⬜🔺", "text": "Triangle, Square, Triangle, Square, Triangle - next is Square!"},
                    ],
                    "steps": [
                        "Look at the sequence of objects or shapes.",
                        "Find the part that repeats (the pattern unit).",
                        "In ABAB: A and B take turns.",
                        "Figure out where you are in the pattern.",
                        "Predict what comes next by continuing the pattern!",
                    ],
                    "fun_fact": "Patterns are everywhere in nature! Zebra stripes, honeycomb hexagons, and even the spiral of a seashell are all patterns.",
                    "problem_config": {
                        "type": "pattern",
                        "params": {},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Number Sequences",
                "description": "Find the missing number in a counting sequence",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Number sequences are patterns made with numbers! When numbers follow a rule, you can find the missing number.\n\nSome sequences count up by 1: 45, 46, _, 48, 49.\nSome count by other numbers: 20, 25, 30, _, 40 (counting by 5s!).\n\nThe trick is to find the pattern: how much does each number change?",
                    "examples": [
                        {"visual": "23, 24, _, 26", "text": "Counting by 1s. The missing number is 25."},
                        {"visual": "30, 40, _, 60", "text": "Counting by 10s. The missing number is 50."},
                        {"visual": "10, 15, 20, _", "text": "Counting by 5s. The next number is 25."},
                        {"visual": "52, 54, _, 58", "text": "Counting by 2s. The missing number is 56."},
                    ],
                    "steps": [
                        "Look at the numbers that are given.",
                        "Find the difference between two neighbors.",
                        "Check: is the same difference between all neighbors?",
                        "Use the pattern to find the missing number.",
                        "Double-check by counting forward and backward.",
                    ],
                    "fun_fact": "The great mathematician Carl Friedrich Gauss figured out how to add all numbers from 1 to 100 in seconds when he was just 10 years old. He found a pattern!",
                    "problem_config": {
                        "type": "number_sequence",
                        "params": {"min": 10, "max": 99},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Groups and Repeated Addition",
                "description": "Learn to count equal groups using repeated addition",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "When you have equal groups, you can count them using REPEATED ADDITION. This is the first step toward multiplication!\n\nIf you have 3 bags with 4 apples each, you can add: 4 + 4 + 4 = 12.\nThat is the same as 3 groups of 4!\n\nInstead of counting every single apple, you can add the groups. This is much faster!",
                    "examples": [
                        {"visual": "(🍎🍎) (🍎🍎) (🍎🍎)", "text": "3 groups of 2 apples. 2 + 2 + 2 = 6 apples!"},
                        {"visual": "(🌟🌟🌟) (🌟🌟🌟)", "text": "2 groups of 3 stars. 3 + 3 = 6 stars!"},
                        {"visual": "(🍪🍪🍪🍪) (🍪🍪🍪🍪) (🍪🍪🍪🍪)", "text": "3 groups of 4 cookies. 4 + 4 + 4 = 12 cookies!"},
                        {"visual": "(🐟🐟🐟🐟🐟) (🐟🐟🐟🐟🐟)", "text": "2 groups of 5 fish. 5 + 5 = 10 fish!"},
                    ],
                    "steps": [
                        "Count how many GROUPS there are.",
                        "Count how many are IN EACH group (they must be equal!).",
                        "Write the addition: add the group size over and over.",
                        "For 4 groups of 3: write 3 + 3 + 3 + 3.",
                        "Add them all up to get the total!",
                    ],
                    "fun_fact": "Repeated addition is actually the secret behind multiplication! Later you will learn that 3 groups of 4 can be written as 3 × 4 = 12. The × sign means 'groups of'!",
                    "problem_config": {
                        "type": "multiplication_intro",
                        "params": {"max_groups": 5, "max_per_group": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "All Four Shapes",
                "description": "Review and identify circles, squares, triangles, and rectangles",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "In Grade 1, you learned about circles, squares, triangles, and rectangles. Let's review all four shapes together!\n\nCircle ⭕: Round, no sides, no corners. Like a ball or a coin.\nTriangle 🔺: 3 sides, 3 corners. Like a slice of pizza.\nSquare ⬜: 4 EQUAL sides, 4 corners. Like a window tile.\nRectangle 📱: 4 sides (2 long, 2 short), 4 corners. Like a door or phone.\n\nRemember: a square is a special rectangle where ALL sides are the same length!",
                    "examples": [
                        {"visual": "⭕ Circle", "text": "A circle has 0 sides and 0 corners. It is perfectly round!"},
                        {"visual": "🔺 Triangle", "text": "A triangle has 3 sides and 3 corners. Tri means three!"},
                        {"visual": "⬜ Square", "text": "A square has 4 equal sides and 4 corners. All sides are the same!"},
                        {"visual": "📱 Rectangle", "text": "A rectangle has 4 sides and 4 corners. Opposite sides are equal."},
                    ],
                    "steps": [
                        "Look at the shape or object.",
                        "Count the sides (straight edges).",
                        "Count the corners (where sides meet).",
                        "0 sides and round → Circle.",
                        "3 sides → Triangle. 4 equal sides → Square. 4 sides (2 long, 2 short) → Rectangle.",
                    ],
                    "fun_fact": "Shapes are used in building everything! Triangles are the strongest shape - that is why bridges and roofs use triangle shapes to stay strong.",
                    "problem_config": {
                        "type": "shape_properties",
                        "params": {"shapes": ["circle", "square", "triangle", "rectangle"]},
                        "count": 5,
                    },
                },
            },
        ],
    },
]
