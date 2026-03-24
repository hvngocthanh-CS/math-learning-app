"""Introduction to volume — counting cubes (Grade 5).

Designed for young learners: uses concrete objects, small numbers,
and clear step-by-step language.
"""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_OBJECTS = [
    ("toy box", "🧸"),
    ("lunch box", "🍱"),
    ("gift box", "🎁"),
    ("brick", "🧱"),
    ("block tower", "🏗️"),
]


@register("volume_intro")
def gen_volume_intro(params: dict, answer_type: str) -> dict:
    min_dim = params.get("min_dim", 1)
    max_dim = params.get("max_dim", 5)

    length = random.randint(min_dim, max_dim)
    width = random.randint(min_dim, max_dim)
    height = random.randint(min_dim, max_dim)
    volume = length * width * height
    obj_name, emoji = random.choice(_OBJECTS)

    variant = random.choice(["simple", "layer", "word"])

    if variant == "simple":
        question = (
            f"A {obj_name} is {length} cm long, {width} cm wide, and {height} cm tall. "
            f"What is its volume?\n"
            f"(Volume = length × width × height)"
        )
        question_text = f"Volume = {length} cm × {width} cm × {height} cm = ? cm³"
        hint = (
            f"Multiply step by step:\n"
            f"First: {length} × {width} = {length * width}.\n"
            f"Then: {length * width} × {height} = {volume}.\n"
            f"Volume = {volume} cm³."
        )
    elif variant == "layer":
        layer = length * width
        question = (
            f"Imagine stacking small cubes inside a {obj_name}.\n"
            f"Each layer has {layer} cubes. There are {height} layers.\n"
            f"How many cubes fit inside?"
        )
        question_text = f"{layer} cubes × {height} layers = ? cubes"
        hint = (
            f"Each layer has {layer} cubes.\n"
            f"There are {height} layers.\n"
            f"{layer} × {height} = {volume} cubes."
        )
    else:
        question = (
            f"A {obj_name} is {length} cm long, {width} cm wide, and {height} cm tall. "
            f"How many 1 cm × 1 cm × 1 cm cubes can fit inside it?"
        )
        question_text = f"{length} × {width} × {height} = ? cubes"
        hint = (
            f"Each small cube is 1 cm³.\n"
            f"Volume = {length} × {width} × {height} = {volume}.\n"
            f"So {volume} cubes fit inside."
        )

    return {
        "question": question,
        "question_text": question_text,
        "answer": volume,
        "options": make_options(volume, min_val=max(1, volume - 10), max_val=volume + 10),
        "hint": hint,
        "type": answer_type,
        "emoji": emoji,
    }
