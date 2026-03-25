"""Finding percentages of a number generator (Grade 5).

Uses friendly percentages (10%, 20%, 25%, 50%, 75%) and
numbers that divide evenly.
"""

import random

from app.features.learn.generators import register

_NAMES = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Lucas", "Mia", "Jack", "Lily", "Ben"]

# (percentage, divisor) — e.g. 25% = divide by 4
_EASY_PERCENTS = [
    (10, 10),
    (20, 5),
    (25, 4),
    (50, 2),
    (75, None),   # special: 3/4
]

_WORD_TEMPLATES = [
    {
        "template": "A shirt costs ${total}. It is {pct}% off. How much is the discount?",
        "hint": "{pct}% of ${total} = ${ans}.",
        "emoji": "🏷️",
    },
    {
        "template": "{name} has {total} stickers and gives away {pct}% of them. How many stickers does {name} give away?",
        "hint": "{pct}% of {total} = {ans} stickers.",
        "emoji": "⭐",
    },
    {
        "template": "A class has {total} students. {pct}% of them are girls. How many girls are there?",
        "hint": "{pct}% of {total} = {ans} girls.",
        "emoji": "🏫",
    },
    {
        "template": "{name} scores {pct}% on a test with {total} questions. How many questions did {name} get right?",
        "hint": "{pct}% of {total} = {ans} questions.",
        "emoji": "📝",
    },
]


def _make_pct_options(answer, total):
    """Generate plausible options for percentage-of-number problems."""
    options = {answer}
    candidates = [
        total - answer,        # complement
        answer * 2,            # doubled
        answer // 2 if answer >= 2 else answer + 5,  # halved
        total // 10,           # 10% (common mistake)
        total // 2,            # 50% (common mistake)
        total,                 # 100% (forgot to divide)
        answer + 5,
        answer - 5,
    ]
    for c in candidates:
        if c > 0 and c != answer and c not in options:
            options.add(c)
        if len(options) >= 4:
            break
    while len(options) < 4:
        options.add(answer + random.choice([1, 2, 3, -1, -2, -3]))
    result = list(options)[:4]
    random.shuffle(result)
    return result


@register("percent_of_number")
def gen_percent_of_number(params: dict, answer_type: str) -> dict:
    pct, divisor = random.choice(_EASY_PERCENTS)

    if pct == 75:
        # 75% = 3/4 → need number divisible by 4
        base = random.randint(2, 25)
        total = base * 4
        answer = base * 3
    else:
        base = random.randint(2, 20)
        total = base * divisor
        answer = base * (pct // (100 // divisor))
        # simplify: answer = total * pct / 100
        answer = total * pct // 100

    variant = random.choice(["direct", "direct", "word"])

    if variant == "word":
        name = random.choice(_NAMES)
        tmpl = random.choice(_WORD_TEMPLATES)
        question = tmpl["template"].format(name=name, total=total, pct=pct, ans=answer)
        question_text = f"{pct}% of {total} = ?"
        hint = tmpl["hint"].format(name=name, total=total, pct=pct, ans=answer)
        emoji = tmpl["emoji"]
        return {
            "question": question,
            "question_text": question_text,
            "answer": answer,
            "options": _make_pct_options(answer, total),
            "hint": hint,
            "type": answer_type,
            "emoji": emoji,
        }

    question = f"What is {pct}% of {total}?"
    question_text = f"{pct}% of {total} = ?"

    if pct == 10:
        hint = f"10% = divide by 10. {total} ÷ 10 = {answer}."
    elif pct == 50:
        hint = f"50% = half. {total} ÷ 2 = {answer}."
    elif pct == 25:
        hint = f"25% = a quarter. {total} ÷ 4 = {answer}."
    elif pct == 75:
        quarter = total // 4
        hint = f"75% = three quarters. {total} ÷ 4 = {quarter}. Then {quarter} × 3 = {answer}."
    else:
        ten_pct = total // 10
        multiplier = pct // 10
        hint = f"First find 10%: {total} ÷ 10 = {ten_pct}. Then × {multiplier}: {ten_pct} × {multiplier} = {answer}."

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": _make_pct_options(answer, total),
        "hint": hint,
        "type": answer_type,
    }
