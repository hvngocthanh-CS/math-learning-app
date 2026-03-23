"""Place value generator (Grade 1)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("place_value")
def gen_place_value(params: dict, answer_type: str) -> dict:
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
            "options": make_options(tens, min_val=0, max_val=3),
            "hint": f"Look at the left digit of {n}.",
            "type": answer_type,
        }
    elif q_type == "ones":
        return {
            "question": f"How many ones in {n}?",
            "question_text": f"The number {n} has how many ones?",
            "answer": ones,
            "options": make_options(ones, min_val=0, max_val=9),
            "hint": f"Look at the right digit of {n}.",
            "type": answer_type,
        }
    else:
        return {
            "question": f"{tens} ten(s) + {ones} one(s) = ?",
            "question_text": f"What number is {tens} ten(s) and {ones} one(s)?",
            "answer": n,
            "options": make_options(n, min_val=min_n - 2, max_val=max_n + 2),
            "hint": f"{tens} × 10 + {ones} = ?",
            "type": answer_type,
        }
