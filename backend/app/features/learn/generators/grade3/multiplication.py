"""Multiplication tables generator (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("multiplication")
def gen_multiplication(params: dict, answer_type: str) -> dict:
    tables = params.get("tables", [2, 3, 4, 5])
    max_factor = params.get("max_factor", 10)

    a = random.choice(tables)
    b = random.randint(1, max_factor)

    # Randomly swap order for variety
    if random.random() < 0.5:
        a, b = b, a

    answer = a * b

    question = f"What is {a} × {b}?"
    question_text = f"{a} × {b} = ?"
    hint = f"Think: {a} groups of {b}. Or count by {b}s, {a} times!"

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": make_options(answer, min_val=max(0, answer - 10), max_val=answer + 10),
        "hint": hint,
        "type": answer_type,
    }
