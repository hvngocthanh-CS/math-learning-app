"""
Shared constants used across all grade-level problem generators.
"""

EMOJI_GROUPS = [
    ("apples", "🍎"), ("stars", "🌟"), ("dogs", "🐶"), ("cats", "🐱"),
    ("fish", "🐟"), ("flowers", "🌸"), ("balloons", "🎈"), ("cookies", "🍪"),
    ("birds", "🐦"), ("frogs", "🐸"), ("hearts", "❤️"), ("bananas", "🍌"),
    ("butterflies", "🦋"), ("trees", "🌲"), ("suns", "☀️"), ("moons", "🌙"),
    ("cakes", "🎂"), ("gifts", "🎁"), ("candies", "🍬"), ("bears", "🐻"),
]

NUMBER_WORDS = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty",
}

CLOCK_EMOJIS = {
    1: "🕐", 2: "🕑", 3: "🕒", 4: "🕓", 5: "🕔", 6: "🕕",
    7: "🕖", 8: "🕗", 9: "🕘", 10: "🕙", 11: "🕚", 12: "🕛",
}

CLOCK_HALF_EMOJIS = {
    1: "🕜", 2: "🕝", 3: "🕞", 4: "🕟", 5: "🕠", 6: "🕡",
    7: "🕢", 8: "🕣", 9: "🕤", 10: "🕥", 11: "🕦", 12: "🕧",
}

SHAPE_DATA = {
    "circle": {"name": "circle", "sides": 0, "corners": 0, "emoji": "⭕",
               "real_world": ["ball", "coin", "clock face", "wheel", "pizza"]},
    "square": {"name": "square", "sides": 4, "corners": 4, "emoji": "⬜",
               "real_world": ["window", "cracker", "tile", "picture frame"]},
    "triangle": {"name": "triangle", "sides": 3, "corners": 3, "emoji": "🔺",
                 "real_world": ["pizza slice", "mountain peak", "yield sign", "roof"]},
    "rectangle": {"name": "rectangle", "sides": 4, "corners": 4, "emoji": "📱",
                  "real_world": ["door", "book", "phone screen", "table top"]},
}

SHAPE_VISUALS = {
    "circle": [
        {"emoji": "🏀", "label": "a basketball", "color": "#FB923C"},
        {"emoji": "🍪", "label": "a cookie", "color": "#FBBF24"},
        {"emoji": "☀️", "label": "the sun", "color": "#FB923C"},
        {"emoji": "🫓", "label": "a pizza", "color": "#F87171"},
        {"emoji": "⚽", "label": "a soccer ball", "color": "#6B7280"},
        {"emoji": "🎯", "label": "a target", "color": "#EF4444"},
        {"emoji": "🍩", "label": "a donut", "color": "#F472B6"},
        {"emoji": "🌕", "label": "the moon", "color": "#FBBF24"},
        {"emoji": "⏰", "label": "a clock", "color": "#60A5FA"},
        {"emoji": "🪙", "label": "a coin", "color": "#FBBF24"},
    ],
    "square": [
        {"emoji": "🖼️", "label": "a picture frame", "color": "#60A5FA"},
        {"emoji": "🧇", "label": "a waffle", "color": "#FBBF24"},
        {"emoji": "🧊", "label": "an ice cube", "color": "#60A5FA"},
        {"emoji": "🪟", "label": "a window", "color": "#60A5FA"},
        {"emoji": "🎁", "label": "a gift box", "color": "#F472B6"},
        {"emoji": "📦", "label": "a box", "color": "#A78BFA"},
        {"emoji": "🧱", "label": "a brick", "color": "#F87171"},
        {"emoji": "🎲", "label": "a dice face", "color": "#34D399"},
        {"emoji": "🟨", "label": "a sticky note", "color": "#FBBF24"},
        {"emoji": "🟩", "label": "a green tile", "color": "#34D399"},
    ],
    "triangle": [
        {"emoji": "🔺", "label": "a triangle sign", "color": "#EF4444"},
        {"emoji": "🍕", "label": "a pizza slice", "color": "#F87171"},
        {"emoji": "🏔️", "label": "a mountain", "color": "#6B7280"},
        {"emoji": "⛺", "label": "a tent", "color": "#34D399"},
        {"emoji": "🎄", "label": "a Christmas tree", "color": "#22C55E"},
        {"emoji": "📐", "label": "a ruler triangle", "color": "#60A5FA"},
        {"emoji": "🧀", "label": "a cheese wedge", "color": "#FBBF24"},
        {"emoji": "🔻", "label": "an arrow pointing down", "color": "#A78BFA"},
        {"emoji": "⚠️", "label": "a warning sign", "color": "#FBBF24"},
        {"emoji": "🛖", "label": "a hut", "color": "#F472B6"},
    ],
    "rectangle": [
        {"emoji": "🚪", "label": "a door", "color": "#A78BFA"},
        {"emoji": "📚", "label": "a book", "color": "#60A5FA"},
        {"emoji": "📱", "label": "a phone", "color": "#6B7280"},
        {"emoji": "💵", "label": "a dollar bill", "color": "#34D399"},
        {"emoji": "🎹", "label": "a piano key", "color": "#6B7280"},
        {"emoji": "🍫", "label": "a chocolate bar", "color": "#A78BFA"},
        {"emoji": "✉️", "label": "an envelope", "color": "#60A5FA"},
        {"emoji": "🖥️", "label": "a computer monitor", "color": "#6B7280"},
        {"emoji": "📺", "label": "a TV", "color": "#A78BFA"},
        {"emoji": "📋", "label": "a clipboard", "color": "#60A5FA"},
    ],
}

# Each pair: (big_item, small_item, question_word)
# Grouped so the question always makes sense for the pair.
SIZE_BIGGER = [
    ("elephant 🐘", "mouse 🐭"),
    ("whale 🐋", "fish 🐟"),
    ("bus 🚌", "bike 🚲"),
    ("airplane ✈️", "bird 🐦"),
    ("basketball 🏀", "golf ball ⚾"),
    ("watermelon 🍉", "strawberry 🍓"),
    ("bear 🐻", "rabbit 🐰"),
    ("truck 🚛", "skateboard 🛹"),
]

SIZE_TALLER = [
    ("giraffe 🦒", "dog 🐶"),
    ("tree 🌲", "flower 🌸"),
    ("building 🏢", "house 🏠"),
    ("adult 🧑", "baby 👶"),
    ("sunflower 🌻", "mushroom 🍄"),
    ("lighthouse 🗼", "tent ⛺"),
]

SIZE_LONGER = [
    ("train 🚂", "car 🚗"),
    ("school bus 🚌", "pencil ✏️"),
    ("river 🏞️", "pond 💧"),
    ("snake 🐍", "worm 🪱"),
    ("bridge 🌉", "bench 🪑"),
    ("scarf 🧣", "sock 🧦"),
]

PATTERN_SETS = [
    ("🔴", "🔵"), ("⭐", "🌙"), ("🍎", "🍌"), ("🔺", "⬜"),
    ("😀", "😢"), ("🌸", "🌼"), ("🐱", "🐶"), ("❤️", "💙"),
    ("🌞", "🌧️"), ("🍓", "🫐"),
]
