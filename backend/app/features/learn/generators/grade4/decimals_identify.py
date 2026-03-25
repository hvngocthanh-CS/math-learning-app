"""Introduction to decimals (tenths) generator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


def _tenths_bar_svg(shaded: int, size_w: int = 200, size_h: int = 40) -> str:
    """SVG bar divided into 10 equal segments with `shaded` segments filled.
    Represents a value between 0.0 and 1.0 (one whole)."""
    bar_x = 10
    bar_y = 5
    bar_w = size_w - 20
    bar_h = size_h - 10
    seg_w = bar_w / 10

    parts = []
    for i in range(10):
        fill = "#60A5FA" if i < shaded else "#E5E7EB"
        x = bar_x + i * seg_w
        parts.append(
            f'<rect x="{x:.1f}" y="{bar_y}" width="{seg_w:.1f}" height="{bar_h}" '
            f'fill="{fill}" stroke="#94A3B8" stroke-width="1.5"/>'
        )

    # Label segments 1-10 below
    for i in range(10):
        cx = bar_x + i * seg_w + seg_w / 2
        parts.append(
            f'<text x="{cx:.1f}" y="{bar_y + bar_h + 14}" '
            f'text-anchor="middle" font-size="9" fill="#9CA3AF">{i + 1}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size_w}" height="{size_h + 18}">'
        + "".join(parts)
        + "</svg>"
    )


def _multi_bar_svg(whole: int, tenths: int, size_w: int = 260, bar_h: int = 24) -> str:
    """SVG showing `whole` fully shaded bars + one partial bar with `tenths` shaded.
    Represents a decimal like 2.3 = two full bars + 3/10 of a bar."""
    bar_x = 10
    bar_w = size_w - 20
    seg_w = bar_w / 10
    gap = 6
    rows = whole + (1 if tenths > 0 else 0)
    total_h = rows * (bar_h + gap) + 16

    parts = []
    for row in range(rows):
        y = 5 + row * (bar_h + gap)
        is_partial = (row == whole) and (tenths > 0)
        filled = tenths if is_partial else 10
        for i in range(10):
            fill = "#60A5FA" if i < filled else "#E5E7EB"
            x = bar_x + i * seg_w
            parts.append(
                f'<rect x="{x:.1f}" y="{y}" width="{seg_w:.1f}" height="{bar_h}" '
                f'fill="{fill}" stroke="#94A3B8" stroke-width="1"/>'
            )
        label = "1 whole" if not is_partial else f"{filled}/10"
        parts.append(
            f'<text x="{bar_x + bar_w + 5}" y="{y + bar_h / 2 + 4}" '
            f'font-size="10" fill="#6B7280">{label}</text>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size_w + 50}" height="{total_h}">'
        + "".join(parts)
        + "</svg>"
    )


def _make_decimal_options(correct: float, count: int = 4) -> list:
    """Generate plausible decimal options near the correct answer."""
    options = {correct}
    offsets = [-0.3, -0.2, -0.1, 0.1, 0.2, 0.3, -1.0, 1.0]
    random.shuffle(offsets)
    for off in offsets:
        v = round(correct + off, 1)
        if v > 0 and v != correct and v not in options:
            options.add(v)
        if len(options) >= count:
            break
    while len(options) < count:
        v = round(random.uniform(0.1, 5.9), 1)
        if v != correct:
            options.add(v)
    result = list(options)[:count]
    random.shuffle(result)
    return result


@register("decimals_identify")
def gen_decimals_identify(params: dict, answer_type: str) -> dict:
    max_whole = params.get("max_whole", 5)

    variant = random.choice([
        "read_bar",
        "read_bar_whole",
        "fraction_to_decimal",
        "decimal_to_fraction",
        "identify_tenths",
    ])

    if variant == "read_bar":
        # Simple: one bar, 0.1 to 0.9 — no whole part
        tenths = random.randint(1, 9)
        svg = _tenths_bar_svg(tenths)
        answer = round(tenths / 10, 1)

        return {
            "question": "This bar is divided into 10 equal parts. What decimal does the shaded part show?",
            "question_text": f"{tenths} out of 10 parts are shaded.\nWhat decimal is this?",
            "image": svg,
            "answer": answer,
            "options": _make_decimal_options(answer),
            "hint": f"{tenths} out of 10 = {tenths}/10 = 0.{tenths}",
            "type": answer_type,
        }

    elif variant == "read_bar_whole":
        # Whole + tenths with visual bars
        whole = random.randint(1, min(max_whole, 3))
        tenths = random.randint(1, 9)
        svg = _multi_bar_svg(whole, tenths)
        answer = float(f"{whole}.{tenths}")

        return {
            "question": f"Each full bar is 1 whole. What decimal does this picture show?",
            "question_text": f"{whole} full bar{'s' if whole > 1 else ''} and {tenths} out of 10 parts.\nWhat decimal is this?",
            "image": svg,
            "answer": answer,
            "options": _make_decimal_options(answer),
            "hint": f"{whole} whole{'s' if whole > 1 else ''} and {tenths}/10 = {whole} + 0.{tenths} = {whole}.{tenths}",
            "type": answer_type,
        }

    elif variant == "fraction_to_decimal":
        # Convert X/10 to decimal
        tenths = random.randint(1, 9)
        answer = float(f"0.{tenths}")

        return {
            "question": f"Write {tenths}/10 as a decimal.",
            "question_text": f"{tenths}/10 = ?",
            "answer": answer,
            "options": _make_decimal_options(answer),
            "hint": f"To write a fraction with 10 on the bottom as a decimal: put the top number after 0. → {tenths}/10 = 0.{tenths}",
            "type": answer_type,
        }

    elif variant == "decimal_to_fraction":
        # Convert 0.X to fraction (answer as tenths numerator)
        tenths = random.randint(1, 9)
        decimal_val = float(f"0.{tenths}")

        return {
            "question": f"Write 0.{tenths} as a fraction with 10 on the bottom. What is the top number?",
            "question_text": f"0.{tenths} = ?/10",
            "answer": tenths,
            "options": make_options(tenths, min_val=1, max_val=9),
            "hint": f"The digit after the decimal point tells you the tenths. 0.{tenths} = {tenths}/10. The top number is {tenths}.",
            "type": answer_type,
        }

    else:  # identify_tenths
        whole = random.randint(0, max_whole)
        tenths = random.randint(1, 9)
        decimal_val = float(f"{whole}.{tenths}")

        return {
            "question": f"What is the tenths digit in {decimal_val}?",
            "question_text": f"{decimal_val}\nWhat digit is in the tenths place?",
            "answer": tenths,
            "options": make_options(tenths, min_val=0, max_val=9),
            "hint": f"The tenths place is the first digit AFTER the decimal point. In {decimal_val}, it is {tenths}.",
            "type": answer_type,
        }
