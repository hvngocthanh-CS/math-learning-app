"""
Grade 1 curriculum for MathQuest.
Each lesson has:
  - Static learn content: explanation, examples, steps, fun_fact
  - Dynamic problem_config: tells the problem generator what to generate
  - practice_problems / quiz_problems are generated at runtime (not stored)
"""

GRADE1_CHAPTERS = [
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 1: Numbers 1-10
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Numbers 1-10",
        "description": "Learn to count and recognize numbers from 1 to 10",
        "order": 1,
        "lessons": [
            {
                "title": "Counting 1 to 5",
                "description": "Learn to count objects from 1 to 5",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Counting is one of the first things we learn in math! When we count, we say numbers in order: 1, 2, 3, 4, 5. Each number tells us how many things there are.\n\nImagine you have some yummy apples 🍎. If you point to each apple and say a number, you are counting! The last number you say tells you how many apples you have.\n\nLet's practice counting from 1 to 5 together. Remember, take your time and point to each object as you count!",
                    "examples": [
                        {"visual": "🍎", "text": "One apple. We write this as 1."},
                        {"visual": "🍎🍎", "text": "Two apples. We write this as 2."},
                        {"visual": "🍎🍎🍎", "text": "Three apples. We write this as 3."},
                        {"visual": "🍎🍎🍎🍎🍎", "text": "Five apples! We write this as 5."},
                    ],
                    "steps": [
                        "Point to each object one at a time.",
                        "Say a number for each object: 1, 2, 3, 4, 5.",
                        "The last number you say is the total count!",
                        "Try again with different objects to practice.",
                    ],
                    "fun_fact": "Did you know? Baby chicks can count up to 5! Even animals know how to count small numbers.",
                    "problem_config": {
                        "type": "counting",
                        "params": {"min": 1, "max": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Counting 6 to 10",
                "description": "Learn to count larger groups from 6 to 10",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "Great job counting to 5! Now let's learn bigger numbers: 6, 7, 8, 9, and 10. These numbers come right after 5.\n\nWhen you have more than 5 things, keep counting! After 5 comes 6, then 7, then 8, then 9, and finally 10. Ten is a very special number because it uses two digits: a 1 and a 0.\n\nYou can use your fingers to help you count - you have exactly 10 fingers!",
                    "examples": [
                        {"visual": "🌟🌟🌟🌟🌟🌟", "text": "Six stars. We write this as 6."},
                        {"visual": "🌟🌟🌟🌟🌟🌟🌟", "text": "Seven stars. We write this as 7."},
                        {"visual": "🌟🌟🌟🌟🌟🌟🌟🌟", "text": "Eight stars. We write this as 8."},
                        {"visual": "🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟", "text": "Ten stars! We write this as 10."},
                    ],
                    "steps": [
                        "Start counting from 1 just like before.",
                        "Keep going past 5: say 6, 7, 8, 9, 10.",
                        "Use your fingers to help - hold up one finger for each number.",
                        "The last number you say is how many there are.",
                        "Practice counting groups of toys or snacks at home!",
                    ],
                    "fun_fact": "You have 10 fingers and 10 toes. That is 20 altogether! Humans have been counting on their fingers for thousands of years.",
                    "problem_config": {
                        "type": "counting",
                        "params": {"min": 6, "max": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Number Recognition",
                "description": "Match numbers to words and recognize written numbers",
                "order": 3,
                "xp_reward": 20,
                "content": {
                    "explanation": "Now that you can count, let's learn to recognize numbers when we see them written down! Each number has its own special look and its own name.\n\nThe number 1 looks like a straight line going down. The number 2 has a curve at the top. The number 3 looks like two bumps. Every number from 1 to 10 has a word name too!\n\nWhen you see the number 5, you say 'five'. When you see the word 'three', you know it means the number 3.",
                    "examples": [
                        {"visual": "1 = one", "text": "The number 1 is called 'one'. It looks like a single line."},
                        {"visual": "2 = two", "text": "The number 2 is called 'two'. It has a curve at the top."},
                        {"visual": "3 = three", "text": "The number 3 is called 'three'. It looks like two bumps."},
                        {"visual": "4 = four", "text": "The number 4 is called 'four'. It has a pointy top."},
                        {"visual": "5 = five", "text": "The number 5 is called 'five'. It has a flat top and a curve."},
                        {"visual": "6 = six", "text": "The number 6 is called 'six'. It has a big round belly."},
                        {"visual": "7 = seven", "text": "The number 7 is called 'seven'. It has a line across the top."},
                        {"visual": "8 = eight", "text": "The number 8 is called 'eight'. It looks like a snowman!"},
                        {"visual": "9 = nine", "text": "The number 9 is called 'nine'. It looks like 6 upside down."},
                        {"visual": "10 = ten", "text": "The number 10 is called 'ten'. It uses two digits!"},
                    ],
                    "steps": [
                        "Look at the number carefully.",
                        "Remember its name: 1=one, 2=two, 3=three, 4=four, 5=five.",
                        "Keep going: 6=six, 7=seven, 8=eight, 9=nine, 10=ten.",
                        "Practice saying each number name when you see the digit.",
                    ],
                    "fun_fact": "The numbers we use (0, 1, 2, 3...) are called Arabic numerals. They were invented over 1,000 years ago in India!",
                    "problem_config": {
                        "type": "number_recognition",
                        "params": {"min": 1, "max": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Number Sequences",
                "description": "Learn number order and fill in missing numbers",
                "order": 4,
                "xp_reward": 20,
                "content": {
                    "explanation": "Numbers always go in the same order: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. When we put numbers in order, we call it a number sequence!\n\nSometimes a number in the sequence is missing, and we need to figure out which one it is. If you see 1, 2, __, 4 - the missing number is 3 because 3 comes between 2 and 4.\n\nKnowing the order of numbers helps us understand which numbers are bigger and which are smaller.",
                    "examples": [
                        {"visual": "1, 2, 3, 4, 5", "text": "The numbers 1 to 5 in order. Each number is one more than the last."},
                        {"visual": "3, _, 5", "text": "The missing number is 4! It goes between 3 and 5."},
                        {"visual": "7, 8, 9, _", "text": "What comes after 9? The answer is 10!"},
                        {"visual": "_, 2, 3", "text": "What comes before 2? The answer is 1!"},
                    ],
                    "steps": [
                        "Read the numbers you can see.",
                        "Think about what comes before and after each number.",
                        "Remember: each number is one more than the number before it.",
                        "Fill in the missing number.",
                        "Check by counting the whole sequence out loud.",
                    ],
                    "fun_fact": "The number zero (0) was invented much later than other numbers. Ancient people counted starting from 1!",
                    "problem_config": {
                        "type": "number_sequence",
                        "params": {"min": 1, "max": 10},
                        "count": 5,
                    },
                },
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 2: Addition within 10
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Addition Basics",
        "description": "Introduction to adding numbers together",
        "order": 2,
        "lessons": [
            {
                "title": "What is Addition?",
                "description": "Learn the concept of addition with visuals",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Addition means putting things together to find out how many you have in all! When we add, we combine two groups into one bigger group.\n\nWe use the plus sign (+) to show addition and the equals sign (=) to show the answer. For example, 2 + 1 = 3 means 'two plus one equals three'.\n\nThink of it like this: if you have 2 toys and your friend gives you 1 more toy, now you have 3 toys altogether!",
                    "examples": [
                        {"visual": "🍎 + 🍎 = 🍎🍎", "text": "1 + 1 = 2. One apple plus one apple equals two apples!"},
                        {"visual": "🍎🍎 + 🍎 = 🍎🍎🍎", "text": "2 + 1 = 3. Two apples plus one apple equals three apples!"},
                        {"visual": "🌟🌟 + 🌟🌟 = 🌟🌟🌟🌟", "text": "2 + 2 = 4. Two stars plus two stars equals four stars!"},
                        {"visual": "🐶 + 🐶🐶🐶 = 🐶🐶🐶🐶", "text": "1 + 3 = 4. One dog plus three dogs equals four dogs!"},
                    ],
                    "steps": [
                        "Look at the first group and count how many.",
                        "Look at the second group and count how many.",
                        "Put both groups together.",
                        "Count the total - that is your answer!",
                        "Write it as: first number + second number = total.",
                    ],
                    "fun_fact": "The plus sign (+) was first used over 500 years ago! Before that, people wrote the word 'and' instead.",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 1, "max_a": 3, "min_b": 1, "max_b": 3, "max_sum": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Adding with Objects",
                "description": "Practice addition using objects and pictures",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "The best way to learn addition is by using real objects! You can use your fingers, toys, candies, or anything you can count.\n\nHere is how to add with objects: First, put out the first number of objects. Then, put out the second number of objects next to them. Finally, count all the objects together to get your answer!\n\nFor example, to solve 3 + 2, put out 3 blocks, then put out 2 more blocks. Now count them all: 1, 2, 3, 4, 5. The answer is 5!",
                    "examples": [
                        {"visual": "🍎🍎🍎 + 🍎🍎 = 🍎🍎🍎🍎🍎", "text": "3 + 2 = 5. Three apples plus two apples equals five!"},
                        {"visual": "🌟 + 🌟🌟🌟🌟 = 🌟🌟🌟🌟🌟", "text": "1 + 4 = 5. One star plus four stars equals five!"},
                        {"visual": "🐟🐟 + 🐟🐟🐟 = 🐟🐟🐟🐟🐟", "text": "2 + 3 = 5. Two fish plus three fish equals five!"},
                        {"visual": "🎈🎈🎈🎈 + 🎈 = 🎈🎈🎈🎈🎈", "text": "4 + 1 = 5. Four balloons plus one balloon equals five!"},
                    ],
                    "steps": [
                        "Read the math problem: what two numbers are you adding?",
                        "Hold up fingers for the first number on one hand.",
                        "Hold up fingers for the second number on the other hand.",
                        "Count all your raised fingers together.",
                        "That total is your answer!",
                    ],
                    "fun_fact": "Ancient people used pebbles to count and add. The word 'calculator' actually comes from the Latin word for pebble!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 1, "max_a": 4, "min_b": 1, "max_b": 4, "max_sum": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Addition up to 5",
                "description": "Practice addition problems with answers up to 5",
                "order": 3,
                "xp_reward": 20,
                "content": {
                    "explanation": "Now let's practice addition with answers up to 5! You already know how to add using objects and fingers.\n\nRemember, you can always use your fingers to help! If the problem says 2 + 3, hold up 2 fingers on one hand and 3 fingers on the other. Then count them all together: 5!\n\nThe more you practice, the faster you will get. Soon you will know the answers without even counting!",
                    "examples": [
                        {"visual": "0 + 5 = 5", "text": "Zero plus five equals five. Adding zero does not change the number!"},
                        {"visual": "1 + 4 = 5", "text": "One plus four equals five."},
                        {"visual": "2 + 3 = 5", "text": "Two plus three equals five."},
                        {"visual": "5 + 0 = 5", "text": "Five plus zero equals five. Adding zero gives the same number!"},
                    ],
                    "steps": [
                        "Read the two numbers in the problem.",
                        "Start with the bigger number (it is easier!).",
                        "Count up from the bigger number by the smaller number.",
                        "For example: 3 + 2 means start at 3 and count up 2 more: 4, 5!",
                        "Write down your answer.",
                    ],
                    "fun_fact": "When you add zero to any number, the answer is always that same number. Zero is called the 'additive identity' because it does not change anything!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 0, "max_a": 5, "min_b": 0, "max_b": 5, "max_sum": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Addition up to 10",
                "description": "Practice addition problems with answers up to 10",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "You are getting so good at addition! Now let's try bigger problems with answers up to 10. You might need to use both hands for these!\n\nWhen adding bigger numbers, a helpful trick is to start with the bigger number and count up. For example, for 3 + 6, start at 6 and count up 3 more: 7, 8, 9. The answer is 9!\n\nYou can also break numbers apart to make them easier. For 4 + 5, think of it as 4 + 4 + 1 = 8 + 1 = 9.",
                    "examples": [
                        {"visual": "5 + 5 = 10", "text": "Five plus five equals ten. Two hands with all fingers up!"},
                        {"visual": "3 + 4 = 7", "text": "Three plus four equals seven."},
                        {"visual": "6 + 2 = 8", "text": "Six plus two equals eight."},
                        {"visual": "4 + 5 = 9", "text": "Four plus five equals nine."},
                    ],
                    "steps": [
                        "Read the two numbers in the problem.",
                        "Start with the bigger number.",
                        "Count up by the smaller number.",
                        "For example: 6 + 3 means start at 6, count: 7, 8, 9!",
                        "Use both hands if you need more fingers.",
                    ],
                    "fun_fact": "If you add all the numbers from 1 to 10 together (1+2+3+4+5+6+7+8+9+10), you get 55!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 1, "max_a": 9, "min_b": 1, "max_b": 9, "max_sum": 10},
                        "count": 5,
                    },
                },
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 3: Subtraction within 10
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Subtraction Basics",
        "description": "Introduction to taking numbers away",
        "order": 3,
        "lessons": [
            {
                "title": "What is Subtraction?",
                "description": "Learn the concept of taking away",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Subtraction means taking away! When we subtract, we start with a group of things and remove some. The number left over is our answer.\n\nWe use the minus sign (-) to show subtraction. For example, 3 - 1 = 2 means 'three minus one equals two'. If you have 3 candies and eat 1, you have 2 left!\n\nSubtraction is the opposite of addition. If 2 + 1 = 3, then 3 - 1 = 2.",
                    "examples": [
                        {"visual": "🍎🍎🍎 - 🍎 = 🍎🍎", "text": "3 - 1 = 2. Start with three apples, take one away, two are left!"},
                        {"visual": "🌟🌟🌟🌟 - 🌟🌟 = 🌟🌟", "text": "4 - 2 = 2. Start with four stars, take two away, two are left!"},
                        {"visual": "🍪🍪🍪🍪🍪 - 🍪🍪🍪 = 🍪🍪", "text": "5 - 3 = 2. Five cookies minus three cookies equals two!"},
                        {"visual": "🐶🐶 - 🐶 = 🐶", "text": "2 - 1 = 1. Two dogs minus one dog equals one dog!"},
                    ],
                    "steps": [
                        "Start with the first number (the bigger number).",
                        "The second number tells you how many to take away.",
                        "Remove that many from your group.",
                        "Count what is left - that is your answer!",
                        "Write it as: big number - small number = answer.",
                    ],
                    "fun_fact": "The minus sign (-) was first used in a math book in the year 1489. That is over 500 years ago!",
                    "problem_config": {
                        "type": "subtraction",
                        "params": {"min_start": 2, "max_start": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Subtracting with Objects",
                "description": "Practice subtraction using objects and visuals",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "Just like with addition, we can use objects to help us subtract! You can use blocks, coins, candies, or even your fingers.\n\nHere is how: Hold up the first number of fingers. Then put down the second number of fingers. Count how many fingers are still up - that is your answer!\n\nFor example, to solve 5 - 2: hold up 5 fingers. Put down 2 fingers. Count the fingers still up: 1, 2, 3. The answer is 3!",
                    "examples": [
                        {"visual": "🖐️ 5 fingers - 2 fingers = 3 fingers up", "text": "5 - 2 = 3. Start with 5 fingers up, put 2 down, 3 are left."},
                        {"visual": "🍭🍭🍭🍭 - 🍭 = 🍭🍭🍭", "text": "4 - 1 = 3. Four lollipops minus one equals three."},
                        {"visual": "🐟🐟🐟🐟🐟 - 🐟🐟 = 🐟🐟🐟", "text": "5 - 2 = 3. Five fish minus two fish equals three."},
                        {"visual": "🌺🌺🌺 - 🌺🌺 = 🌺", "text": "3 - 2 = 1. Three flowers minus two flowers equals one."},
                    ],
                    "steps": [
                        "Read the problem: what number do you start with?",
                        "Hold up that many fingers (or put out that many objects).",
                        "Now look at how many you need to take away.",
                        "Put down that many fingers (or remove that many objects).",
                        "Count what is left - that is your answer!",
                    ],
                    "fun_fact": "Monkeys can do simple subtraction too! Scientists showed that monkeys can figure out when items are taken away from a group.",
                    "problem_config": {
                        "type": "subtraction",
                        "params": {"min_start": 2, "max_start": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Subtraction within 10",
                "description": "Practice subtraction with numbers up to 10",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Now let's try bigger subtraction problems! We will subtract numbers up to 10. Remember, you can always count backwards to find the answer.\n\nCounting backwards means starting at the first number and counting down. For 8 - 3, start at 8 and count back 3: 7, 6, 5. The answer is 5!\n\nAnother trick: think about addition! If you know that 4 + 3 = 7, then you also know that 7 - 3 = 4.",
                    "examples": [
                        {"visual": "7 - 2 = 5", "text": "Seven minus two equals five. Start at 7, count back: 6, 5."},
                        {"visual": "9 - 4 = 5", "text": "Nine minus four equals five. Start at 9, count back: 8, 7, 6, 5."},
                        {"visual": "10 - 3 = 7", "text": "Ten minus three equals seven."},
                        {"visual": "8 - 5 = 3", "text": "Eight minus five equals three."},
                    ],
                    "steps": [
                        "Read the first number (the one you start with).",
                        "Read the second number (how many to take away).",
                        "Start at the first number and count backwards.",
                        "Count back as many times as the second number.",
                        "The number you land on is your answer!",
                    ],
                    "fun_fact": "When a rocket launches, we count backwards: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, BLAST OFF! That is subtraction in action!",
                    "problem_config": {
                        "type": "subtraction",
                        "params": {"min_start": 3, "max_start": 10},
                        "count": 5,
                    },
                },
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 4: Comparing Numbers
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Comparing Numbers",
        "description": "Learn to compare numbers using greater than, less than, and equal",
        "order": 4,
        "lessons": [
            {
                "title": "Greater Than and Less Than",
                "description": "Learn the symbols > and < to compare two numbers",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "When we compare two numbers, we figure out which one is bigger and which one is smaller. We use special symbols to show this!\n\nThe greater than sign > looks like an open mouth eating the bigger number. 5 > 3 means 'five is greater than three'. The mouth always opens toward the bigger number!\n\nThe less than sign < is the opposite. 2 < 7 means 'two is less than seven'. Think of a hungry alligator - it always wants to eat the bigger number!",
                    "examples": [
                        {"visual": "5 > 3", "text": "5 is greater than 3. The alligator mouth opens toward 5!"},
                        {"visual": "2 < 7", "text": "2 is less than 7. The small pointy end faces 2."},
                        {"visual": "9 > 4", "text": "9 is greater than 4. Nine is the bigger number!"},
                        {"visual": "1 < 6", "text": "1 is less than 6. One is the smaller number!"},
                    ],
                    "steps": [
                        "Look at the two numbers you want to compare.",
                        "Decide which number is bigger.",
                        "The alligator mouth (open side) always faces the BIGGER number.",
                        "Use > if the first number is bigger: 8 > 3.",
                        "Use < if the first number is smaller: 3 < 8.",
                    ],
                    "fun_fact": "The > and < symbols were invented by Thomas Harriot in 1631. He was an English mathematician who also helped explore America!",
                    "problem_config": {
                        "type": "comparison",
                        "params": {"min": 1, "max": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Equal To",
                "description": "Learn the equals sign and when two numbers are the same",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "Sometimes two numbers are the same! When two things have the same value, we say they are EQUAL. We use the equals sign = to show this.\n\n5 = 5 means 'five equals five'. They are the same number!\n\nNow you know all three comparison symbols: > (greater than), < (less than), and = (equal to). You can compare any two numbers!",
                    "examples": [
                        {"visual": "3 = 3", "text": "Three equals three. They are the same number!"},
                        {"visual": "🍎🍎🍎 = 🍌🍌🍌", "text": "3 apples and 3 bananas. The amounts are equal: 3 = 3"},
                        {"visual": "7 = 7", "text": "Seven equals seven. Same number on both sides!"},
                        {"visual": "2 + 3 = 5", "text": "Two plus three equals five. Both sides have the same value!"},
                    ],
                    "steps": [
                        "Look at both numbers or groups.",
                        "Count each side carefully.",
                        "If both sides have the same amount, they are EQUAL.",
                        "Use the = sign to show they are the same.",
                        "Remember: > means bigger, < means smaller, = means same!",
                    ],
                    "fun_fact": "The equals sign = was invented by Robert Recorde in 1557. He said he used two parallel lines because 'no two things can be more equal' than parallel lines!",
                    "problem_config": {
                        "type": "comparison_full",
                        "params": {"min": 1, "max": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Ordering Numbers",
                "description": "Arrange numbers from smallest to largest and largest to smallest",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "Now that you know how to compare numbers, let's learn to put them in order!\n\nAscending order means from SMALLEST to BIGGEST: 1, 3, 5, 7, 9. The numbers go up like climbing stairs!\n\nDescending order means from BIGGEST to SMALLEST: 9, 7, 5, 3, 1. The numbers go down like sliding down a slide!",
                    "examples": [
                        {"visual": "2, 5, 8 (ascending)", "text": "Ascending order (smallest to biggest): 2, 5, 8."},
                        {"visual": "9, 6, 1 (descending)", "text": "Descending order (biggest to smallest): 9, 6, 1."},
                        {"visual": "4, 1, 7 → 1, 4, 7", "text": "Arrange 4, 1, 7 ascending: 1, 4, 7."},
                        {"visual": "3, 8, 5 → 8, 5, 3", "text": "Arrange 3, 8, 5 descending: 8, 5, 3."},
                    ],
                    "steps": [
                        "Look at all the numbers you need to order.",
                        "For ascending (going up): find the smallest number first.",
                        "Then find the next smallest, and keep going.",
                        "For descending (going down): find the biggest number first.",
                        "Check your answer by making sure each number follows the pattern.",
                    ],
                    "fun_fact": "Computers sort millions of numbers in less than a second! They use special sorting methods called algorithms.",
                    "problem_config": {
                        "type": "ordering",
                        "params": {"min": 1, "max": 10, "count": 3},
                        "count": 5,
                    },
                },
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 5: Shapes
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Shapes",
        "description": "Learn about basic geometric shapes and patterns",
        "order": 5,
        "lessons": [
            {
                "title": "Circles and Squares",
                "description": "Identify circles and squares in the world around you",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "Shapes are everywhere! Let's learn about two very common shapes: circles and squares.\n\nA circle is perfectly round, like a ball or a cookie. It has no corners and no straight sides. Think of the sun or a wheel - they are circles!\n\nA square has 4 straight sides that are all the same length, and 4 corners. Think of a window or a cracker.",
                    "examples": [
                        {"visual": "⭕ Circle", "text": "This is a circle. It is round with no corners. A clock face is a circle!"},
                        {"visual": "⬜ Square", "text": "This is a square. It has 4 equal sides and 4 corners."},
                        {"visual": "🏀 Basketball", "text": "A basketball is shaped like a circle (a sphere in 3D)!"},
                        {"visual": "🖼️ Picture frame", "text": "Many picture frames are shaped like squares!"},
                    ],
                    "steps": [
                        "Look at the shape carefully.",
                        "Is it round with no corners? It is a circle!",
                        "Does it have 4 equal straight sides and 4 corners? It is a square!",
                        "Look around your room - can you find circles and squares?",
                        "Practice drawing circles and squares on paper.",
                    ],
                    "fun_fact": "A pizza is a circle! And when you cut it into slices, each slice is shaped like a triangle. Shapes are delicious!",
                    "problem_config": {
                        "type": "shape_properties",
                        "params": {"shapes": ["circle", "square"]},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Triangles and Rectangles",
                "description": "Learn about triangles and rectangles",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "Let's learn about two more important shapes: triangles and rectangles!\n\nA triangle has 3 sides and 3 corners. 'Tri' means three! Think of a pizza slice or a mountain peak.\n\nA rectangle has 4 sides and 4 corners, just like a square. But a rectangle's sides are not all the same length - two sides are longer and two are shorter. Think of a door or a book!",
                    "examples": [
                        {"visual": "🔺 Triangle", "text": "This is a triangle. It has 3 sides and 3 corners."},
                        {"visual": "📱 Rectangle", "text": "A phone screen is a rectangle. 2 long sides and 2 short sides."},
                        {"visual": "🏔️ Mountain", "text": "A mountain peak looks like a triangle!"},
                        {"visual": "📚 Book", "text": "A book cover is shaped like a rectangle."},
                    ],
                    "steps": [
                        "Count the sides of the shape.",
                        "If it has 3 sides and 3 corners, it is a triangle!",
                        "If it has 4 sides with 2 long and 2 short, it is a rectangle!",
                        "Remember: a square is a special rectangle where all sides are equal.",
                        "Look for triangles and rectangles around your home!",
                    ],
                    "fun_fact": "The pyramids in Egypt are made of triangles on every side! They are over 4,500 years old and still standing.",
                    "problem_config": {
                        "type": "shape_properties",
                        "params": {"shapes": ["triangle", "rectangle"]},
                        "count": 5,
                    },
                },
            },
        ],
    },
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 6: Numbers 11-20
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Numbers 11-20",
        "description": "Learn to count, read, and work with numbers from 11 to 20",
        "order": 6,
        "lessons": [
            {
                "title": "Counting 11 to 15",
                "description": "Learn to count and recognize numbers from 11 to 15",
                "order": 1,
                "xp_reward": 20,
                "content": {
                    "explanation": "You already know numbers 1 to 10. Now let's learn bigger numbers: 11, 12, 13, 14, and 15!\n\nThese numbers are made of tens and ones. The number 11 means 1 ten and 1 one. The number 12 means 1 ten and 2 ones.\n\nThink of it like this: 10 is like a full box of 10 items. 13 means one full box (10) plus 3 more items outside the box!",
                    "examples": [
                        {"visual": "11 = eleven", "text": "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ + ⭐\nCount: 10 + 1 = 11!"},
                        {"visual": "12 = twelve", "text": "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ + ⭐⭐\nCount: 10 + 2 = 12!"},
                        {"visual": "13 = thirteen", "text": "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ + ⭐⭐⭐\nCount: 10 + 3 = 13!"},
                        {"visual": "14 = fourteen", "text": "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ + ⭐⭐⭐⭐\nCount: 10 + 4 = 14!"},
                        {"visual": "15 = fifteen", "text": "⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐ + ⭐⭐⭐⭐⭐\nCount: 10 + 5 = 15!"},
                    ],
                    "steps": [
                        "Numbers after 10 are made of TENS and ONES.",
                        "11 = 10 + 1 (eleven), 12 = 10 + 2 (twelve).",
                        "13 = 10 + 3 (thirteen), 14 = 10 + 4 (fourteen).",
                        "15 = 10 + 5 (fifteen).",
                        "To count past 10, just keep going: 11, 12, 13, 14, 15!",
                    ],
                    "fun_fact": "The word 'eleven' comes from Old English meaning 'one left over' (after counting to ten). And 'twelve' means 'two left over'!",
                    "problem_config": {
                        "type": "counting",
                        "params": {"min": 11, "max": 15},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Counting 16 to 20",
                "description": "Learn to count and recognize numbers from 16 to 20",
                "order": 2,
                "xp_reward": 20,
                "content": {
                    "explanation": "Let's finish learning all the numbers up to 20! After 15 comes 16, 17, 18, 19, and 20.\n\n16 = 10 + 6, 17 = 10 + 7, 18 = 10 + 8, 19 = 10 + 9.\n\n20 is special! It means 2 tens and 0 ones. Twenty is two groups of ten! Now you can count all the way from 1 to 20!",
                    "examples": [
                        {"visual": "16 = sixteen", "text": "🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 + 🌸🌸🌸🌸🌸🌸\nCount: 10 + 6 = 16!"},
                        {"visual": "17 = seventeen", "text": "🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 + 🌸🌸🌸🌸🌸🌸🌸\nCount: 10 + 7 = 17!"},
                        {"visual": "18 = eighteen", "text": "🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 + 🌸🌸🌸🌸🌸🌸🌸🌸\nCount: 10 + 8 = 18!"},
                        {"visual": "19 = nineteen", "text": "🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 + 🌸🌸🌸🌸🌸🌸🌸🌸🌸\nCount: 10 + 9 = 19!"},
                        {"visual": "20 = twenty", "text": "🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 + 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸\nCount: 10 + 10 = 20! Two groups of ten!"},
                    ],
                    "steps": [
                        "16 = 10 + 6 (sixteen), 17 = 10 + 7 (seventeen).",
                        "18 = 10 + 8 (eighteen), 19 = 10 + 9 (nineteen).",
                        "20 = 10 + 10 = two tens (twenty).",
                        "Practice counting from 1 to 20 out loud!",
                        "You can use your fingers twice: first 1-10, then 11-20.",
                    ],
                    "fun_fact": "In French, the number 80 is said as 'quatre-vingts' which means 'four twenties'. Some languages count by twenties instead of tens!",
                    "problem_config": {
                        "type": "counting",
                        "params": {"min": 16, "max": 20},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Tens and Ones",
                "description": "Understand place value: tens and ones in numbers 11-20",
                "order": 3,
                "xp_reward": 20,
                "content": {
                    "explanation": "Every number from 11 to 20 is made up of TENS and ONES. This is called place value!\n\nThe tens digit is on the left. The ones digit is on the right. In the number 14, the 1 means one ten (10) and the 4 means four ones (4). So 14 = 10 + 4!\n\nThink of it like a piggy bank: coins in stacks of 10. If you have 1 stack and 7 loose coins, you have 17!",
                    "examples": [
                        {"visual": "13 → 1 ten + 3 ones", "text": "13 has 1 in the tens place and 3 in the ones place."},
                        {"visual": "16 → 1 ten + 6 ones", "text": "16 has 1 in the tens place and 6 in the ones place."},
                        {"visual": "20 → 2 tens + 0 ones", "text": "20 has 2 in the tens place and 0 in the ones place."},
                        {"visual": "19 → 1 ten + 9 ones", "text": "19 has 1 ten and 9 ones. It is the last number before 20!"},
                    ],
                    "steps": [
                        "Look at the number. It has two digits.",
                        "The LEFT digit is the TENS place.",
                        "The RIGHT digit is the ONES place.",
                        "Tens place tells you how many groups of 10.",
                        "Ones place tells you how many extra ones.",
                    ],
                    "fun_fact": "Our number system is called 'base 10' because we group things by tens. This is probably because humans have 10 fingers!",
                    "problem_config": {
                        "type": "place_value",
                        "params": {"min": 11, "max": 20},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Addition within 20",
                "description": "Practice adding numbers with sums up to 20",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "Now let's add bigger numbers with answers up to 20! A helpful trick: when adding a number to 10, just put the number after the 1! 10 + 7 = 17.\n\nFor harder problems like 8 + 5, use the 'make 10' strategy: take 2 from the 5 to make 8 into 10, then add the leftover 3. So 8 + 5 = 10 + 3 = 13!",
                    "examples": [
                        {"visual": "10 + 6 = 16", "text": "Ten plus six equals sixteen. Just put the 6 after the 1!"},
                        {"visual": "9 + 5 = 14", "text": "Nine plus five: take 1 from 5 to make 10, then 10 + 4 = 14!"},
                        {"visual": "8 + 7 = 15", "text": "Eight plus seven: take 2 from 7 to make 10, then 10 + 5 = 15!"},
                        {"visual": "10 + 10 = 20", "text": "Ten plus ten equals twenty! Two groups of ten!"},
                    ],
                    "steps": [
                        "If adding to 10, just combine: 10 + 4 = 14.",
                        "For other problems, try the 'make 10' strategy.",
                        "Take from one number to make the other into 10.",
                        "Then add the leftover to 10.",
                        "Example: 7 + 6 = (7+3) + 3 = 10 + 3 = 13.",
                    ],
                    "fun_fact": "The 'make 10' strategy is widely used in Asian countries and is one of the reasons students there are great at mental math!",
                    "problem_config": {
                        "type": "addition",
                        "params": {"min_a": 2, "max_a": 10, "min_b": 2, "max_b": 10, "max_sum": 20},
                        "count": 5,
                    },
                },
            },
        ],
    },
]
