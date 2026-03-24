"""Equivalent fractions generator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import fraction_svg


@register("equivalent_fractions")
def gen_equivalent_fractions(params: dict, answer_type: str) -> dict:
    # Base fractions that are easy for grade 4
    base_fractions = params.get("base_fractions", [
        (1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 4), (1, 5), (2, 5),
    ])

    base_n, base_d = random.choice(base_fractions)
    multiplier = random.choice([2, 3, 4])

    equiv_n = base_n * multiplier
    equiv_d = base_d * multiplier

    svg_base = fraction_svg(base_n, base_d)
    svg_equiv = fraction_svg(equiv_n, equiv_d)

    variant = random.choice(["find_numerator", "find_denominator", "identify"])

    if variant == "find_numerator":
        question = f"Find the missing number: {base_n}/{base_d} = ?/{equiv_d}"
        question_text = f"{base_n}/{base_d} = ?/{equiv_d}"
        answer = equiv_n
        hint = (
            f"Multiply top and bottom by the same number. "
            f"{base_d} × {multiplier} = {equiv_d}, so {base_n} × {multiplier} = {equiv_n}."
        )
        wrong = list({equiv_n + 1, equiv_n - 1, base_n, equiv_n + 2} - {equiv_n, 0})
        options = [equiv_n] + wrong[:3]
        random.shuffle(options)
    elif variant == "find_denominator":
        question = f"Find the missing number: {base_n}/{base_d} = {equiv_n}/?"
        question_text = f"{base_n}/{base_d} = {equiv_n}/?"
        answer = equiv_d
        hint = (
            f"Multiply top and bottom by the same number. "
            f"{base_n} × {multiplier} = {equiv_n}, so {base_d} × {multiplier} = {equiv_d}."
        )
        wrong = list({equiv_d + 1, equiv_d - 1, base_d, equiv_d + 2} - {equiv_d, 0})
        options = [equiv_d] + wrong[:3]
        random.shuffle(options)
    else:
        # Show both pizzas, ask if they are equivalent
        question = f"Are {base_n}/{base_d} and {equiv_n}/{equiv_d} equivalent?"
        question_text = f"{base_n}/{base_d}  and  {equiv_n}/{equiv_d}"
        # Mix in a non-equivalent sometimes
        if random.random() < 0.4:
            # Make non-equivalent
            equiv_n_wrong = equiv_n + random.choice([-1, 1])
            if equiv_n_wrong < 1:
                equiv_n_wrong = equiv_n + 1
            if equiv_n_wrong >= equiv_d:
                equiv_n_wrong = equiv_n - 1 if equiv_n > 1 else equiv_n + 1
            question_text = f"{base_n}/{base_d}  and  {equiv_n_wrong}/{equiv_d}"
            question = f"Are {base_n}/{base_d} and {equiv_n_wrong}/{equiv_d} equivalent?"
            answer = "no"
            hint = f"{base_n}/{base_d} = {equiv_n}/{equiv_d}, but {equiv_n_wrong}/{equiv_d} is different."
            svg_equiv = fraction_svg(equiv_n_wrong, equiv_d)
        else:
            answer = "yes"
            hint = f"Both fractions equal the same amount: {base_n}/{base_d} = {equiv_n}/{equiv_d}."

        options = ["yes", "no"]

    result = {
        "question": question,
        "question_text": question_text,
        "image_left": svg_base,
        "image_right": svg_equiv,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
    if variant == "identify":
        result["subtype"] = "equivalent_pick"
    return result
