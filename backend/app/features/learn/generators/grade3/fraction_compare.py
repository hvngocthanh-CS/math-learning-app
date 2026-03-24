"""Fraction comparison generator (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import fraction_svg


@register("fraction_compare")
def gen_fraction_compare(params: dict, answer_type: str) -> dict:
    denominators = params.get("denominators", [2, 3, 4, 6, 8])

    variant = random.choice(["same_denom", "same_numer", "unit_fractions"])

    if variant == "same_denom":
        # Same denominator, different numerators
        d = random.choice(denominators)
        n1 = random.randint(1, d - 1)
        n2 = random.randint(1, d - 1)
        while n1 == n2:
            n2 = random.randint(1, d - 1)
        d1, d2 = d, d
        hint = f"Same denominator ({d}). Compare numerators: {n1} vs {n2}. Bigger numerator = bigger fraction!"
    elif variant == "same_numer":
        # Same numerator, different denominators
        n = random.randint(1, 3)
        d1 = random.choice([d for d in denominators if d > n])
        d2 = random.choice([d for d in denominators if d > n and d != d1])
        n1, n2 = n, n
        hint = f"Same numerator ({n}). Compare denominators: {d1} vs {d2}. Smaller denominator = bigger pieces = bigger fraction!"
    else:
        # Unit fractions (1/something)
        n1, n2 = 1, 1
        d1 = random.choice(denominators)
        d2 = random.choice([d for d in denominators if d != d1])
        hint = f"Both are unit fractions (1 on top). 1/{d1} vs 1/{d2}. Fewer total slices means each slice is bigger!"

    # Build SVG pizza visuals for both fractions
    svg1 = fraction_svg(n1, d1)
    svg2 = fraction_svg(n2, d2)

    # Calculate actual values to compare
    val1 = n1 / d1
    val2 = n2 / d2

    if val1 > val2:
        answer = ">"
    elif val1 < val2:
        answer = "<"
    else:
        answer = "="

    frac1 = f"{n1}/{d1}"
    frac2 = f"{n2}/{d2}"

    return {
        "question": f"Compare: {frac1}  _  {frac2}",
        "question_text": f"{frac1}   _   {frac2}",
        "image_left": svg1,
        "image_right": svg2,
        "answer": answer,
        "options": [">", "<", "="],
        "hint": hint,
        "type": answer_type,
        "subtype": "comparison",
    }
