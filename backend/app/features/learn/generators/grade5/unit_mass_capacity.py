"""Units of mass and capacity conversion generator (Grade 5)."""

import random

from app.features.learn.generators import register

# (from_unit, to_unit, factor)
_CONVERSIONS = [
    ("kg", "g", 1000),
    ("g", "kg", 1000),
    ("L", "mL", 1000),
    ("mL", "L", 1000),
]


def _make_unit_options(answer, factor):
    """Generate options that differ by powers of 10 — tricky zero counts."""
    options = {answer}

    candidates = []
    if isinstance(answer, int) and answer > 0:
        candidates.append(answer * 10)
        candidates.append(answer * 100)
        if answer % 10 == 0:
            candidates.append(answer // 10)
        if answer % 100 == 0:
            candidates.append(answer // 100)
        candidates.append(answer * factor)
        if answer >= 10:
            candidates.append(int(str(answer)[:-1]) if len(str(answer)) > 1 else answer + 1)
            candidates.append(answer * 10)

    for c in candidates:
        if c > 0 and c != answer and c not in options:
            options.add(c)
        if len(options) >= 4:
            break

    fallbacks = [answer * 2, answer * 5, answer + factor, max(1, answer - factor)]
    for c in fallbacks:
        if c > 0 and c != answer and c not in options:
            options.add(c)
        if len(options) >= 4:
            break

    result = list(options)[:4]
    random.shuffle(result)
    return result


@register("unit_mass_capacity")
def gen_unit_mass_capacity(params: dict, answer_type: str) -> dict:
    from_unit, to_unit, factor = random.choice(_CONVERSIONS)

    smaller_to_bigger = {("g", "kg"), ("mL", "L")}
    is_dividing = (from_unit, to_unit) in smaller_to_bigger

    if is_dividing:
        answer = random.randint(1, 15)
        value = answer * factor
        hint = f"To convert {from_unit} to {to_unit}, divide by {factor}: {value} ÷ {factor} = {answer} {to_unit}."
    else:
        value = random.randint(1, 15)
        answer = value * factor
        hint = f"To convert {from_unit} to {to_unit}, multiply by {factor}: {value} × {factor} = {answer} {to_unit}."

    question = f"Convert {value} {from_unit} to {to_unit}."
    question_text = f"{value} {from_unit} = ? {to_unit}"

    options = _make_unit_options(answer, factor)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
