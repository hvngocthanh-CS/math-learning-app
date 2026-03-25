"""Division with remainders generator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("division_remainder")
def gen_division_remainder(params: dict, answer_type: str) -> dict:
    max_divisor = params.get("max_divisor", 9)
    max_dividend = params.get("max_dividend", 80)

    divisor = random.randint(2, max_divisor)
    # Ensure there IS a remainder
    quotient = random.randint(2, max_dividend // divisor)
    remainder = random.randint(1, divisor - 1)
    dividend = divisor * quotient + remainder

    if dividend > max_dividend:
        quotient -= 1
        dividend = divisor * quotient + remainder

    variant = random.choice(["find_quotient", "find_remainder"])

    if variant == "find_quotient":
        question = f"What is {dividend} ÷ {divisor}? (Just the whole number part)"
        question_text = f"{dividend} ÷ {divisor} = ?\nWhat is the quotient (whole part)?"
        answer = quotient
        hint = (
            f"{divisor} × {quotient} = {divisor * quotient}, "
            f"and {dividend} - {divisor * quotient} = {remainder}. "
            f"So the quotient is {quotient} with remainder {remainder}."
        )
        options = make_options(answer, min_val=1, max_val=max(quotient + 5, 12))
    else:
        question = f"What is the remainder when {dividend} ÷ {divisor}?"
        question_text = f"{dividend} ÷ {divisor}\nWhat is the remainder?"
        answer = remainder
        hint = (
            f"{divisor} × {quotient} = {divisor * quotient}. "
            f"{dividend} - {divisor * quotient} = {remainder}. "
            f"The remainder is {remainder}."
        )
        options = make_options(answer, min_val=0, max_val=max(divisor, 6))

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
