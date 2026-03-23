"""Addition and subtraction generators (Grade 1)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import EMOJI_GROUPS
from app.features.learn.generators.common.helpers import make_options


@register("addition")
def gen_addition(params: dict, answer_type: str) -> dict:
    min_a = params.get("min_a", 0)
    max_a = params.get("max_a", 5)
    min_b = params.get("min_b", 0)
    max_b = params.get("max_b", 5)
    max_sum = params.get("max_sum", 10)
    tens_only = params.get("tens_only", False)

    for _ in range(50):
        a = random.randint(min_a, max_a)
        b = random.randint(min_b, max_b)
        if tens_only:
            a = (a // 10) * 10 or 10
            b = (b // 10) * 10 or 10
        if a + b <= max_sum:
            break
    answer = a + b

    use_emoji = random.random() < 0.4
    if use_emoji and answer <= 10:
        name, emoji = random.choice(EMOJI_GROUPS)
        visual_a = emoji * a if a > 0 else "nothing"
        visual_b = emoji * b if b > 0 else "nothing"
        question = f"{visual_a} + {visual_b} = ?"
        question_text = f"What is {a} + {b}?"
        hint = f"Count all the {name} together: {a} and {b} more."
    else:
        question = f"What is {a} + {b}?"
        question_text = f"Solve: {a} + {b} = ?"
        if a >= 8 or b >= 8:
            hint = f"Try 'make 10': {a} + {10-a} = 10, then add {b-(10-a)} more." if a < 10 and b > 0 else f"Start at {a} and count {b} more."
        else:
            hint = f"Start at {max(a,b)} and count {min(a,b)} more."

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": make_options(answer, min_val=0, max_val=max_sum + 2),
        "hint": hint,
        "type": answer_type,
    }


@register("subtraction")
def gen_subtraction(params: dict, answer_type: str) -> dict:
    min_start = params.get("min_start", 2)
    max_start = params.get("max_start", 10)

    a = random.randint(min_start, max_start)
    b = random.randint(0, a)
    answer = a - b

    use_emoji = random.random() < 0.4
    if use_emoji and a <= 10:
        name, emoji = random.choice(EMOJI_GROUPS)
        visual = emoji * a
        question = f"{visual} take away {emoji * b if b > 0 else 'none'} = ?"
        question_text = f"What is {a} - {b}?"
        hint = f"Start with {a} {name}, take away {b}."
    else:
        question = f"What is {a} - {b}?"
        question_text = f"Solve: {a} - {b} = ?"
        hint = f"Start at {a} and count back {b}." if b > 0 else f"Taking away zero means nothing changes!"

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": make_options(answer, min_val=0, max_val=max_start),
        "hint": hint,
        "type": answer_type,
    }
