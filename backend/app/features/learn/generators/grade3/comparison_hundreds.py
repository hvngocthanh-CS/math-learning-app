"""Comparison generator for three-digit numbers (Grade 3)."""

import random

from app.features.learn.generators import register


@register("comparison_hundreds")
def gen_comparison_hundreds(params: dict, answer_type: str) -> dict:
    min_val = params.get("min", 100)
    max_val = params.get("max", 999)

    a = random.randint(min_val, max_val)
    # Create b that is sometimes close to a (for harder comparison)
    if random.random() < 0.4:
        # Same hundreds, differ in tens/ones
        b = (a // 100) * 100 + random.randint(0, 99)
        b = max(min_val, min(max_val, b))
    else:
        b = random.randint(min_val, max_val)

    # Avoid equal numbers most of the time
    if a == b and random.random() < 0.8:
        b = min(max_val, b + random.randint(1, 50))

    if a > b:
        answer = ">"
    elif a < b:
        answer = "<"
    else:
        answer = "="

    return {
        "question": f"Compare: {a} and {b}",
        "question_text": f"{a}  ?  {b}",
        "answer": answer,
        "options": [">", "<", "="],
        "hint": f"Compare hundreds first: {a // 100} vs {b // 100}. If same, compare tens, then ones.",
        "type": answer_type,
        "subtype": "comparison",
    }
