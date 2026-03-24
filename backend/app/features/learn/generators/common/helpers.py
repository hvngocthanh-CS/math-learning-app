"""
Shared helper functions used by problem generators across all grades.
"""

import math
import random
from typing import List

from app.features.learn.generators.common.constants import NUMBER_WORDS


def fraction_svg(numerator: int, denominator: int, size: int = 140) -> str:
    """Return an inline SVG of a pizza-style circle divided into *denominator*
    equal slices with *numerator* slices filled.

    The image uses warm pizza colours:
      - filled slices  → golden-yellow (#F4A83D) with a pepperoni dot
      - empty slices   → light beige  (#FFF3DC)
      - crust border   → brown        (#C07830)
      - divider lines  → brown
    """
    cx = cy = size / 2
    r = size / 2 - 4  # leave room for stroke

    if denominator == 1:
        fill = "#F4A83D" if numerator == 1 else "#FFF3DC"
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}">'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="#C07830" stroke-width="3"/></svg>'
        )

    paths: list[str] = []
    angle_step = 2 * math.pi / denominator
    # Start from 12-o'clock (-π/2)
    start_offset = -math.pi / 2

    for i in range(denominator):
        a1 = start_offset + i * angle_step
        a2 = start_offset + (i + 1) * angle_step
        x1 = cx + r * math.cos(a1)
        y1 = cy + r * math.sin(a1)
        x2 = cx + r * math.cos(a2)
        y2 = cy + r * math.sin(a2)
        large_arc = 1 if angle_step > math.pi else 0
        fill = "#F4A83D" if i < numerator else "#FFF3DC"

        paths.append(
            f'<path d="M {cx},{cy} L {x1:.2f},{y1:.2f} '
            f'A {r},{r} 0 {large_arc} 1 {x2:.2f},{y2:.2f} Z" '
            f'fill="{fill}" stroke="#C07830" stroke-width="2"/>'
        )

        # small pepperoni dot on filled slices
        if i < numerator:
            mid_a = (a1 + a2) / 2
            dot_r = r * 0.55
            dx = cx + dot_r * math.cos(mid_a)
            dy = cy + dot_r * math.sin(mid_a)
            dot_size = max(3, r * 0.08)
            paths.append(
                f'<circle cx="{dx:.1f}" cy="{dy:.1f}" r="{dot_size:.1f}" fill="#C0392B"/>'
            )

    # outer crust ring
    paths.append(
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
        f'stroke="#C07830" stroke-width="3"/>'
    )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}">'
        + "".join(paths)
        + "</svg>"
    )


def make_options(answer: int, count: int = 4, min_val: int = 0, max_val: int = 20) -> List[int]:
    """Generate multiple choice options that include the correct answer."""
    # Ensure range is wide enough for `count` distinct values
    while (max_val - min_val + 1) < count:
        if min_val > 0:
            min_val -= 1
        max_val += 1

    options = {answer}
    attempts = 0
    while len(options) < count and attempts < 50:
        offset = random.choice([-2, -1, 1, 2, -3, 3])
        val = answer + offset
        if min_val <= val <= max_val:
            options.add(val)
        attempts += 1
    # Safe fallback: pick from remaining values in range
    if len(options) < count:
        remaining = [v for v in range(min_val, max_val + 1) if v not in options]
        random.shuffle(remaining)
        for v in remaining:
            if len(options) >= count:
                break
            options.add(v)
    result = list(options)
    random.shuffle(result)
    return result


def make_word_options(correct_word: str, min_n: int, max_n: int, count: int = 4) -> list:
    """Generate word options for multiple choice, including the correct answer."""
    word_options = {correct_word}
    attempts = 0
    while len(word_options) < count and attempts < 100:
        rand_n = random.randint(min_n, max_n)
        word_options.add(NUMBER_WORDS.get(rand_n, str(rand_n)))
        attempts += 1
    result = list(word_options)
    random.shuffle(result)
    return result
