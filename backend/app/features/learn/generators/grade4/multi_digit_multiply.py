"""Multi-digit multiplication generator (Grade 4) — 2-digit × 1-digit."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("multi_digit_multiply")
def gen_multi_digit_multiply(params: dict, answer_type: str) -> dict:
    min_two = params.get("min_two", 11)
    max_two = params.get("max_two", 49)
    min_one = params.get("min_one", 2)
    max_one = params.get("max_one", 9)

    a = random.randint(min_two, max_two)
    b = random.randint(min_one, max_one)

    # Optionally swap display order for variety
    if random.random() < 0.5:
        display = f"{a} × {b}"
    else:
        display = f"{b} × {a}"

    answer = a * b

    # Decompose for hint
    tens_part = (a // 10) * 10
    ones_part = a % 10
    hint = (
        f"Break {a} into {tens_part} + {ones_part}. "
        f"Then: {tens_part}×{b} = {tens_part * b}, {ones_part}×{b} = {ones_part * b}. "
        f"Add them: {tens_part * b} + {ones_part * b} = {answer}."
    )

    return {
        "question": f"What is {display}?",
        "question_text": f"{display} = ?",
        "answer": answer,
        "options": make_options(answer, min_val=max(10, answer - 30), max_val=answer + 30),
        "hint": hint,
        "type": answer_type,
    }
