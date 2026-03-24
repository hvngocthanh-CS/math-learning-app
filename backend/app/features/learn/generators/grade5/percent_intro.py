"""Introduction to percentages generator (Grade 5).

Converts simple fractions to percentages and vice versa.
"""

import random

from app.features.learn.generators import register

# (numerator, denominator, percentage)
_FRACTIONS = [
    (1, 2, 50),
    (1, 4, 25),
    (3, 4, 75),
    (1, 5, 20),
    (2, 5, 40),
    (3, 5, 60),
    (4, 5, 80),
    (1, 10, 10),
    (3, 10, 30),
    (7, 10, 70),
    (9, 10, 90),
    (1, 1, 100),
]


def _make_percent_options(answer):
    """Generate percentage options that are common mistakes."""
    options = {answer}
    # Common wrong answers: nearby multiples of 5/10/25
    candidates = [
        answer + 25, answer - 25,
        answer + 10, answer - 10,
        answer + 5, answer - 5,
        answer * 2,
        100 - answer,
    ]
    for c in candidates:
        if 0 < c <= 100 and c != answer and c not in options:
            options.add(c)
        if len(options) >= 4:
            break
    # Fallback
    while len(options) < 4:
        c = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90])
        if c != answer:
            options.add(c)
    result = list(options)[:4]
    random.shuffle(result)
    return result


@register("percent_intro")
def gen_percent_intro(params: dict, answer_type: str) -> dict:
    num, den, pct = random.choice(_FRACTIONS)

    variant = random.choice(["frac_to_pct", "frac_to_pct", "pct_to_frac", "score"])

    if variant == "frac_to_pct":
        question = f"What is {num}/{den} as a percentage?"
        question_text = f"{num}/{den} = ? %"
        answer = pct
        hint = f"{num}/{den} → 100 ÷ {den} = {100 // den} → {100 // den} × {num} = {pct}%."
        options = _make_percent_options(answer)
    elif variant == "pct_to_frac":
        # Ask which fraction equals the percentage
        question = f"{pct}% is the same as which fraction?"
        question_text = f"{pct}% = ?/{den}"
        answer = num
        hint = f"{pct}% means {pct} out of 100. Simplify: {pct}/100 = {num}/{den}."
        # Options: other numerators over the same denominator
        options = {answer}
        for c in [answer + 1, answer - 1, answer + 2, den - answer, den]:
            if 0 < c <= den and c != answer:
                options.add(c)
            if len(options) >= 4:
                break
        while len(options) < 4:
            options.add(random.randint(1, den))
        options = list(options)[:4]
        random.shuffle(options)
    else:
        # Score out of 10
        score = random.randint(1, 10)
        pct_answer = score * 10
        question = f"You got {score} out of 10 on a quiz. What is your score as a percentage?"
        question_text = f"{score}/10 = ? %"
        answer = pct_answer
        hint = f"{score} out of 10 = {score}/10. Multiply by 10: {score} × 10 = {pct_answer}%."
        options = _make_percent_options(answer)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
