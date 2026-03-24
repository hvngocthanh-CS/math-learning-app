"""Comparing decimals generator (Grade 4)."""

import random

from app.features.learn.generators import register


@register("decimal_compare")
def gen_decimal_compare(params: dict, answer_type: str) -> dict:
    max_whole = params.get("max_whole", 9)

    # Generate two different decimals with one decimal place
    w1 = random.randint(0, max_whole)
    t1 = random.randint(0, 9)
    w2 = random.randint(0, max_whole)
    t2 = random.randint(0, 9)

    val1 = w1 + t1 / 10
    val2 = w2 + t2 / 10

    while val1 == val2:
        t2 = random.randint(0, 9)
        val2 = w2 + t2 / 10

    s1 = f"{w1}.{t1}"
    s2 = f"{w2}.{t2}"

    if val1 > val2:
        answer = ">"
    elif val1 < val2:
        answer = "<"
    else:
        answer = "="

    if w1 != w2:
        hint = f"Compare the whole number parts first: {w1} vs {w2}."
    else:
        hint = f"Same whole number ({w1}). Compare the tenths: {t1} vs {t2}."

    return {
        "question": f"Compare: {s1} _ {s2}",
        "question_text": f"{s1}  _  {s2}",
        "answer": answer,
        "options": [">", "<", "="],
        "hint": hint,
        "type": answer_type,
        "subtype": "comparison",
    }
