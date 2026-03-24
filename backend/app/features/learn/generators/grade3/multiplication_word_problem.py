"""Multiplication word problem generator (Grade 3)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Jack", "Sophie", "Ethan", "Mia", "Lucas"]

_TEMPLATES = [
    ("There are {a} bags. Each bag has {b} {item}. How many {item} are there in total?",
     [("apples", "🍎"), ("oranges", "🍊"), ("cookies", "🍪"), ("candies", "🍬"), ("marbles", "🔮")]),
    ("{name} has {a} boxes. Each box has {b} {item}. How many {item} does {name} have in total?",
     [("toys", "🧸"), ("books", "📚"), ("crayons", "🖍️"), ("stickers", "⭐"), ("pencils", "✏️")]),
    ("There are {a} rows of cars. Each row has {b} cars. How many cars are there in total?",
     [("cars", "🚗")]),
    ("There are {a} tables. Each table has {b} {item}. How many {item} are there in total?",
     [("plates", "🍽️"), ("cups", "☕"), ("flowers", "🌸"), ("chairs", "🪑")]),
    ("{name} has {a} friends. {name} gives {b} {item} to each friend. How many {item} does {name} give in total?",
     [("stickers", "⭐"), ("candies", "🍬"), ("cards", "🃏"), ("cookies", "🍪")]),
    ("There are {a} {item}. Each one has {b} legs. How many legs are there in total?",
     [("dogs", "🐶"), ("cats", "🐱"), ("horses", "🐴"), ("spiders", "🕷️")]),
]


@register("multiplication_word_problem")
def gen_multiplication_word_problem(params: dict, answer_type: str) -> dict:
    min_factor = params.get("min_factor", 2)
    max_factor = params.get("max_factor", 10)

    a = random.randint(min_factor, max_factor)
    b = random.randint(min_factor, max_factor)
    answer = a * b

    template, items = random.choice(_TEMPLATES)
    item_name, item_emoji = random.choice(items)
    name = random.choice(_NAMES)

    story = template.format(name=name, a=a, b=b, item=item_name)

    return {
        "question": story,
        "question_text": f"{item_emoji} {story}",
        "answer": answer,
        "options": make_options(answer, min_val=max(0, answer - 10), max_val=answer + 15),
        "hint": f"This is {a} groups of {b}. Multiply: {a} × {b} = ?",
        "type": answer_type,
    }
