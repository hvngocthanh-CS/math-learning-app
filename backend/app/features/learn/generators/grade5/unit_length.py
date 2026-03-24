"""Units of length conversion generator (Grade 5)."""

import random

from app.features.learn.generators import register

# (from_unit, to_unit, factor)
_CONVERSIONS = [
    ("m", "cm", 100),
    ("cm", "m", 100),
    ("km", "m", 1000),
    ("m", "km", 1000),
    ("cm", "mm", 10),
    ("mm", "cm", 10),
]


def _make_unit_options(answer, factor):
    """Generate options that differ by powers of 10 — tricky zero counts."""
    options = {answer}

    # Common mistakes: wrong factor (×10 instead of ×100, etc.)
    candidates = []
    if isinstance(answer, int) and answer > 0:
        # Multiplied by wrong factor
        candidates.append(answer * 10)
        candidates.append(answer * 100)
        if answer % 10 == 0:
            candidates.append(answer // 10)
        if answer % 100 == 0:
            candidates.append(answer // 100)
        # Used wrong operation (multiplied instead of divided or vice versa)
        candidates.append(answer * factor)
        if answer * factor > 1:
            candidates.append(answer * factor)
        # Off by one zero
        if answer >= 10:
            # Drop a zero: 3000 -> 300
            candidates.append(int(str(answer)[:-1]) if len(str(answer)) > 1 else answer + 1)
            # Add a zero: 300 -> 3000
            candidates.append(answer * 10)

    # Filter: positive, different from answer, no duplicates
    for c in candidates:
        if c > 0 and c != answer and c not in options:
            options.add(c)
        if len(options) >= 4:
            break

    # Fallback if not enough options
    fallbacks = [answer * 2, answer * 5, answer + factor, max(1, answer - factor)]
    for c in fallbacks:
        if c > 0 and c != answer and c not in options:
            options.add(c)
        if len(options) >= 4:
            break

    result = list(options)[:4]
    random.shuffle(result)
    return result


@register("unit_length")
def gen_unit_length(params: dict, answer_type: str) -> dict:
    from_unit, to_unit, factor = random.choice(_CONVERSIONS)

    smaller_to_bigger = {
        ("cm", "m"): True,
        ("m", "km"): True,
        ("mm", "cm"): True,
    }
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
