"""Basic division generator (Grade 4) — exact division, no remainders."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options


@register("division_basic")
def gen_division_basic(params: dict, answer_type: str) -> dict:
    max_divisor = params.get("max_divisor", 9)
    max_quotient = params.get("max_quotient", 12)

    divisor = random.randint(2, max_divisor)
    quotient = random.randint(2, max_quotient)
    dividend = divisor * quotient

    variant = random.choice(["find_quotient", "find_dividend", "find_divisor"])

    if variant == "find_quotient":
        question = f"What is {dividend} ÷ {divisor}?"
        question_text = f"{dividend} ÷ {divisor} = ?"
        answer = quotient
        hint = f"Think: {divisor} × ? = {dividend}. Since {divisor} × {quotient} = {dividend}, the answer is {quotient}."
        options = make_options(answer, min_val=1, max_val=max(quotient + 5, 15))
    elif variant == "find_dividend":
        question = f"What number divided by {divisor} equals {quotient}?"
        question_text = f"? ÷ {divisor} = {quotient}"
        answer = dividend
        hint = f"If ? ÷ {divisor} = {quotient}, then ? = {divisor} × {quotient} = {dividend}."
        options = make_options(answer, min_val=max(4, answer - 15), max_val=answer + 15)
    else:
        question = f"{dividend} divided by what number equals {quotient}?"
        question_text = f"{dividend} ÷ ? = {quotient}"
        answer = divisor
        hint = f"If {dividend} ÷ ? = {quotient}, then ? = {dividend} ÷ {quotient} = {divisor}."
        options = make_options(answer, min_val=2, max_val=max(divisor + 5, 10))

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
