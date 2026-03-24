"""Rounding to the nearest 1,000 generator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("rounding_thousands")
def gen_rounding_thousands(params: dict, answer_type: str) -> dict:
    min_val = params.get("min", 1001)
    max_val = params.get("max", 9999)
    number = random.randint(min_val, max_val)

    hundreds_digit = (number % 1000) // 100
    rounded = (number // 1000) * 1000
    if hundreds_digit >= 5:
        rounded += 1000

    question = f"Round {number:,} to the nearest thousand."
    question_text = f"{number:,}\nRound to the nearest 1,000"
    answer = rounded

    if hundreds_digit >= 5:
        hint = f"The hundreds digit is {hundreds_digit} (5 or more), so round UP to {rounded:,}."
    else:
        hint = f"The hundreds digit is {hundreds_digit} (less than 5), so round DOWN to {rounded:,}."

    # Build plausible wrong options: nearby multiples of 1000
    base = (number // 1000) * 1000
    possible = sorted({base - 1000, base, base + 1000, base + 2000} - {0})
    possible = [v for v in possible if 0 < v <= 10000]
    options = list({answer} | set(possible))[:4]
    if len(options) < 4:
        options = make_options(answer, min_val=1000, max_val=10000)
    random.shuffle(options)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
