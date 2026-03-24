"""Area of triangles generator (Grade 5) — includes word problems."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

_WORD_TEMPLATES = [
    {
        "template": "{name} is making a triangular flag with base {b} cm and height {h} cm. What is the area of the flag?",
        "hint": "Area = base × height ÷ 2 = {b} × {h} ÷ 2 = {bh} ÷ 2 = {ans} cm².",
        "emoji": "🚩",
    },
    {
        "template": "A triangular garden has a base of {b} m and a height of {h} m. How many square metres is the garden?",
        "hint": "Area = {b} × {h} ÷ 2 = {bh} ÷ 2 = {ans} m².",
        "emoji": "🌿",
    },
    {
        "template": "{name} cuts a piece of paper into a triangle with base {b} cm and height {h} cm. What is the area of the triangle?",
        "hint": "Area = base × height ÷ 2 = {b} × {h} ÷ 2 = {bh} ÷ 2 = {ans} cm².",
        "emoji": "✂️",
    },
]


@register("area_triangle")
def gen_area_triangle(params: dict, answer_type: str) -> dict:
    min_base = params.get("min_base", 2)
    max_base = params.get("max_base", 16)
    min_height = params.get("min_height", 2)
    max_height = params.get("max_height", 12)

    # Ensure base × height is even so the area is a whole number
    while True:
        base = random.randint(min_base, max_base)
        height = random.randint(min_height, max_height)
        if (base * height) % 2 == 0:
            break

    area = (base * height) // 2

    variant = random.choice(["find_area", "find_area", "find_base", "word_problem"])

    if variant == "word_problem":
        name = random.choice(_NAMES)
        tmpl = random.choice(_WORD_TEMPLATES)
        question = tmpl["template"].format(name=name, b=base, h=height)
        hint = tmpl["hint"].format(b=base, h=height, bh=base * height, ans=area)
        return {
            "question": question,
            "question_text": question,
            "answer": area,
            "options": make_options(area, min_val=max(1, area - 15), max_val=area + 15),
            "hint": hint,
            "type": answer_type,
            "emoji": tmpl["emoji"],
        }

    if variant == "find_area":
        question = f"A triangle has base {base} cm and height {height} cm. What is its area?"
        question_text = f"Area = {base} cm × {height} cm ÷ 2 = ? cm²"
        answer = area
        hint = f"Area = base × height ÷ 2 = {base} × {height} ÷ 2 = {base * height} ÷ 2 = {area} cm²."
        options = make_options(answer, min_val=max(1, answer - 15), max_val=answer + 15)
    else:
        answer = base
        question = f"A triangle has area {area} cm² and height {height} cm. What is the base?"
        question_text = f"? cm × {height} cm ÷ 2 = {area} cm²"
        hint = f"Base = area × 2 ÷ height = {area} × 2 ÷ {height} = {area * 2} ÷ {height} = {base} cm."
        options = make_options(answer, min_val=max(1, answer - 5), max_val=answer + 8)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
