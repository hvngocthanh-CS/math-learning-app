"""
Grade 5 curriculum for MathQuest.
3 chapters, 9 lessons total.
Builds on Grade 4 (multiplication/division, fractions, decimals).
Topics: area, volume, units of measurement, percentages.
"""

GRADE5_CHAPTERS = [
    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 1: Area
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Area",
        "description": "Calculate the area of rectangles, squares, triangles, and circles",
        "order": 1,
        "lessons": [
            {
                "title": "Area of Rectangles and Squares",
                "description": "Calculate area using length × width for rectangles and side × side for squares",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Area is the amount of space INSIDE a flat shape. We measure area in square units (cm², m²).\n\nFor a rectangle:\nArea = length × width\n\nImagine covering the rectangle with small square tiles — the number of tiles is the area!\n\nExample: A rectangle that is 5 cm long and 3 cm wide.\nArea = 5 × 3 = 15 cm²\n\nA square is a special rectangle where all sides are equal:\nArea of a square = side × side\n\nExample: A square with side 4 cm.\nArea = 4 × 4 = 16 cm²\n\nWord problem: A room is 6 m long and 4 m wide. How much carpet is needed?\nArea = 6 × 4 = 24 m².",
                    "examples": [
                        {"visual": "🖥️", "text": "A rectangle 6 cm × 4 cm. Area = 6 × 4 = 24 cm²."},
                        {"visual": "🪟", "text": "A square with side 5 cm. Area = 5 × 5 = 25 cm²."},
                        {"visual": "🎨", "text": "A wall is 8 m × 3 m. Paint needed? Area = 8 × 3 = 24 m²."},
                        {"visual": "🏠", "text": "A square garden has side 7 m. Area = 7 × 7 = 49 m²."},
                    ],
                    "steps": [
                        "Identify: is it a rectangle or a square?",
                        "Rectangle: Area = length × width.",
                        "Square: Area = side × side.",
                        "Write the answer with square units (cm², m²).",
                        "To find a missing side: divide the area by the known side.",
                    ],
                    "fun_fact": "The largest rectangle you can make with a fixed perimeter is always a square! For example, with 20 cm of string, a 5×5 square gives 25 cm² — more than any other rectangle.",
                    "problem_config": {
                        "type": "area_rectangle",
                        "params": {"min_side": 2, "max_side": 15},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Area of Triangles",
                "description": "Calculate the area of a triangle using base × height ÷ 2",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "A triangle is exactly HALF of a rectangle!\n\nIf you draw a rectangle and cut it diagonally, you get two triangles. Each triangle is half the rectangle.\n\nArea of a triangle = base × height ÷ 2\n\nThe BASE is the bottom side. The HEIGHT is the straight-up distance from the base to the top point.\n\nExample: base = 8 cm, height = 6 cm.\nArea = 8 × 6 ÷ 2 = 48 ÷ 2 = 24 cm²\n\nWord problem: A triangular flag has base 10 cm and height 6 cm.\nArea = 10 × 6 ÷ 2 = 30 cm².",
                    "examples": [
                        {"visual": "🔺", "text": "Base 6 cm, height 4 cm. Area = 6 × 4 ÷ 2 = 12 cm²."},
                        {"visual": "🔺", "text": "Base 10 cm, height 5 cm. Area = 10 × 5 ÷ 2 = 25 cm²."},
                        {"visual": "🚩", "text": "A triangular flag: base 8 cm, height 6 cm. Area = 8 × 6 ÷ 2 = 24 cm²."},
                        {"visual": "🌿", "text": "A triangular garden: base 12 m, height 4 m. Area = 12 × 4 ÷ 2 = 24 m²."},
                    ],
                    "steps": [
                        "Find the base and the height of the triangle.",
                        "Multiply base × height.",
                        "Divide the result by 2.",
                        "Write the answer with square units (cm², m²).",
                        "Example: base 7, height 4 → 7 × 4 = 28 → 28 ÷ 2 = 14 cm².",
                    ],
                    "fun_fact": "The Bermuda Triangle in the Atlantic Ocean covers about 1,300,000 km² — that is roughly the area of a triangle with a base of 1,600 km and a height of 1,625 km!",
                    "problem_config": {
                        "type": "area_triangle",
                        "params": {"min_base": 2, "max_base": 16, "min_height": 2, "max_height": 12},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Area of Circles",
                "description": "Calculate the area of a circle using π × radius × radius",
                "order": 3,
                "xp_reward": 30,
                "content": {
                    "explanation": "A circle's area depends on its RADIUS (the distance from the centre to the edge).\n\nArea of a circle = π × r × r\n\nπ (pi) is a special number ≈ 3.14.\n\nStep by step:\n1. Find the radius (r).\n2. Multiply r × r (square the radius).\n3. Multiply by 3.14.\n\nExample: radius = 5 cm.\nArea = 3.14 × 5 × 5 = 3.14 × 25 = 78.5 cm²\n\nIf you are given the DIAMETER, remember: radius = diameter ÷ 2.\nDiameter = 10 cm → radius = 5 cm.",
                    "examples": [
                        {"visual": "⭕", "text": "Radius 3 cm. Area = 3.14 × 3 × 3 = 3.14 × 9 = 28.26 cm²."},
                        {"visual": "⭕", "text": "Radius 5 cm. Area = 3.14 × 5 × 5 = 3.14 × 25 = 78.5 cm²."},
                        {"visual": "🍕", "text": "A pizza with radius 7 cm. Area = 3.14 × 7 × 7 = 3.14 × 49 = 153.86 cm²."},
                        {"visual": "🌊", "text": "A circular pond, radius 4 m. Area = 3.14 × 4 × 4 = 3.14 × 16 = 50.24 m²."},
                    ],
                    "steps": [
                        "Find the radius of the circle.",
                        "If given the diameter, divide by 2 to get the radius.",
                        "Square the radius: r × r.",
                        "Multiply by π (use 3.14).",
                        "Example: r = 6 → 6 × 6 = 36 → 3.14 × 36 = 113.04 cm².",
                    ],
                    "fun_fact": "π (pi) has been calculated to over 100 trillion digits! But for everyday use, 3.14 is more than enough. Even NASA only uses 15 digits of pi for space navigation!",
                    "problem_config": {
                        "type": "area_circle",
                        "params": {"min_radius": 1, "max_radius": 10},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 2: Volume and Units of Measurement
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Volume and Units of Measurement",
        "description": "Learn about 3D volume and convert between measurement units",
        "order": 2,
        "lessons": [
            {
                "title": "Introduction to Volume",
                "description": "Understand volume by counting cubes inside a box",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Volume is how much space is INSIDE a box or container.\n\nThink of it like this: if you fill a lunch box with tiny cubes (1 cm × 1 cm × 1 cm), how many cubes fit inside? That number is the volume!\n\nHow to count:\n1. Count cubes along the length → that is the LENGTH.\n2. Count cubes along the width → that is the WIDTH.\n3. Count how many layers stack up → that is the HEIGHT.\n4. Multiply: length × width × height = volume.\n\nExample: A toy box is 4 cm long, 3 cm wide, and 2 cm tall.\nVolume = 4 × 3 × 2 = 24 cm³\n\nWe write cm³ (say 'cubic centimetres') because we are counting tiny cubes!",
                    "examples": [
                        {"visual": "🍱", "text": "A lunch box: 3 cm × 2 cm × 2 cm. Volume = 3 × 2 × 2 = 12 cm³."},
                        {"visual": "🧸", "text": "A toy box: 5 cm × 4 cm × 1 cm. Volume = 5 × 4 × 1 = 20 cm³."},
                        {"visual": "🎁", "text": "A gift box: 3 cm × 3 cm × 3 cm. Volume = 3 × 3 × 3 = 27 cm³."},
                        {"visual": "🧱", "text": "A brick: 4 cm × 2 cm × 3 cm. Volume = 4 × 2 × 3 = 24 cm³."},
                    ],
                    "steps": [
                        "Volume = the space inside a 3D box.",
                        "Find the length, width, and height.",
                        "Multiply: length × width = cubes in one layer.",
                        "Then multiply by height = total cubes.",
                        "Write the answer with cm³ (cubic centimetres).",
                    ],
                    "fun_fact": "A sugar cube is about 1 cm³. Your lunch box can hold about 1,000 sugar cubes — that is a volume of about 1,000 cm³!",
                    "problem_config": {
                        "type": "volume_intro",
                        "params": {"min_dim": 1, "max_dim": 5},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Volume of Boxes",
                "description": "Calculate volume of real-life box shapes using length × width × height",
                "order": 2,
                "xp_reward": 25,
                "content": {
                    "explanation": "Any box shape (shoebox, fish tank, pencil case) is called a rectangular prism.\n\nThe formula is always the same:\nVolume = length × width × height\n\nJust multiply step by step:\nStep 1: length × width (cubes in one layer)\nStep 2: result × height (stack the layers)\n\nExample: A shoebox is 8 cm long, 5 cm wide, and 3 cm tall.\nStep 1: 8 × 5 = 40\nStep 2: 40 × 3 = 120\nVolume = 120 cm³\n\nIf you know the volume and two sides, you can find the missing side:\nVolume = 60 cm³, length = 5 cm, width = 4 cm.\n5 × 4 = 20. Height = 60 ÷ 20 = 3 cm.",
                    "examples": [
                        {"visual": "👟", "text": "A shoebox: 8 cm × 5 cm × 3 cm. Step 1: 8 × 5 = 40. Step 2: 40 × 3 = 120 cm³."},
                        {"visual": "🐟", "text": "A fish tank: 6 cm × 4 cm × 3 cm. Step 1: 6 × 4 = 24. Step 2: 24 × 3 = 72 cm³."},
                        {"visual": "✏️", "text": "A pencil case: 5 cm × 3 cm × 2 cm. Step 1: 5 × 3 = 15. Step 2: 15 × 2 = 30 cm³."},
                        {"visual": "📚", "text": "A thick book: 7 cm × 5 cm × 2 cm. Step 1: 7 × 5 = 35. Step 2: 35 × 2 = 70 cm³."},
                    ],
                    "steps": [
                        "Find the length, width, and height of the box.",
                        "Step 1: Multiply length × width.",
                        "Step 2: Multiply that result × height.",
                        "Write the answer with cm³.",
                        "To find a missing side: divide the volume by the other two sides multiplied together.",
                    ],
                    "fun_fact": "An Olympic swimming pool is like a giant box: 50 m long, 25 m wide, and 2 m deep. Its volume is 50 × 25 × 2 = 2,500 m³ — that is 2,500,000 litres of water!",
                    "problem_config": {
                        "type": "volume_prism",
                        "params": {"min_dim": 2, "max_dim": 10},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Units of Length",
                "description": "Convert between millimetres, centimetres, metres, and kilometres",
                "order": 3,
                "xp_reward": 25,
                "content": {
                    "explanation": "The metric system uses these length units:\n\n1 km = 1,000 m (kilometre — for long distances)\n1 m = 100 cm (metre — for room-size things)\n1 cm = 10 mm (centimetre — for small objects)\n\nTo convert to a SMALLER unit → MULTIPLY (more small units fit).\nTo convert to a BIGGER unit → DIVIDE (fewer big units needed).\n\nExamples:\n3 m = 3 × 100 = 300 cm (smaller unit → multiply)\n5,000 m = 5,000 ÷ 1,000 = 5 km (bigger unit → divide)\n45 mm = 45 ÷ 10 = 4.5 cm",
                    "examples": [
                        {"visual": "📏", "text": "2 m = 200 cm. Multiply by 100."},
                        {"visual": "📏", "text": "350 cm = 3.5 m. Divide by 100."},
                        {"visual": "📏", "text": "4 km = 4,000 m. Multiply by 1,000."},
                        {"visual": "📏", "text": "60 mm = 6 cm. Divide by 10."},
                    ],
                    "steps": [
                        "Know the conversion: 1 km = 1,000 m, 1 m = 100 cm, 1 cm = 10 mm.",
                        "Going to a smaller unit? Multiply.",
                        "Going to a bigger unit? Divide.",
                        "Think: does the answer make sense? (Smaller units → bigger number).",
                        "Example: 7 m to cm → smaller unit → 7 × 100 = 700 cm.",
                    ],
                    "fun_fact": "The metre was originally defined in 1791 as one ten-millionth of the distance from the North Pole to the Equator. Today it is defined by the speed of light!",
                    "problem_config": {
                        "type": "unit_length",
                        "params": {},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Units of Mass and Capacity",
                "description": "Convert between grams, kilograms, millilitres, and litres",
                "order": 4,
                "xp_reward": 25,
                "content": {
                    "explanation": "Mass (weight) units:\n1 kg = 1,000 g (kilogram and gram)\n\nCapacity (liquid) units:\n1 L = 1,000 mL (litre and millilitre)\n\nSame rule as length:\n- To a SMALLER unit → MULTIPLY.\n- To a BIGGER unit → DIVIDE.\n\nExamples:\n3 kg = 3 × 1,000 = 3,000 g\n4,500 mL = 4,500 ÷ 1,000 = 4.5 L\n250 g = 250 ÷ 1,000 = 0.25 kg",
                    "examples": [
                        {"visual": "⚖️", "text": "5 kg = 5,000 g. Multiply by 1,000."},
                        {"visual": "⚖️", "text": "2,500 g = 2.5 kg. Divide by 1,000."},
                        {"visual": "🥤", "text": "3 L = 3,000 mL. Multiply by 1,000."},
                        {"visual": "🥤", "text": "750 mL = 0.75 L. Divide by 1,000."},
                    ],
                    "steps": [
                        "Know: 1 kg = 1,000 g and 1 L = 1,000 mL.",
                        "Going to a smaller unit? Multiply by 1,000.",
                        "Going to a bigger unit? Divide by 1,000.",
                        "Check: smaller unit → bigger number.",
                        "Example: 2.5 kg to g → smaller unit → 2.5 × 1,000 = 2,500 g.",
                    ],
                    "fun_fact": "A litre of water weighs exactly 1 kilogram! This is not a coincidence — the metric system was designed so that 1 mL of water = 1 g.",
                    "problem_config": {
                        "type": "unit_mass_capacity",
                        "params": {},
                        "count": 5,
                    },
                },
            },
        ],
    },

    # ═══════════════════════════════════════════════════════════════
    # CHAPTER 3: Percentages
    # ═══════════════════════════════════════════════════════════════
    {
        "title": "Percentages",
        "description": "Understand percentages and calculate simple percentages of numbers",
        "order": 3,
        "lessons": [
            {
                "title": "Introduction to Percentages",
                "description": "Learn what % means and convert between fractions and percentages",
                "order": 1,
                "xp_reward": 25,
                "content": {
                    "explanation": "Percent means 'out of 100'. The symbol is %.\n\n25% means 25 out of 100.\n\nYou already know percentages from daily life!\n- A test score of 80/100 = 80%\n- Half of something = 50%\n- All of something = 100%\n\nConverting fractions to percentages:\n1/2 = 50% (half)\n1/4 = 25% (a quarter)\n3/4 = 75% (three quarters)\n1/5 = 20% (one fifth)\n1/10 = 10% (one tenth)\n\nThe trick: divide 100 by the denominator, then multiply by the numerator.\n3/4 → 100 ÷ 4 = 25 → 25 × 3 = 75%",
                    "examples": [
                        {"visual": "🍕", "text": "You eat half a pizza. That is 1/2 = 50% of the pizza."},
                        {"visual": "📝", "text": "You score 7 out of 10 on a test. 7/10 = 70%."},
                        {"visual": "🔋", "text": "Your phone battery is at 1/4. That is 25%."},
                        {"visual": "🥛", "text": "A glass is 3/4 full. That is 75% full."},
                    ],
                    "steps": [
                        "Percent means 'out of 100'. 30% = 30 out of 100.",
                        "To convert a fraction to %: divide 100 by the bottom number.",
                        "Then multiply by the top number.",
                        "Example: 3/5 → 100 ÷ 5 = 20 → 20 × 3 = 60%.",
                        "Remember: 1/2 = 50%, 1/4 = 25%, 1/10 = 10%.",
                    ],
                    "fun_fact": "The % symbol evolved from the Italian phrase 'per cento' (per hundred). Over centuries, 'per cento' was shortened to 'p cento', then 'pc', and finally the two circles in % represent the two zeros in 100!",
                    "problem_config": {
                        "type": "percent_intro",
                        "params": {},
                        "count": 5,
                    },
                },
            },
            {
                "title": "Finding Percentages of a Number",
                "description": "Calculate a percentage of a number, like 25% of 80",
                "order": 2,
                "xp_reward": 30,
                "content": {
                    "explanation": "To find a percentage of a number, use this trick:\n\nStep 1: Find 10% first (divide by 10).\nStep 2: Use 10% to build any percentage!\n\n10% of 80 = 80 ÷ 10 = 8\n20% of 80 = 8 × 2 = 16\n50% of 80 = 80 ÷ 2 = 40\n25% of 80 = 80 ÷ 4 = 20\n\nOr use the formula:\nPercentage × number ÷ 100\n30% of 60 = 30 × 60 ÷ 100 = 1800 ÷ 100 = 18\n\nReal life: A shirt costs $40 and is 25% off.\nDiscount = 25% of 40 = 40 ÷ 4 = $10.\nYou pay $40 - $10 = $30!",
                    "examples": [
                        {"visual": "🛒", "text": "10% of 50 = 50 ÷ 10 = 5."},
                        {"visual": "💰", "text": "25% of 80 = 80 ÷ 4 = 20."},
                        {"visual": "🏷️", "text": "50% of 60 = 60 ÷ 2 = 30. That is half!"},
                        {"visual": "🎯", "text": "20% of 45 = 45 ÷ 10 = 4.5 → 4.5 × 2 = 9."},
                    ],
                    "steps": [
                        "To find 10%: divide the number by 10.",
                        "To find 50%: divide the number by 2.",
                        "To find 25%: divide the number by 4.",
                        "For other percentages: find 10% first, then multiply.",
                        "Example: 30% of 70 → 10% = 7 → 7 × 3 = 21.",
                    ],
                    "fun_fact": "Shops use percentages for sales all the time! '50% off' means you pay half. '25% off' means you save a quarter. Next time you see a sale sign, try calculating the real price in your head!",
                    "problem_config": {
                        "type": "percent_of_number",
                        "params": {},
                        "count": 5,
                    },
                },
            },
        ],
    },
]
