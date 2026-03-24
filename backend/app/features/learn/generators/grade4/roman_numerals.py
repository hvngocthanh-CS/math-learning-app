"""Roman numerals generator (Grade 4)."""

import random

from app.features.learn.generators import register

_ROMAN_VALUES = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]


def _to_roman(n: int) -> str:
    result = []
    for value, symbol in _ROMAN_VALUES:
        while n >= value:
            result.append(symbol)
            n -= value
    return "".join(result)


def _make_roman_options(correct: str, count: int = 4) -> list:
    """Generate plausible wrong Roman numeral options."""
    options = {correct}
    val = _from_roman(correct)
    nearby = [val - 2, val - 1, val + 1, val + 2, val + 5, val - 5, val + 10, val - 10]
    random.shuffle(nearby)
    for n in nearby:
        if 1 <= n <= 1000 and len(options) < count:
            r = _to_roman(n)
            if r != correct:
                options.add(r)
    result = list(options)[:count]
    random.shuffle(result)
    return result


def _from_roman(s: str) -> int:
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        val = roman_map[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total


def _make_number_options(correct: int, count: int = 4) -> list:
    options = {correct}
    nearby = [correct - 2, correct - 1, correct + 1, correct + 2,
              correct + 5, correct - 5, correct + 10, correct - 10]
    random.shuffle(nearby)
    for n in nearby:
        if 1 <= n <= 1000 and n != correct and len(options) < count:
            options.add(n)
    result = list(options)[:count]
    random.shuffle(result)
    return result


@register("roman_numerals")
def gen_roman_numerals(params: dict, answer_type: str) -> dict:
    max_val = params.get("max_val", 100)
    min_val = params.get("min_val", 1)

    number = random.randint(min_val, max_val)
    roman = _to_roman(number)

    variant = random.choice(["to_roman", "to_number"])

    if variant == "to_roman":
        question = f"Write {number} in Roman numerals."
        question_text = f"{number} = ?"
        answer = roman
        hint = f"Remember: I=1, V=5, X=10, L=50, C=100. Build {number} step by step."
        options = _make_roman_options(roman)
    else:
        question = f"What number is {roman}?"
        question_text = f"{roman} = ?"
        answer = number
        hint = f"Read each symbol: I=1, V=5, X=10, L=50, C=100. If a smaller value is before a larger, subtract it."
        options = _make_number_options(number)

    return {
        "question": question,
        "question_text": question_text,
        "answer": answer,
        "options": options,
        "hint": hint,
        "type": answer_type,
    }
