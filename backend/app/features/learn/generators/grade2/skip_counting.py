"""Skip counting generator (Grade 2) - count by 2s, 5s, 10s."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("skip_counting")
def gen_skip_counting(params: dict, answer_type: str) -> dict:
    # Support both single step and a list of steps to mix
    steps = params.get("steps", None)
    step = random.choice(steps) if steps else params.get("step", random.choice([2, 5, 10]))
    max_val = params.get("max", 100)

    # Build a sequence of 5-6 numbers counting by step
    start = random.choice(range(step, max_val // 2, step))
    length = random.randint(5, 6)
    seq = [start + step * i for i in range(length) if start + step * i <= max_val]

    if len(seq) < 4:
        seq = [step * i for i in range(1, length + 1) if step * i <= max_val]

    # Remove one number for the student to fill in
    missing_idx = random.randint(1, len(seq) - 2)  # avoid first/last for clarity
    answer = seq[missing_idx]
    display = [str(x) if i != missing_idx else "_" for i, x in enumerate(seq)]
    seq_str = ", ".join(display)

    return {
        "question": f"Count by {step}s! Fill in the blank.",
        "question_text": f"What is the missing number? {seq_str}",
        "answer": answer,
        "options": make_options(answer, min_val=max(0, answer - step * 2), max_val=answer + step * 2),
        "hint": f"Each number is {step} more than the one before. What is {seq[missing_idx - 1]} + {step}?",
        "type": answer_type,
    }
