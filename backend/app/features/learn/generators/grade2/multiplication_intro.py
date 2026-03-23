"""Introduction to multiplication as repeated addition (Grade 2)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import EMOJI_GROUPS
from app.features.learn.generators.common.helpers import make_options


@register("multiplication_intro")
def gen_multiplication_intro(params: dict, answer_type: str) -> dict:
    max_groups = params.get("max_groups", 5)
    max_per_group = params.get("max_per_group", 5)

    groups = random.randint(2, max_groups)
    per_group = random.randint(1, max_per_group)
    answer = groups * per_group
    name, emoji = random.choice(EMOJI_GROUPS)

    # Show groups visually: (🍎🍎) (🍎🍎) (🍎🍎)
    group_visual = f"({emoji * per_group})"
    visual = " ".join([group_visual] * groups)

    q_type = random.choice(["total", "repeated_add"])

    if q_type == "total":
        question = f"There are {groups} groups with {per_group} {name} each. How many in total?"
        question_text = f"{visual}\n{groups} groups of {per_group} = ?"
        hint = f"Add {per_group} + {per_group} for {groups} times. Or count all the {name}!"
    else:
        add_str = " + ".join([str(per_group)] * groups)
        question = f"What is {add_str}?"
        question_text = f"{visual}\n{add_str} = ?"
        hint = f"You are adding {per_group} a total of {groups} times."

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": make_options(answer, min_val=max(0, answer - 5), max_val=answer + 5),
        "hint": hint,
        "type": answer_type,
    }
