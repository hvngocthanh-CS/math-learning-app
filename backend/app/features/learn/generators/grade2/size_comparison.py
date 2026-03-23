"""Size comparison generator (Grade 2)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import (
    SIZE_BIGGER, SIZE_TALLER, SIZE_LONGER,
)

_OPPOSITES = {"bigger": "smaller", "taller": "shorter", "longer": "shorter"}

_GROUPS = [
    ("bigger", SIZE_BIGGER),
    ("taller", SIZE_TALLER),
    ("longer", SIZE_LONGER),
]


@register("size_comparison")
def gen_size_comparison(params: dict, answer_type: str) -> dict:
    # Pick a random category, then a fitting pair
    word, pairs = random.choice(_GROUPS)
    item_a, item_b = random.choice(pairs)
    # item_a is always the bigger/taller/longer one

    # Randomly ask positive or negative direction
    ask_positive = random.choice([True, False])
    if ask_positive:
        answer = item_a
        question_word = word
        hint = f"Think about real life! {item_a.split()[0].capitalize()} is much {word} than {item_b.split()[0]}."
    else:
        answer = item_b
        question_word = _OPPOSITES[word]
        hint = f"Think about real life! {item_b.split()[0].capitalize()} is much {question_word} than {item_a.split()[0]}."

    # Randomly swap display order
    options = [item_a, item_b]
    random.shuffle(options)

    return {
        "question": f"Which one is {question_word}?",
        "question_text": f"Which one is {question_word}?",
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
        "subtype": "size_pick",
    }
