"""Perimeter generator (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("perimeter")
def gen_perimeter(params: dict, answer_type: str) -> dict:
    shapes = params.get("shapes", ["square", "rectangle", "triangle"])
    min_side = params.get("min_side", 2)
    max_side = params.get("max_side", 15)

    shape = random.choice(shapes)

    if shape == "square":
        side = random.randint(min_side, max_side)
        answer = 4 * side
        question = f"A square has sides of length {side}. What is the perimeter?"
        question_text = f"⬜ Square: side = {side}\nPerimeter = ?"
        hint = f"A square has 4 equal sides. Perimeter = 4 × {side}."
        max_opt = 4 * max_side + 10
    elif shape == "rectangle":
        length = random.randint(min_side + 2, max_side)
        width = random.randint(min_side, length - 1)
        answer = 2 * length + 2 * width
        question = f"A rectangle is {length} long and {width} wide. What is the perimeter?"
        question_text = f"✉️ Rectangle: length = {length}, width = {width}\nPerimeter = ?"
        hint = f"Perimeter = {length} + {width} + {length} + {width}. Add all four sides!"
        max_opt = 2 * max_side + 2 * max_side + 10
    else:  # triangle
        s1 = random.randint(min_side, max_side)
        s2 = random.randint(min_side, max_side)
        # Ensure valid triangle: third side < sum of other two
        s3 = random.randint(max(min_side, abs(s1 - s2) + 1), min(max_side, s1 + s2 - 1))
        answer = s1 + s2 + s3
        question = f"A triangle has sides of {s1}, {s2}, and {s3}. What is the perimeter?"
        question_text = f"📐 Triangle: sides = {s1}, {s2}, {s3}\nPerimeter = ?"
        hint = f"Add all three sides: {s1} + {s2} + {s3}."
        max_opt = 3 * max_side + 10

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": make_options(answer, min_val=max(0, answer - 10), max_val=min(max_opt, answer + 10)),
        "hint": hint,
        "type": answer_type,
    }
