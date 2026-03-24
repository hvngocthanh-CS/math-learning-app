"""Volume of rectangular prisms generator (Grade 5).

Uses real-life objects and friendly numbers for young learners.
"""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

_WORD_TEMPLATES = [
    {
        "template": "{name}'s fish tank is {l} cm long, {w} cm wide, and {h} cm tall. What is the volume of the fish tank?",
        "emoji": "🐟",
    },
    {
        "template": "A shoebox is {l} cm long, {w} cm wide, and {h} cm tall. What is the volume of the shoebox?",
        "emoji": "👟",
    },
    {
        "template": "{name} has a pencil case that is {l} cm long, {w} cm wide, and {h} cm tall. What is the volume?",
        "emoji": "✏️",
    },
    {
        "template": "A toy chest is {l} cm long, {w} cm wide, and {h} cm tall. What is the volume of the chest?",
        "emoji": "🧸",
    },
    {
        "template": "A book is {l} cm long, {w} cm wide, and {h} cm thick. What is the volume of the book?",
        "emoji": "📚",
    },
]


@register("volume_prism")
def gen_volume_prism(params: dict, answer_type: str) -> dict:
    min_dim = params.get("min_dim", 2)
    max_dim = params.get("max_dim", 10)

    length = random.randint(min_dim, max_dim)
    width = random.randint(min_dim, max_dim)
    height = random.randint(min_dim, max_dim)
    volume = length * width * height

    variant = random.choice(["calculate", "calculate", "word", "find_side"])

    if variant == "word":
        name = random.choice(_NAMES)
        tmpl = random.choice(_WORD_TEMPLATES)
        question = tmpl["template"].format(name=name, l=length, w=width, h=height)
        question_text = f"Volume = {length} cm × {width} cm × {height} cm = ? cm³"
        hint = (
            f"Volume = length × width × height\n"
            f"= {length} × {width} × {height}\n"
            f"= {length * width} × {height}\n"
            f"= {volume} cm³."
        )
        options = make_options(volume, min_val=max(1, volume - 30), max_val=volume + 30)
        return {
            "question": question,
            "question_text": question_text,
            "answer": volume,
            "options": options,
            "hint": hint,
            "type": answer_type,
            "emoji": tmpl["emoji"],
        }

    if variant == "calculate":
        question = (
            f"A box is {length} cm long, {width} cm wide, and {height} cm tall.\n"
            f"Volume = length × width × height. What is the volume?"
        )
        question_text = f"Volume = {length} cm × {width} cm × {height} cm = ? cm³"
        answer = volume
        hint = (
            f"Step 1: {length} × {width} = {length * width}\n"
            f"Step 2: {length * width} × {height} = {volume}\n"
            f"Volume = {volume} cm³."
        )
        options = make_options(answer, min_val=max(1, answer - 30), max_val=answer + 30)
    else:
        # Find a missing side — use simple wording
        dims = [
            ("long", "length", length),
            ("wide", "width", width),
            ("tall", "height", height),
        ]
        idx = random.randint(0, 2)
        missing_adj, missing_name, missing_val = dims[idx]
        known = [d for i, d in enumerate(dims) if i != idx]
        product_known = known[0][2] * known[1][2]
        answer = missing_val

        question = (
            f"A box has a volume of {volume} cm³.\n"
            f"It is {known[0][2]} cm {known[0][0]} and {known[1][2]} cm {known[1][0]}.\n"
            f"How many cm {missing_adj} is it?"
        )
        question_text = f"{known[0][2]} cm × {known[1][2]} cm × ? cm = {volume} cm³"
        hint = (
            f"Volume = {known[0][2]} × {known[1][2]} × ?\n"
            f"{product_known} × ? = {volume}\n"
            f"? = {volume} ÷ {product_known} = {answer} cm."
        )
        options = make_options(answer, min_val=max(1, answer - 4), max_val=answer + 6)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
