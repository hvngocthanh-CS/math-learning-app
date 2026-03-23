"""Time reading generator (Grade 2)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import CLOCK_EMOJIS
from app.features.learn.generators.common.helpers import make_options


@register("time_reading")
def gen_time_reading(params: dict, answer_type: str) -> dict:
    hours = params.get("hours", list(range(1, 13)))
    hour = random.choice(hours)
    emoji = CLOCK_EMOJIS.get(hour, "🕐")

    return {
        "question": "What time is it?",
        "question_text": "Look at the clock. What time does it show?",
        "answer": hour,
        "options": make_options(hour, min_val=1, max_val=12),
        "hint": "Look at where the short hand points.",
        "type": answer_type,
        "subtype": "clock",
        "clock_emoji": emoji,
    }
