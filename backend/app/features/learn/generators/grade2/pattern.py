"""Pattern recognition generator (Grade 2)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import PATTERN_SETS


@register("pattern")
def gen_pattern(params: dict, answer_type: str) -> dict:
    a_emoji, b_emoji = random.choice(PATTERN_SETS)
    length = random.randint(4, 6)
    pattern = [a_emoji if i % 2 == 0 else b_emoji for i in range(length)]
    answer_emoji = a_emoji if length % 2 == 0 else b_emoji
    pattern_str = " ".join(pattern)

    return {
        "question": "What comes next in the pattern?",
        "question_text": pattern_str + " ❓",
        "answer": answer_emoji,
        "options": [a_emoji, b_emoji],
        "hint": f"{a_emoji} and {b_emoji} take turns. After {'A' if pattern[-1] == a_emoji else 'B'} comes {'B' if pattern[-1] == a_emoji else 'A'}.",
        "type": answer_type,
        "subtype": "pattern_pick",
    }
