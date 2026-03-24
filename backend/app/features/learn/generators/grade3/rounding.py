"""Rounding generator for nearest 10 and 100 (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("rounding")
def gen_rounding(params: dict, answer_type: str) -> dict:
    min_val = params.get("min", 101)
    max_val = params.get("max", 999)

    number = random.randint(min_val, max_val)
    round_to = random.choice(["nearest 10", "nearest 100"])

    if round_to == "nearest 10":
        ones = number % 10
        answer = number - ones if ones < 5 else number + (10 - ones)
        look_digit = ones
        hint = f"Look at the ones digit: {ones}. {'It is 5 or more, so round UP!' if ones >= 5 else 'It is less than 5, so round DOWN!'}"
        # Options are multiples of 10 near the answer
        candidates = sorted({answer + offset * 10 for offset in [-3, -2, -1, 0, 1, 2, 3] if 0 <= answer + offset * 10 <= 1000})
        options = [answer] + [c for c in candidates if c != answer]
        options = options[:4]
        random.shuffle(options)
    else:
        tens = (number % 100) // 10
        answer = (number // 100) * 100 if tens < 5 else (number // 100 + 1) * 100
        look_digit = tens
        hint = f"Look at the tens digit: {tens}. {'It is 5 or more, so round UP!' if tens >= 5 else 'It is less than 5, so round DOWN!'}"
        # Options are multiples of 100
        candidates = sorted({answer + offset * 100 for offset in [-2, -1, 0, 1, 2] if 0 <= answer + offset * 100 <= 1000})
        options = [answer] + [c for c in candidates if c != answer]
        options = options[:4]
        random.shuffle(options)

    return {
        "question": f"Round {number} to the {round_to}.",
        "question_text": f"Round {number} to the {round_to} = ?",
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
