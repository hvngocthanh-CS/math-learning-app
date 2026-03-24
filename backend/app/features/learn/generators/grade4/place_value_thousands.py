"""Place value to 10,000 generator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("place_value_thousands")
def gen_place_value_thousands(params: dict, answer_type: str) -> dict:
    min_val = params.get("min", 1001)
    max_val = params.get("max", 9999)
    number = random.randint(min_val, max_val)

    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    variant = random.choice(["thousands", "hundreds", "tens", "ones", "expanded"])

    if variant == "thousands":
        question = f"How many thousands are in {number:,}?"
        question_text = f"{number:,}\nHow many thousands?"
        answer = thousands
        hint = f"The thousands digit is the FIRST digit from the left. In {number:,}, it is {thousands}."
        options = make_options(answer, min_val=1, max_val=9)
    elif variant == "hundreds":
        question = f"What is the hundreds digit in {number:,}?"
        question_text = f"{number:,}\nWhat is the hundreds digit?"
        answer = hundreds
        hint = f"The hundreds digit is the SECOND digit from the left. In {number:,}, it is {hundreds}."
        options = make_options(answer, min_val=0, max_val=9)
    elif variant == "tens":
        question = f"What is the tens digit in {number:,}?"
        question_text = f"{number:,}\nWhat is the tens digit?"
        answer = tens
        hint = f"The tens digit is the THIRD digit from the left. In {number:,}, it is {tens}."
        options = make_options(answer, min_val=0, max_val=9)
    elif variant == "ones":
        question = f"What is the ones digit in {number:,}?"
        question_text = f"{number:,}\nWhat is the ones digit?"
        answer = ones
        hint = f"The ones digit is the LAST (rightmost) digit. In {number:,}, it is {ones}."
        options = make_options(answer, min_val=0, max_val=9)
    else:
        # Expanded form: give digits, ask for the number
        answer = number
        question = f"What number has {thousands} thousands, {hundreds} hundreds, {tens} tens, and {ones} ones?"
        question_text = (
            f"{thousands} thousands + {hundreds} hundreds\n"
            f"+ {tens} tens + {ones} ones = ?"
        )
        hint = f"{thousands}×1000 + {hundreds}×100 + {tens}×10 + {ones} = {number:,}"
        options = make_options(answer, min_val=max(1000, answer - 500), max_val=min(9999, answer + 500))

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
