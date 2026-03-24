"""Place value generator for hundreds, tens, ones (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("place_value_hundreds")
def gen_place_value_hundreds(params: dict, answer_type: str) -> dict:
    min_val = params.get("min", 101)
    max_val = params.get("max", 999)

    number = random.randint(min_val, max_val)
    hundreds = number // 100
    tens = (number % 100) // 10
    ones = number % 10

    variant = random.choice(["hundreds", "tens", "ones", "expanded"])

    if variant == "hundreds":
        question = f"How many HUNDREDS are in {number}?"
        question_text = f"{number} → How many hundreds?"
        answer = hundreds
        hint = f"The first digit of {number} is {hundreds}. That is the hundreds place!"
        options = make_options(answer, min_val=0, max_val=9)
    elif variant == "tens":
        question = f"How many TENS are in {number}?"
        question_text = f"{number} → How many tens?"
        answer = tens
        hint = f"The middle digit of {number} is {tens}. That is the tens place!"
        options = make_options(answer, min_val=0, max_val=9)
    elif variant == "ones":
        question = f"How many ONES are in {number}?"
        question_text = f"{number} → How many ones?"
        answer = ones
        hint = f"The last digit of {number} is {ones}. That is the ones place!"
        options = make_options(answer, min_val=0, max_val=9)
    else:  # expanded
        # Ask: what number has H hundreds, T tens, O ones?
        question = f"What number has {hundreds} hundreds, {tens} tens, and {ones} ones?"
        question_text = f"{hundreds} hundreds + {tens} tens + {ones} ones = ?"
        answer = number
        hint = f"{hundreds} × 100 = {hundreds * 100}, {tens} × 10 = {tens * 10}, plus {ones}."
        options = make_options(answer, min_val=max(100, number - 50), max_val=min(999, number + 50))

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
