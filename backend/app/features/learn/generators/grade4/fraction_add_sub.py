"""Adding and subtracting fractions with same denominator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import fraction_svg


def _make_fraction_options_simple(answer_n: int, answer_d: int, count: int = 4) -> list:
    """Generate fraction string options for same-denominator problems."""
    correct = f"{answer_n}/{answer_d}"
    options = {correct}
    attempts = 0
    while len(options) < count and attempts < 50:
        n = random.randint(1, answer_d - 1)
        frac = f"{n}/{answer_d}"
        if frac != correct:
            options.add(frac)
        # Also try with different denominator
        if len(options) < count:
            d2 = random.choice([d for d in [2, 3, 4, 6, 8] if d != answer_d and d >= 2])
            n2 = random.randint(1, d2 - 1)
            options.add(f"{n2}/{d2}")
        attempts += 1
    result = list(options)[:count]
    random.shuffle(result)
    return result


@register("fraction_add_sub")
def gen_fraction_add_sub(params: dict, answer_type: str) -> dict:
    denominators = params.get("denominators", [2, 3, 4, 6, 8])
    d = random.choice(denominators)

    # Subtraction needs d >= 3 so we can have n1 >= 2
    op = random.choice(["add", "subtract"]) if d >= 3 else "add"

    if op == "add":
        # Ensure sum < denominator (proper fraction result)
        max_n1 = d - 2
        if max_n1 < 1:
            max_n1 = 1
        n1 = random.randint(1, max_n1)
        n2 = random.randint(1, d - 1 - n1) if d - 1 - n1 >= 1 else 1
        result_n = n1 + n2
        symbol = "+"
        question = f"What is {n1}/{d} + {n2}/{d}?"
        question_text = f"{n1}/{d}  +  {n2}/{d}  = ?"
        hint = f"Same denominator! Just add the numerators: {n1} + {n2} = {result_n}. Answer: {result_n}/{d}."
    else:
        # Ensure positive result
        n1 = random.randint(2, d - 1)
        n2 = random.randint(1, n1 - 1)
        result_n = n1 - n2
        symbol = "-"
        question = f"What is {n1}/{d} - {n2}/{d}?"
        question_text = f"{n1}/{d}  -  {n2}/{d}  = ?"
        hint = f"Same denominator! Just subtract the numerators: {n1} - {n2} = {result_n}. Answer: {result_n}/{d}."

    answer = f"{result_n}/{d}"

    svg1 = fraction_svg(n1, d)
    svg2 = fraction_svg(n2, d)

    return {
        "question": question,
        "question_text": question_text,
        "image_left": svg1,
        "image_right": svg2,
        "answer": answer,
        "options": _make_fraction_options_simple(result_n, d),
        "hint": hint,
        "type": answer_type,
        "subtype": "fraction_input",
    }
