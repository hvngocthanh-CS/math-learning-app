"""Fraction identification generator (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import fraction_svg, make_options


def _make_fraction_options(numerator: int, denominator: int, count: int = 4) -> list:
    """Generate fraction string options including the correct answer."""
    correct = f"{numerator}/{denominator}"
    options = {correct}

    # Strategy: mix wrong numerators and wrong denominators
    possible_denoms = [d for d in [2, 3, 4, 6, 8] if d >= 2]
    attempts = 0
    while len(options) < count and attempts < 50:
        strategy = random.choice(["wrong_numer", "wrong_denom", "random"])
        if strategy == "wrong_numer":
            n = random.randint(1, denominator - 1) if denominator > 2 else random.randint(1, 3)
            frac = f"{n}/{denominator}"
        elif strategy == "wrong_denom":
            d = random.choice(possible_denoms)
            n = min(numerator, d - 1) if numerator < d else random.randint(1, d - 1)
            frac = f"{n}/{d}"
        else:
            d = random.choice(possible_denoms)
            n = random.randint(1, d - 1)
            frac = f"{n}/{d}"
        if frac != correct:
            options.add(frac)
        attempts += 1

    result = list(options)
    random.shuffle(result)
    return result


@register("fraction_identify")
def gen_fraction_identify(params: dict, answer_type: str) -> dict:
    denominators = params.get("denominators", [2, 3, 4])
    denominator = random.choice(denominators)
    numerator = random.randint(1, denominator - 1)

    # Build SVG pizza visual
    svg = fraction_svg(numerator, denominator)

    variant = random.choice(["read_fraction", "find_numerator", "find_denominator"])

    if variant == "read_fraction":
        question = "What fraction is shaded?"
        question_text = (
            f"{numerator} out of {denominator} slices are filled. "
            f"What fraction is this?"
        )
        answer = f"{numerator}/{denominator}"
        hint = (
            f"Count the golden slices ({numerator}) and total slices ({denominator}). "
            f"Write it as numerator/denominator."
        )
        options = _make_fraction_options(numerator, denominator)
        subtype = "fraction_input"
    elif variant == "find_numerator":
        question = f"In the fraction {numerator}/{denominator}, what is the numerator (top number)?"
        question_text = f"Fraction: {numerator}/{denominator}\nWhat is the numerator?"
        answer = numerator
        hint = "The numerator is the TOP number. It tells how many slices are filled."
        options = make_options(answer, min_val=1, max_val=max(denominator + 2, 6))
        subtype = None
    else:
        question = f"In the fraction {numerator}/{denominator}, what is the denominator (bottom number)?"
        question_text = f"Fraction: {numerator}/{denominator}\nWhat is the denominator?"
        answer = denominator
        hint = "The denominator is the BOTTOM number. It tells how many equal slices the pizza is divided into."
        options = make_options(answer, min_val=2, max_val=max(denominator + 3, 8))
        subtype = None

    result = {
        "question": question,
        "question_text": question_text,
        "image": svg,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
    if subtype:
        result["subtype"] = subtype
    return result
