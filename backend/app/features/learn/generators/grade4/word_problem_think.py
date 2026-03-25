"""Thinking word problems for Grade 4 — require a bit more reasoning."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.helpers import make_options

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

# ─── ADDITION templates ───────────────────────────────────────────

_ADD_TEMPLATES = [
    # Two-step: add three numbers
    {
        "template": "{name} has {a} marbles. {name2} gives {name} {b} more marbles. Then {name} finds {c} marbles on the ground. How many marbles does {name} have now?",
        "calc": lambda a, b, c: a + b + c,
        "hint": "Add all the marbles together: {a} + {b} + {c} = {ans}.",
        "emoji": "🔮",
    },
    {
        "template": "A store has {a} red apples and {b} green apples. In the afternoon, they receive {c} more apples. How many apples does the store have in total?",
        "calc": lambda a, b, c: a + b + c,
        "hint": "Add all the apples: {a} + {b} + {c} = {ans}.",
        "emoji": "🍎",
    },
    {
        "template": "There are {a} boys and {b} girls in a class. {c} more students join. How many students are there now?",
        "calc": lambda a, b, c: a + b + c,
        "hint": "First find the original total: {a} + {b}. Then add the new students: + {c} = {ans}.",
        "emoji": "🏫",
    },
    # Distractor: extra info to ignore
    {
        "template": "{name} reads {a} pages on Monday and {b} pages on Tuesday. {name2} reads {c} pages in total. How many pages did {name} read altogether?",
        "calc": lambda a, b, c: a + b,
        "hint": "The question asks about {name} only: {a} + {b} = {ans}.",
        "emoji": "📖",
    },
    # Compare & total
    {
        "template": "{name} has {a} stickers. {name2} has {b} stickers. {name3} has {c} stickers. How many stickers do they have altogether?",
        "calc": lambda a, b, c: a + b + c,
        "hint": "Add all three: {a} + {b} + {c} = {ans}.",
        "emoji": "⭐",
    },
    # Table / list style
    {
        "template": "A fruit shop sold {a} oranges on Monday, {b} oranges on Tuesday, and {c} oranges on Wednesday. How many oranges were sold in total?",
        "calc": lambda a, b, c: a + b + c,
        "hint": "Add up all three days: {a} + {b} + {c} = {ans}.",
        "emoji": "🍊",
    },
    # Find the missing addend (reverse thinking)
    {
        "template": "{name} has some toys. After receiving {b} toys from {name2}, {name} now has {total} toys. How many toys did {name} start with?",
        "calc": lambda a, b, c: a,  # a is the starting amount
        "hint": "Think backwards: {total} - {b} = {ans}.",
        "emoji": "🧸",
        "variant": "missing_start",
    },
    # Comparison: how many in total between two
    {
        "template": "{name} scored {a} points in the first game and {b} points in the second game. {name} needs {total} points to win a prize. How many more points does {name} need?",
        "calc": lambda a, b, c: c,  # c = total - a - b
        "hint": "First find what {name} has: {a} + {b} = {ab}. Then: {total} - {ab} = {ans}.",
        "emoji": "🏆",
        "variant": "how_many_more",
    },
]

# ─── SUBTRACTION templates ────────────────────────────────────────

_SUB_TEMPLATES = [
    # Classic two-step subtract
    {
        "template": "{name} has {total} stickers. {name} gives {a} stickers to {name2} and {b} stickers to {name3}. How many stickers does {name} have left?",
        "calc": lambda total, a, b: total - a - b,
        "hint": "Subtract both gifts: {total} - {a} - {b} = {ans}.",
        "emoji": "⭐",
    },
    {
        "template": "A bakery bakes {total} cookies. They sell {a} in the morning and {b} in the afternoon. How many cookies are left?",
        "calc": lambda total, a, b: total - a - b,
        "hint": "Subtract both sales: {total} - {a} - {b} = {ans}.",
        "emoji": "🍪",
    },
    {
        "template": "{name} has ${total}. {name} spends ${a} on a book and ${b} on lunch. How much money does {name} have left?",
        "calc": lambda total, a, b: total - a - b,
        "hint": "Subtract both expenses: ${total} - ${a} - ${b} = ${ans}.",
        "emoji": "💰",
    },
    {
        "template": "A bus has {total} passengers. At the first stop, {a} people get off. At the second stop, {b} more get off. How many passengers are still on the bus?",
        "calc": lambda total, a, b: total - a - b,
        "hint": "Subtract passengers who got off: {total} - {a} - {b} = {ans}.",
        "emoji": "🚌",
    },
    # Find the difference
    {
        "template": "{name} has {total} candies. {name2} has {a} candies. How many more candies does {name} have than {name2}?",
        "calc": lambda total, a, b: total - a,
        "hint": "Find the difference: {total} - {a} = {ans}.",
        "emoji": "🍬",
        "variant": "difference",
    },
    # How many given away (reverse thinking)
    {
        "template": "{name} had {total} balloons. After giving some to {name2}, {name} has {remaining} balloons left. How many balloons did {name} give away?",
        "calc": lambda total, a, b: total - a,  # a = remaining
        "hint": "Subtract what is left from the start: {total} - {remaining} = {ans}.",
        "emoji": "🎈",
        "variant": "find_given",
    },
    # Spending from a budget
    {
        "template": "{name} has {total} minutes of free time. {name} spends {a} minutes reading and {b} minutes drawing. How many minutes are left?",
        "calc": lambda total, a, b: total - a - b,
        "hint": "Subtract both activities: {total} - {a} - {b} = {ans}.",
        "emoji": "⏰",
    },
    # Distance / progress
    {
        "template": "A trail is {total} meters long. {name} has already walked {a} meters. How many meters are left to finish the trail?",
        "calc": lambda total, a, b: total - a,
        "hint": "Subtract distance walked: {total} - {a} = {ans}.",
        "emoji": "🥾",
        "variant": "remaining",
    },
]

# ─── MIXED templates (add then subtract or vice versa) ────────────

_MIXED_TEMPLATES = [
    {
        "template": "{name} has {a} cards. {name} buys {b} more cards but then gives {c} cards to {name2}. How many cards does {name} have now?",
        "calc": lambda a, b, c: a + b - c,
        "hint": "First add: {a} + {b} = {ab}. Then subtract: {ab} - {c} = {ans}.",
        "emoji": "🃏",
    },
    {
        "template": "A pond has {a} fish. {c} fish swim away but {b} new fish arrive. How many fish are in the pond now?",
        "calc": lambda a, b, c: a - c + b,
        "hint": "First subtract: {a} - {c} = {ac}. Then add: {ac} + {b} = {ans}.",
        "emoji": "🐟",
    },
    {
        "template": "{name} bakes {a} cupcakes. {name} gives {c} to {name2} and then makes {b} more. How many cupcakes does {name} have?",
        "calc": lambda a, b, c: a - c + b,
        "hint": "First subtract: {a} - {c} = {ac}. Then add: {ac} + {b} = {ans}.",
        "emoji": "🧁",
    },
    {
        "template": "A garden has {a} flowers. {name} picks {c} flowers but plants {b} new ones. How many flowers are there now?",
        "calc": lambda a, b, c: a - c + b,
        "hint": "First subtract: {a} - {c} = {ac}. Then add: {ac} + {b} = {ans}.",
        "emoji": "🌷",
    },
]


def _gen_add(min_val, max_val, names):
    name, name2, name3 = names
    tmpl = random.choice(_ADD_TEMPLATES)
    variant = tmpl.get("variant", "")

    if variant == "missing_start":
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val // 2)
        total = a + b
        c = 0
        answer = a
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, a=a, b=b, c=c, total=total,
        )
        hint = tmpl["hint"].format(name=name, a=a, b=b, total=total, ans=answer)
    elif variant == "how_many_more":
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        extra = random.randint(min_val, max_val // 2)
        total = a + b + extra
        c = extra
        answer = extra
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, a=a, b=b, c=c, total=total,
        )
        hint = tmpl["hint"].format(name=name, a=a, b=b, ab=a + b, total=total, ans=answer)
    else:
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        c = random.randint(min_val, max_val // 2)
        answer = tmpl["calc"](a, b, c)
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, a=a, b=b, c=c,
        )
        hint = tmpl["hint"].format(name=name, a=a, b=b, c=c, ans=answer)

    return question_text, answer, hint, tmpl["emoji"]


def _gen_sub(min_val, max_val, names):
    name, name2, name3 = names
    tmpl = random.choice(_SUB_TEMPLATES)
    variant = tmpl.get("variant", "")

    if variant == "difference":
        total = random.randint(max_val // 2, max_val + min_val)
        a = random.randint(min_val, total - 1)
        b = 0
        answer = total - a
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, total=total, a=a, b=b,
        )
        hint = tmpl["hint"].format(total=total, a=a, ans=answer)
    elif variant == "find_given":
        remaining = random.randint(min_val, max_val)
        given = random.randint(min_val, max_val)
        total = remaining + given
        a = remaining
        b = 0
        answer = given
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, total=total, a=a, b=b,
            remaining=remaining,
        )
        hint = tmpl["hint"].format(total=total, remaining=remaining, ans=answer)
    elif variant == "remaining":
        total = random.randint(max_val, max_val * 2)
        a = random.randint(min_val, total - min_val)
        b = 0
        answer = total - a
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, total=total, a=a, b=b,
        )
        hint = tmpl["hint"].format(total=total, a=a, ans=answer)
    else:
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val // 2)
        total = a + b + random.randint(min_val, max_val)
        answer = tmpl["calc"](total, a, b)
        question_text = tmpl["template"].format(
            name=name, name2=name2, name3=name3, total=total, a=a, b=b,
        )
        hint = tmpl["hint"].format(total=total, a=a, b=b, ans=answer)

    return question_text, answer, hint, tmpl["emoji"]


def _gen_mixed(min_val, max_val, names):
    name, name2, name3 = names
    tmpl = random.choice(_MIXED_TEMPLATES)
    a = random.randint(min_val + 20, max_val)
    b = random.randint(min_val, max_val // 2)
    c = random.randint(min_val, min(a + b - 1, max_val // 2))
    answer = tmpl["calc"](a, b, c)
    question_text = tmpl["template"].format(
        name=name, name2=name2, a=a, b=b, c=c,
    )
    hint = tmpl["hint"].format(a=a, b=b, c=c, ab=a + b, ac=a - c, ans=answer)
    return question_text, answer, hint, tmpl["emoji"]


@register("word_problem_think")
def gen_word_problem_think(params: dict, answer_type: str) -> dict:
    min_val = params.get("min", 10)
    max_val = params.get("max", 100)
    ops = params.get("ops", ["add", "subtract", "mixed"])

    names = random.sample(_NAMES, 3)
    op = random.choice(ops)

    if op == "add":
        question_text, answer, hint, emoji = _gen_add(min_val, max_val, names)
    elif op == "subtract":
        question_text, answer, hint, emoji = _gen_sub(min_val, max_val, names)
    else:
        question_text, answer, hint, emoji = _gen_mixed(min_val, max_val, names)

    return {
        "question": question_text,
        "question_text": question_text,
        "emoji": emoji,
        "answer": answer,
        "options": make_options(answer, min_val=max(0, answer - 30), max_val=answer + 30),
        "hint": hint,
        "type": answer_type,
    }
