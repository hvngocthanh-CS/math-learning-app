"""Word problem generator (Grade 2) - simple addition and subtraction stories."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Jack", "Sophie", "Ethan", "Mia", "Lucas"]

# Each template is (template_string, list_of_compatible_items)
# This ensures items always make sense in context.

_GENERAL_ITEMS = [
    ("stickers", "⭐"), ("marbles", "🔮"), ("crayons", "🖍️"), ("cards", "🃏"),
    ("coins", "🪙"), ("toys", "🧸"), ("blocks", "🧱"), ("buttons", "🔘"),
]

_FOOD_ITEMS = [
    ("apples", "🍎"), ("cookies", "🍪"), ("candies", "🍬"),
    ("oranges", "🍊"), ("strawberries", "🍓"), ("cupcakes", "🧁"),
]

_TREE_ITEMS = [
    ("apples", "🍎"), ("oranges", "🍊"), ("leaves", "🍃"), ("birds", "🐦"),
]

_EDIBLE_ITEMS = [
    ("apples", "🍎"), ("cookies", "🍪"), ("candies", "🍬"),
    ("oranges", "🍊"), ("strawberries", "🍓"), ("cupcakes", "🧁"),
]

_CONTAINER_ITEMS = [
    ("books", "📚"), ("pencils", "✏️"), ("toys", "🧸"),
    ("crayons", "🖍️"), ("marbles", "🔮"), ("balls", "⚽"),
]

_ADD_TEMPLATES = [
    ("{name} has {a} {item}. {name2} gives {name} {b} more. How many {item} does {name} have now?",
     _GENERAL_ITEMS + _FOOD_ITEMS),
    ("There are {a} {item} on a table. Someone puts {b} more. How many {item} are there now?",
     _GENERAL_ITEMS + _FOOD_ITEMS),
    ("{name} finds {a} {item} in the morning and {b} {item} in the afternoon. How many {item} in total?",
     _GENERAL_ITEMS),
    ("A box has {a} {item}. Another box has {b} {item}. How many {item} altogether?",
     _CONTAINER_ITEMS),
]

_SUB_TEMPLATES = [
    ("{name} has {a} {item}. {name} gives {b} to {name2}. How many {item} does {name} have left?",
     _GENERAL_ITEMS + _FOOD_ITEMS),
    ("There are {a} {item} in a basket. {name} takes {b}. How many {item} are left?",
     _GENERAL_ITEMS + _FOOD_ITEMS),
    ("{name} has {a} {item}. {name} eats {b}. How many {item} are left?",
     _EDIBLE_ITEMS),
    ("A tree has {a} {item}. {b} fall down. How many {item} are still on the tree?",
     _TREE_ITEMS),
]


@register("word_problem")
def gen_word_problem(params: dict, answer_type: str) -> dict:
    op = params.get("operation", random.choice(["addition", "subtraction"]))
    min_val = params.get("min", 1)
    max_val = params.get("max", 20)
    max_result = params.get("max_result", max_val)

    name1, name2 = random.sample(_NAMES, 2)

    if op == "addition":
        template, items = random.choice(_ADD_TEMPLATES)
        for _ in range(50):
            a = random.randint(min_val, max_val)
            b = random.randint(min_val, max_val)
            if a + b <= max_result:
                break
        answer = a + b
        hint = f"Add the two numbers: {a} + {b} = ?"
    else:
        template, items = random.choice(_SUB_TEMPLATES)
        a = random.randint(max(min_val + 1, 3), max_val)
        b = random.randint(min_val, a - 1)
        answer = a - b
        hint = f"Subtract: {a} - {b} = ?"

    item_name, item_emoji = random.choice(items)
    story = template.format(name=name1, name2=name2, a=a, b=b, item=item_name)

    return {
        "question": story,
        "question_text": f"{item_emoji} {story}",
        "answer": answer,
        "options": make_options(answer, min_val=0, max_val=max_result + 5),
        "hint": hint,
        "type": answer_type,
    }
