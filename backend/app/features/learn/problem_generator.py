"""
Random problem generator for MathQuest.
Each lesson stores a problem_config (JSON) that describes what type of problems to generate.
Every time a student opens Practice or Quiz, fresh random problems are created.
"""

import random
from typing import List, Dict, Any

# Emoji pools for visual problems
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

SIZE_PAIRS = [
    ("elephant 🐘", "mouse 🐭", "bigger"), ("tree 🌲", "flower 🌸", "taller"),
    ("train 🚂", "car 🚗", "longer"), ("basketball 🏀", "golf ball ⚾", "bigger"),
    ("giraffe 🦒", "dog 🐶", "taller"), ("bus 🚌", "bike 🚲", "bigger"),
    ("school bus 🚌", "pencil ✏️", "longer"), ("horse 🐴", "cat 🐱", "taller"),
    ("whale 🐋", "fish 🐟", "bigger"), ("building 🏢", "house 🏠", "taller"),
    ("airplane ✈️", "bird 🐦", "bigger"), ("river 🏞️", "pond 💧", "longer"),
]

PATTERN_SETS = [
    ("🔴", "🔵"), ("⭐", "🌙"), ("🍎", "🍌"), ("🔺", "⬜"),
    ("😀", "😢"), ("🌸", "🌼"), ("🐱", "🐶"), ("❤️", "💙"),
    ("🌞", "🌧️"), ("🍓", "🫐"),
]


def _make_options(answer: int, count: int = 4, min_val: int = 0, max_val: int = 20) -> List[int]:
    """Generate multiple choice options that include the correct answer."""
    options = {answer}
    attempts = 0
    while len(options) < count and attempts < 50:
        # Generate distractors near the answer
        offset = random.choice([-2, -1, 1, 2, -3, 3])
        val = answer + offset
        if min_val <= val <= max_val and val != answer:
            options.add(val)
        attempts += 1
    # Fill remaining with random values if needed
    while len(options) < count:
        val = random.randint(min_val, max_val)
        if val != answer:
            options.add(val)
    result = list(options)
    random.shuffle(result)
    return result


def generate_problems(config: Dict[str, Any], mode: str = "practice") -> List[Dict]:
    """
    Generate random problems based on config.
    mode: "practice" (free_input) or "quiz" (multiple_choice)
    """
    problem_type = config["type"]
    params = config.get("params", {})
    count = config.get("count", 5)
    answer_type = "free_input" if mode == "practice" else "multiple_choice"

    generators = {
        "counting": _gen_counting,
        "number_recognition": _gen_number_recognition,
        "number_sequence": _gen_number_sequence,
        "addition": _gen_addition,
        "subtraction": _gen_subtraction,
        "comparison": _gen_comparison,
        "comparison_full": _gen_comparison_full,
        "ordering": _gen_ordering,
        "place_value": _gen_place_value,
        "shape_properties": _gen_shape_properties,
        "pattern": _gen_pattern,
        "size_comparison": _gen_size_comparison,
        "time_reading": _gen_time_reading,
    }

    generator = generators.get(problem_type)
    if not generator:
        return []

    # Shape: pre-select unique problems to guarantee variety
    if problem_type == "shape_properties":
        shapes = params.get("shapes", ["circle", "square"])

        # Image-based questions (identify shape from emoji object)
        img_pool = []
        for s in shapes:
            for v in SHAPE_VISUALS.get(s, []):
                img_pool.append((s, v))
        random.shuffle(img_pool)

        if answer_type == "free_input":
            # Practice: all 5 are image-based
            selected = img_pool[:count]
            problems = []
            for shape_key, visual in selected:
                shape = SHAPE_DATA[shape_key]
                problems.append({
                    "question": f"What shape is {visual['label']}?",
                    "question_text": visual["emoji"],
                    "answer": shape["name"],
                    "options": [SHAPE_DATA[s]["name"] for s in shapes],
                    "hint": f"A {shape['name']} has {shape['sides']} sides and {shape['corners']} corners." if shape["sides"] > 0 else f"A {shape['name']} is round with no corners.",
                    "type": answer_type,
                    "subtype": "shape_identify",
                    "shape_emoji": visual["emoji"],
                    "shape_color": visual["color"],
                    "shape_label": visual["label"],
                })
            return problems
        else:
            # Quiz: mix of image questions (3) + sides/corners questions (2)
            problems = []

            # 3 image-based questions
            for shape_key, visual in img_pool[:3]:
                shape = SHAPE_DATA[shape_key]
                problems.append({
                    "question": f"What shape is {visual['label']}?",
                    "question_text": visual["emoji"],
                    "answer": shape["name"],
                    "options": [SHAPE_DATA[s]["name"] for s in shapes],
                    "hint": f"Think about what {visual['label']} looks like.",
                    "type": answer_type,
                    "subtype": "shape_identify",
                    "shape_emoji": visual["emoji"],
                    "shape_color": visual["color"],
                    "shape_label": visual["label"],
                })

            # 2 sides/corners questions (one of each, different shapes)
            props_types = ["sides", "corners"]
            random.shuffle(props_types)
            used_shapes = list(shapes)
            random.shuffle(used_shapes)
            for i, q_type in enumerate(props_types):
                shape_key = used_shapes[i % len(used_shapes)]
                shape = SHAPE_DATA[shape_key]
                if q_type == "sides":
                    problems.append({
                        "question": f"How many sides does a {shape['name']} have?",
                        "question_text": f"A {shape['name']} {shape['emoji']} has how many sides?",
                        "answer": shape["sides"],
                        "options": _make_options(shape["sides"], min_val=0, max_val=6),
                        "hint": f"Count each straight edge of a {shape['name']}." if shape["sides"] > 0 else f"A {shape['name']} is round with no straight sides.",
                        "type": answer_type,
                    })
                else:
                    problems.append({
                        "question": f"How many corners does a {shape['name']} have?",
                        "question_text": f"A {shape['name']} {shape['emoji']} has how many corners?",
                        "answer": shape["corners"],
                        "options": _make_options(shape["corners"], min_val=0, max_val=6),
                        "hint": f"Count where the sides meet." if shape["corners"] > 0 else f"A {shape['name']} has no corners - it is smooth and round.",
                        "type": answer_type,
                    })

            random.shuffle(problems)
            return problems

    problems = []
    seen = set()
    attempts = 0
    while len(problems) < count and attempts < count * 10:
        problem = generator(params, answer_type)
        # Deduplicate by answer + question_text
        key = (problem["answer"], problem["question_text"])
        if key not in seen:
            seen.add(key)
            problems.append(problem)
        attempts += 1

    return problems


# ─── Individual generators ───────────────────────────────────────────

def _gen_counting(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    n = random.randint(min_n, max_n)
    name, emoji = random.choice(EMOJI_GROUPS)
    visual = emoji * n
    return {
        "question": f"How many {name}?",
        "question_text": f"Count the {name}: {visual}",
        "answer": n,
        "options": _make_options(n, min_val=max(0, min_n - 1), max_val=max_n + 1),
        "hint": f"Point to each {name[:-1] if name.endswith('s') else name} and count carefully.",
        "type": answer_type,
    }


def _gen_number_recognition(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    n = random.randint(min_n, max_n)
    word = NUMBER_WORDS.get(n, str(n))
    name, emoji = random.choice(EMOJI_GROUPS)
    visual = emoji * n

    if answer_type == "multiple_choice":
        # Quiz: 4 variants including word answers
        variant = random.choice(["visual_to_number", "visual_to_word", "word_to_number", "number_to_word"])
    else:
        # Practice (free_input): only number answers
        variant = random.choice(["visual_to_number", "word_to_number"])

    if variant == "visual_to_number":
        return {
            "question": "Count and choose the number!",
            "question_text": visual,
            "answer": n,
            "options": _make_options(n, min_val=max(0, min_n - 1), max_val=max_n + 1),
            "hint": f"Point to each {name[:-1] if name.endswith('s') else name} and count.",
            "type": answer_type,
        }
    elif variant == "visual_to_word":
        word_options = _make_word_options(word, min_n, max_n)
        return {
            "question": "Count and choose the word!",
            "question_text": visual,
            "answer": word,
            "options": word_options,
            "hint": f"Count the {name}, then find the matching word.",
            "type": answer_type,
        }
    elif variant == "word_to_number":
        return {
            "question": f"What number is '{word}'?",
            "question_text": f"What number is the word '{word}'?",
            "answer": n,
            "options": _make_options(n, min_val=min_n, max_val=max_n),
            "hint": f"'{word.capitalize()}' comes after '{NUMBER_WORDS.get(n-1, '')}'.",
            "type": answer_type,
        }
    else:
        word_options = _make_word_options(word, min_n, max_n)
        return {
            "question": f"The number {n} is called...",
            "question_text": f"What is the word for the number {n}?",
            "answer": word,
            "options": word_options,
            "hint": f"Count up: {', '.join(NUMBER_WORDS.get(i, str(i)) for i in range(max(1,n-2), n+1))}.",
            "type": answer_type,
        }


def _make_word_options(correct_word: str, min_n: int, max_n: int, count: int = 4) -> list:
    """Generate word options for multiple choice, including the correct answer."""
    word_options = {correct_word}
    while len(word_options) < count:
        rand_n = random.randint(min_n, max_n)
        word_options.add(NUMBER_WORDS.get(rand_n, str(rand_n)))
    result = list(word_options)
    random.shuffle(result)
    return result


def _gen_number_sequence(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    # Generate a sequence with one missing
    start = random.randint(min_n, max(min_n, max_n - 3))
    length = min(4, max_n - start + 1)
    seq = list(range(start, start + length))
    missing_idx = random.randint(0, len(seq) - 1)
    answer = seq[missing_idx]
    display = [str(x) if i != missing_idx else "_" for i, x in enumerate(seq)]
    seq_str = ", ".join(display)
    return {
        "question": f"Fill in: {seq_str}",
        "question_text": f"What is the missing number? {seq_str}",
        "answer": answer,
        "options": _make_options(answer, min_val=min_n, max_val=max_n),
        "hint": f"Count in order. What goes between {answer-1} and {answer+1}?" if min_n < answer < max_n else "Think about the counting order.",
        "type": answer_type,
    }


def _gen_addition(params: dict, answer_type: str) -> dict:
    min_a = params.get("min_a", 0)
    max_a = params.get("max_a", 5)
    min_b = params.get("min_b", 0)
    max_b = params.get("max_b", 5)
    max_sum = params.get("max_sum", 10)

    for _ in range(50):
        a = random.randint(min_a, max_a)
        b = random.randint(min_b, max_b)
        if a + b <= max_sum:
            break
    answer = a + b

    # Sometimes show with emojis
    use_emoji = random.random() < 0.4
    if use_emoji and answer <= 10:
        name, emoji = random.choice(EMOJI_GROUPS)
        visual_a = emoji * a if a > 0 else "nothing"
        visual_b = emoji * b if b > 0 else "nothing"
        question = f"{visual_a} + {visual_b} = ?"
        question_text = f"What is {a} + {b}?"
        hint = f"Count all the {name} together: {a} and {b} more."
    else:
        question = f"What is {a} + {b}?"
        question_text = f"Solve: {a} + {b} = ?"
        if a >= 8 or b >= 8:
            hint = f"Try 'make 10': {a} + {10-a} = 10, then add {b-(10-a)} more." if a < 10 and b > 0 else f"Start at {a} and count {b} more."
        else:
            hint = f"Start at {max(a,b)} and count {min(a,b)} more."

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": _make_options(answer, min_val=0, max_val=max_sum + 2),
        "hint": hint,
        "type": answer_type,
    }


def _gen_subtraction(params: dict, answer_type: str) -> dict:
    min_start = params.get("min_start", 2)
    max_start = params.get("max_start", 10)

    a = random.randint(min_start, max_start)
    b = random.randint(0, a)
    answer = a - b

    use_emoji = random.random() < 0.4
    if use_emoji and a <= 10:
        name, emoji = random.choice(EMOJI_GROUPS)
        visual = emoji * a
        question = f"{visual} take away {emoji * b if b > 0 else 'none'} = ?"
        question_text = f"What is {a} - {b}?"
        hint = f"Start with {a} {name}, take away {b}."
    else:
        question = f"What is {a} - {b}?"
        question_text = f"Solve: {a} - {b} = ?"
        hint = f"Start at {a} and count back {b}." if b > 0 else f"Taking away zero means nothing changes!"

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": _make_options(answer, min_val=0, max_val=max_start),
        "hint": hint,
        "type": answer_type,
    }


def _gen_comparison(params: dict, answer_type: str) -> dict:
    """Generate comparison problems. Practice: pick > or <. Quiz: pick bigger/smaller number."""
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)

    a = random.randint(min_n, max_n)
    b = random.randint(min_n, max_n)
    while a == b:
        b = random.randint(min_n, max_n)

    if answer_type == "multiple_choice":
        # Quiz: ask which number is bigger or smaller
        ask_bigger = random.choice([True, False])
        if ask_bigger:
            answer = max(a, b)
            question = "Which number is larger?"
            hint = f"Count up: the number you reach later is larger."
        else:
            answer = min(a, b)
            question = "Which number is smaller?"
            hint = f"Count up: the number you reach first is smaller."
        return {
            "question": question,
            "question_text": f"{a} and {b}",
            "answer": answer,
            "options": [a, b],
            "hint": hint,
            "type": answer_type,
            "subtype": "comparison_pick",
        }
    else:
        # Practice: pick > or <
        if a > b:
            answer = ">"
            hint = f"{a} is bigger than {b}, so the alligator mouth opens toward {a}."
        else:
            answer = "<"
            hint = f"{a} is smaller than {b}."
        return {
            "question": f"Which sign goes between {a} and {b}?",
            "question_text": f"{a} ? {b}",
            "answer": answer,
            "options": [">", "<"],
            "hint": hint,
            "type": answer_type,
            "subtype": "comparison",
        }


def _gen_comparison_full(params: dict, answer_type: str) -> dict:
    """Generate >, <, or = comparison problems."""
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)

    choice = random.choice(["greater", "less", "equal"])
    if choice == "equal":
        n = random.randint(min_n, max_n)
        a, b = n, n
        answer = "="
        hint = f"Both numbers are {n}. They are equal!"
    else:
        a = random.randint(min_n, max_n)
        b = random.randint(min_n, max_n)
        while a == b:
            b = random.randint(min_n, max_n)
        answer = ">" if a > b else "<"
        hint = f"{a} is {'bigger' if a > b else 'smaller'} than {b}."

    if answer_type == "multiple_choice":
        # Quiz: show visual emoji quantities
        _, emoji_a = random.choice(EMOJI_GROUPS)
        _, emoji_b = random.choice(EMOJI_GROUPS)
        visual_a = emoji_a * a
        visual_b = emoji_b * b
        return {
            "question": "Compare the two groups! Which sign goes in between?",
            "question_text": f"{visual_a}  ?  {visual_b}",
            "answer": answer,
            "options": [">", "<", "="],
            "hint": hint,
            "type": answer_type,
            "subtype": "comparison_visual",
        }

    return {
        "question": f"Which sign goes between {a} and {b}?",
        "question_text": f"{a} ? {b}",
        "answer": answer,
        "options": [">", "<", "="],
        "hint": hint,
        "type": answer_type,
        "subtype": "comparison",
    }


def _gen_ordering(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    num_count = params.get("count", 3)

    numbers = random.sample(range(min_n, max_n + 1), min(num_count, max_n - min_n + 1))
    numbers_str = ", ".join(str(n) for n in numbers)

    q_type = random.choice(["smallest", "biggest", "middle"])
    sorted_nums = sorted(numbers)

    if q_type == "smallest":
        answer = sorted_nums[0]
        question_text = f"Which is the smallest: {numbers_str}?"
        hint = "Find the number closest to 1."
    elif q_type == "biggest":
        answer = sorted_nums[-1]
        question_text = f"Which is the biggest: {numbers_str}?"
        hint = "Find the largest number."
    else:
        if len(sorted_nums) >= 3:
            answer = sorted_nums[len(sorted_nums) // 2]
            question_text = f"What is the middle number when ordering {numbers_str}?"
            hint = f"Order them: {', '.join(str(n) for n in sorted_nums)}. The middle one is..."
        else:
            answer = sorted_nums[0]
            question_text = f"Which is the smallest: {numbers_str}?"
            hint = "Find the number closest to 1."

    return {
        "question": question_text,
        "question_text": question_text,
        "answer": answer,
        "options": _make_options(answer, min_val=min_n, max_val=max_n),
        "hint": hint,
        "type": answer_type,
    }


def _gen_place_value(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 11)
    max_n = params.get("max", 20)
    n = random.randint(min_n, max_n)
    tens = n // 10
    ones = n % 10

    q_type = random.choice(["tens", "ones", "compose"])
    if q_type == "tens":
        return {
            "question": f"How many tens in {n}?",
            "question_text": f"The number {n} has how many tens?",
            "answer": tens,
            "options": _make_options(tens, min_val=0, max_val=3),
            "hint": f"Look at the left digit of {n}.",
            "type": answer_type,
        }
    elif q_type == "ones":
        return {
            "question": f"How many ones in {n}?",
            "question_text": f"The number {n} has how many ones?",
            "answer": ones,
            "options": _make_options(ones, min_val=0, max_val=9),
            "hint": f"Look at the right digit of {n}.",
            "type": answer_type,
        }
    else:
        return {
            "question": f"{tens} ten(s) + {ones} one(s) = ?",
            "question_text": f"What number is {tens} ten(s) and {ones} one(s)?",
            "answer": n,
            "options": _make_options(n, min_val=min_n - 2, max_val=max_n + 2),
            "hint": f"{tens} × 10 + {ones} = ?",
            "type": answer_type,
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


def _gen_shape_properties(params: dict, answer_type: str) -> dict:
    shapes = params.get("shapes", ["circle", "square"])
    shape_key = random.choice(shapes)
    shape = SHAPE_DATA[shape_key]

    if answer_type == "free_input":
        # Practice: show one object, pick circle or square
        visual = random.choice(SHAPE_VISUALS.get(shape_key, [{"emoji": "🔷", "label": "", "color": "#A78BFA"}]))
        return {
            "question": f"What shape is {visual['label']}?",
            "question_text": visual["emoji"],
            "answer": shape["name"],
            "options": [SHAPE_DATA[s]["name"] for s in shapes],
            "hint": f"A {shape['name']} has {shape['sides']} sides and {shape['corners']} corners." if shape["sides"] > 0 else f"A {shape['name']} is round with no corners.",
            "type": answer_type,
            "subtype": "shape_identify",
            "shape_emoji": visual["emoji"],
            "shape_color": visual["color"],
            "shape_label": visual["label"],
        }

    q_type = random.choice(["sides", "corners", "identify"])
    if q_type == "sides":
        return {
            "question": f"How many sides does a {shape['name']} have?",
            "question_text": f"A {shape['name']} {shape['emoji']} has how many sides?",
            "answer": shape["sides"],
            "options": _make_options(shape["sides"], min_val=0, max_val=6),
            "hint": f"Count each straight edge of a {shape['name']}." if shape["sides"] > 0 else f"A {shape['name']} is round with no straight sides.",
            "type": answer_type,
        }
    elif q_type == "corners":
        return {
            "question": f"How many corners does a {shape['name']} have?",
            "question_text": f"A {shape['name']} {shape['emoji']} has how many corners?",
            "answer": shape["corners"],
            "options": _make_options(shape["corners"], min_val=0, max_val=6),
            "hint": f"Count where the sides meet." if shape["corners"] > 0 else f"A {shape['name']} has no corners - it is smooth and round.",
            "type": answer_type,
        }
    else:
        item = random.choice(shape["real_world"])
        choices_str = ", ".join(f"{SHAPE_DATA[s]['sides']}={s}" for s in shapes)
        return {
            "question": f"A {item} is shaped like a ___",
            "question_text": f"What shape is a {item}? ({choices_str})",
            "answer": shape["sides"],
            "options": sorted(set(SHAPE_DATA[s]["sides"] for s in shapes)),
            "hint": f"Think about what a {item} looks like.",
            "type": answer_type,
        }


def _gen_pattern(params: dict, answer_type: str) -> dict:
    a_emoji, b_emoji = random.choice(PATTERN_SETS)
    length = random.randint(4, 6)
    pattern = [a_emoji if i % 2 == 0 else b_emoji for i in range(length)]
    answer_emoji = a_emoji if length % 2 == 0 else b_emoji
    pattern_str = " ".join(pattern)

    return {
        "question": "What comes next in the pattern?",
        "question_text": pattern_str + " ❓",
        "answer": answer_emoji,
        "options": [a_emoji, b_emoji],
        "hint": f"{a_emoji} and {b_emoji} take turns. After {'A' if pattern[-1] == a_emoji else 'B'} comes {'B' if pattern[-1] == a_emoji else 'A'}.",
        "type": answer_type,
        "subtype": "pattern_pick",
    }


def _gen_size_comparison(params: dict, answer_type: str) -> dict:
    item_a, item_b, relation = random.choice(SIZE_PAIRS)
    # Randomly ask "which is bigger" or "which is smaller"
    ask_bigger = random.choice([True, False])

    if ask_bigger:
        word = relation  # bigger/taller/longer
        answer = 1  # first item is always the bigger one in SIZE_PAIRS
        question_text = f"Which is {word}: {item_a} or {item_b}? (1=first, 2=second)"
        hint = f"{item_a.split()[0]} is much {word} than {item_b.split()[0]}!"
    else:
        opposite = {"bigger": "smaller", "taller": "shorter", "longer": "shorter"}
        word = opposite[relation]
        answer = 2  # second item is smaller
        question_text = f"Which is {word}: {item_a} or {item_b}? (1=first, 2=second)"
        hint = f"{item_b.split()[0]} is much {word} than {item_a.split()[0]}!"

    return {
        "question": question_text,
        "question_text": question_text,
        "answer": answer,
        "options": [1, 2],
        "hint": hint,
        "type": answer_type,
    }


def _gen_time_reading(params: dict, answer_type: str) -> dict:
    hours = params.get("hours", list(range(1, 13)))
    hour = random.choice(hours)
    emoji = CLOCK_EMOJIS.get(hour, "🕐")

    return {
        "question": f"{emoji} What time is it?",
        "question_text": f"The short hand points to {hour}, long hand to 12. What hour is it?",
        "answer": hour,
        "options": _make_options(hour, min_val=1, max_val=12),
        "hint": f"Look at where the short hand points.",
        "type": answer_type,
    }
