"""Even and odd number generator (Grade 2)."""

import random

from app.features.learn.generators import register


@register("even_odd")
def gen_even_odd(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 20)
    n = random.randint(min_n, max_n)
    answer = "even" if n % 2 == 0 else "odd"

    return {
        "question": f"Is {n} even or odd?",
        "question_text": f"Is the number {n} even or odd?",
        "answer": answer,
        "options": ["even", "odd"],
        "hint": f"Even numbers can be split into 2 equal groups. Can you split {n} into 2 equal groups?" if n <= 10 else f"Even numbers end in 0, 2, 4, 6, or 8. What does {n} end in?",
        "type": answer_type,
        "subtype": "even_odd",
    }
