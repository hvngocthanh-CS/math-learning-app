"""Area of circles generator (Grade 5).

Uses integer-friendly values: radius is given, answer = radius × radius × 3
(simplified pi ≈ 3 for Grade 5 level, or exact with pi for multiple choice).
"""

import random
import math

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

_WORD_TEMPLATES = [
    {
        "template": "{name} is making a circular badge with radius {r} cm. What is the area of the badge? (Use π ≈ 3.14)",
        "emoji": "🎖️",
    },
    {
        "template": "A circular pond has a radius of {r} m. What is the area of the pond? (Use π ≈ 3.14)",
        "emoji": "🌊",
    },
    {
        "template": "{name} bakes a circular pizza with radius {r} cm. What is the area of the pizza? (Use π ≈ 3.14)",
        "emoji": "🍕",
    },
]


def _round2(x):
    """Round to 2 decimal places and return as int if whole, else float."""
    val = round(x, 2)
    if val == int(val):
        return int(val)
    return val


def _make_circle_options(answer):
    """Generate plausible options for circle area answers."""
    options = {answer}
    # Common mistakes: forgetting to square, forgetting pi, doubling instead of squaring
    candidates = [
        _round2(answer * 2),
        _round2(answer / 2),
        _round2(answer + random.choice([-3, -2, 2, 3])),
        _round2(answer * 1.5),
        _round2(answer - random.randint(1, 5)),
        _round2(answer + random.randint(1, 5)),
    ]
    for c in candidates:
        if c > 0 and c != answer:
            options.add(c)
        if len(options) >= 4:
            break
    # fallback
    while len(options) < 4:
        options.add(_round2(answer + random.randint(-10, 10)))
    result = list(options)
    random.shuffle(result)
    return result


@register("area_circle")
def gen_area_circle(params: dict, answer_type: str) -> dict:
    min_r = params.get("min_radius", 1)
    max_r = params.get("max_radius", 10)

    radius = random.randint(min_r, max_r)
    area = _round2(3.14 * radius * radius)

    variant = random.choice(["find_area", "find_area", "word_problem"])

    if variant == "word_problem":
        name = random.choice(_NAMES)
        tmpl = random.choice(_WORD_TEMPLATES)
        question = tmpl["template"].format(name=name, r=radius)
        hint = f"Area = π × r × r = 3.14 × {radius} × {radius} = 3.14 × {radius * radius} = {area}."
        return {
            "question": question,
            "question_text": question,
            "answer": area,
            "options": _make_circle_options(area),
            "hint": hint,
            "type": answer_type,
            "emoji": tmpl["emoji"],
        }

    question = f"A circle has radius {radius} cm. What is its area? (Use π ≈ 3.14)"
    question_text = f"Area = 3.14 × {radius} cm × {radius} cm = ? cm²"
    hint = f"Area = π × r × r = 3.14 × {radius} × {radius} = 3.14 × {radius * radius} = {area} cm²."

    return {
        "question": question,
        "question_text": question_text,
        "answer": area,
        "options": _make_circle_options(area),
        "hint": hint,
        "type": answer_type,
    }
