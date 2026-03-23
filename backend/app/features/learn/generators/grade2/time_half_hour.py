"""Time reading to the half hour generator (Grade 2)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import CLOCK_EMOJIS, CLOCK_HALF_EMOJIS


def _make_time_options(correct: str, count: int = 4) -> list:
    """Generate plausible time options for multiple choice."""
    options = {correct}
    hour = int(correct.split(":")[0])
    minute = correct.split(":")[1]

    # Add nearby hour distractors
    distractors = []
    for offset in [-1, 1, -2, 2]:
        h = (hour + offset - 1) % 12 + 1
        distractors.append(f"{h}:{minute}")
    # Also add swapped minute (if :00 add :30 variant, vice versa)
    swap_min = "30" if minute == "00" else "00"
    distractors.append(f"{hour}:{swap_min}")

    random.shuffle(distractors)
    for d in distractors:
        if len(options) >= count:
            break
        if d != correct:
            options.add(d)

    result = list(options)
    random.shuffle(result)
    return result


@register("time_half_hour")
def gen_time_half_hour(params: dict, answer_type: str) -> dict:
    hours = params.get("hours", list(range(1, 13)))
    hour = random.choice(hours)
    is_half = random.choice([True, False])

    if is_half:
        emoji = CLOCK_HALF_EMOJIS.get(hour, "🕜")
        answer = f"{hour}:30"
        question_text = "Look at the clock. What time does it show?"
        hint = "When the long hand points down to 6, it means 30 minutes (half past)."
    else:
        emoji = CLOCK_EMOJIS.get(hour, "🕐")
        answer = f"{hour}:00"
        question_text = "Look at the clock. What time does it show?"
        hint = "When the long hand points up to 12, it means exactly on the hour (:00)."

    return {
        "question": "What time is it?",
        "question_text": question_text,
        "answer": answer,
        "options": _make_time_options(answer),
        "hint": hint,
        "type": answer_type,
        "subtype": "clock",
        "clock_emoji": emoji,
    }
