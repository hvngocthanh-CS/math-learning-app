"""Area of rectangles and squares generator (Grade 5) — includes word problems."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

_WORD_TEMPLATES = [
    {
        "template": "{name} is painting a rectangular wall that is {l} m long and {w} m tall. How many square metres of paint are needed?",
        "hint": "Area = length × width = {l} × {w} = {ans} m².",
        "emoji": "🎨",
    },
    {
        "template": "A rectangular room is {l} m long and {w} m wide. How many square metres of carpet are needed to cover the floor?",
        "hint": "Area = {l} × {w} = {ans} m².",
        "emoji": "🏠",
    },
    {
        "template": "{name} has a rectangular garden that is {l} m long and {w} m wide. What is the area of the garden?",
        "hint": "Area = length × width = {l} × {w} = {ans} m².",
        "emoji": "🌿",
    },
    {
        "template": "A square playground has sides of {l} m. What is the area of the playground?",
        "hint": "Area of a square = side × side = {l} × {l} = {ans} m².",
        "emoji": "🏃",
        "square": True,
    },
]


@register("area_rectangle")
def gen_area_rectangle(params: dict, answer_type: str) -> dict:
    min_side = params.get("min_side", 2)
    max_side = params.get("max_side", 15)

    variant = random.choice(["find_area", "find_area", "find_side", "word_problem"])

    if variant == "word_problem":
        name = random.choice(_NAMES)
        tmpl = random.choice(_WORD_TEMPLATES)
        if tmpl.get("square"):
            side = random.randint(min_side, max_side)
            answer = side * side
            question = tmpl["template"].format(name=name, l=side, w=side)
            question_text = question
            hint = tmpl["hint"].format(l=side, w=side, ans=answer)
        else:
            length = random.randint(min_side + 2, max_side)
            width = random.randint(min_side, length)
            answer = length * width
            question = tmpl["template"].format(name=name, l=length, w=width)
            question_text = question
            hint = tmpl["hint"].format(l=length, w=width, ans=answer)
        options = make_options(answer, min_val=max(1, answer - 20), max_val=answer + 20)
        return {
            "question": question,
            "question_text": question_text,
            "answer": answer,
            "options": options,
            "hint": hint,
            "type": answer_type,
            "emoji": tmpl["emoji"],
        }

    if variant == "find_area":
        is_square = random.choice([True, False])
        if is_square:
            side = random.randint(min_side, max_side)
            answer = side * side
            question = f"A square has side {side} cm. What is its area?"
            question_text = f"Area = {side} cm × {side} cm = ? cm²"
            hint = f"Area of a square = side × side = {side} × {side} = {answer} cm²."
        else:
            length = random.randint(min_side, max_side)
            width = random.randint(min_side, max_side)
            answer = length * width
            question = f"A rectangle has length {length} cm and width {width} cm. What is its area?"
            question_text = f"Area = {length} cm × {width} cm = ? cm²"
            hint = f"Area = length × width = {length} × {width} = {answer} cm²."
        options = make_options(answer, min_val=max(1, answer - 20), max_val=answer + 20)
    else:
        known_side = random.randint(min_side, max_side)
        answer = random.randint(min_side, max_side)
        area = known_side * answer
        if random.choice([True, False]):
            question = f"A rectangle has area {area} cm² and length {known_side} cm. What is the width?"
            question_text = f"{known_side} cm × ? cm = {area} cm²"
            hint = f"Width = area ÷ length = {area} ÷ {known_side} = {answer} cm."
        else:
            question = f"A rectangle has area {area} cm² and width {known_side} cm. What is the length?"
            question_text = f"? cm × {known_side} cm = {area} cm²"
            hint = f"Length = area ÷ width = {area} ÷ {known_side} = {answer} cm."
        options = make_options(answer, min_val=max(1, answer - 5), max_val=answer + 8)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
