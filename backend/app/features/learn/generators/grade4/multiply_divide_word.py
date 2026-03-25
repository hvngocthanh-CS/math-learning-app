"""Multiplication & division word problem generator (Grade 4)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

_MULTIPLY_TEMPLATES = [
    ("{name} buys {a} packs of stickers. Each pack has {b} stickers. How many stickers in total?", "🌟"),
    ("There are {a} rows of chairs. Each row has {b} chairs. How many chairs altogether?", "🪑"),
    ("{name} reads {b} pages every day for {a} days. How many pages in total?", "📖"),
    ("A bakery makes {a} trays of cupcakes. Each tray has {b} cupcakes. How many cupcakes?", "🧁"),
    ("{name} earns ${b} each week. After {a} weeks, how much money has {name} earned?", "💰"),
]

_DIVIDE_TEMPLATES = [
    ("{name} has {total} candies and shares them equally among {b} friends. How many does each friend get?", "🍬"),
    ("There are {total} students split into {b} equal teams. How many on each team?", "👫"),
    ("{name} has {total} stickers and puts {b} on each page. How many pages are needed?", "📋"),
    ("A full box holds {b} apples. {name} has {total} apples. How many full boxes?", "🍎"),
    ("{total} marbles are shared equally into {b} bags. How many in each bag?", "🔮"),
]


@register("multiply_divide_word")
def gen_multiply_divide_word(params: dict, answer_type: str) -> dict:
    min_factor = params.get("min_factor", 3)
    max_factor = params.get("max_factor", 12)

    name = random.choice(_NAMES)
    op = random.choice(["multiply", "divide"])

    if op == "multiply":
        a = random.randint(min_factor, max_factor)
        b = random.randint(min_factor, max_factor)
        answer = a * b
        template, emoji = random.choice(_MULTIPLY_TEMPLATES)
        question_text = template.format(name=name, a=a, b=b)
        hint = f"This is a multiplication problem: {a} × {b} = {answer}."
        options = make_options(answer, min_val=max(10, answer - 20), max_val=answer + 20)
    else:
        b = random.randint(min_factor, max_factor)
        quotient = random.randint(min_factor, max_factor)
        total = b * quotient
        answer = quotient
        template, emoji = random.choice(_DIVIDE_TEMPLATES)
        question_text = template.format(name=name, total=total, b=b)
        hint = f"This is a division problem: {total} ÷ {b} = {quotient}."
        emoji = emoji
        options = make_options(answer, min_val=max(2, answer - 5), max_val=answer + 5)

    return {
        "question": question_text,
        "question_text": question_text,
        "emoji": emoji,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
