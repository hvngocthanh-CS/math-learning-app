"""
Grade 2 curriculum for MathQuest.
"""

GRADE2_CHAPTERS = [
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 1: Measurement
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Measurement",
        "description": "Introduction to measuring and comparing",
        "order": 1,
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
                "title": "Telling Time",
                "description": "Learn to read a clock to the hour",
                "order": 2,
                "xp_reward": 25,
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
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 2: Patterns
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Patterns",
        "description": "Learn to recognize and continue patterns",
        "order": 2,
        "lessons": [
            {
                "title": "Pattern Recognition",
                "description": "Find and continue ABAB patterns",
                "order": 1,
                "xp_reward": 25,
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
        ],
    },
]
