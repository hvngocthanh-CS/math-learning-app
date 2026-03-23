"""Comparison and ordering generators (Grade 1)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import EMOJI_GROUPS
from app.features.learn.generators.common.helpers import make_options


@register("comparison")
def gen_comparison(params: dict, answer_type: str) -> dict:
    """Generate comparison problems. Practice: pick > or <. Quiz: pick bigger/smaller number."""
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)

    a = random.randint(min_n, max_n)
    b = random.randint(min_n, max_n)
    while a == b:
        b = random.randint(min_n, max_n)

    if answer_type == "multiple_choice":
        ask_bigger = random.choice([True, False])
        if ask_bigger:
            answer = max(a, b)
            question = "Which number is larger?"
            hint = "Count up: the number you reach later is larger."
        else:
            answer = min(a, b)
            question = "Which number is smaller?"
            hint = "Count up: the number you reach first is smaller."
        return {
            "question": question,
            "question_text": f"{a} and {b}",
            "answer": answer,
            "options": [a, b],
            "hint": hint,
            "type": answer_type,
            "subtype": "comparison_pick",
        }
    else:
        if a > b:
            answer = ">"
            hint = f"{a} is bigger than {b}, so the alligator mouth opens toward {a}."
        else:
            answer = "<"
            hint = f"{a} is smaller than {b}."
        return {
            "question": f"Which sign goes between {a} and {b}?",
            "question_text": f"{a} ? {b}",
            "answer": answer,
            "options": [">", "<"],
            "hint": hint,
            "type": answer_type,
            "subtype": "comparison",
        }


@register("comparison_full")
def gen_comparison_full(params: dict, answer_type: str) -> dict:
    """Generate >, <, or = comparison problems."""
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)

    choice = random.choice(["greater", "less", "equal"])
    if choice == "equal":
        n = random.randint(min_n, max_n)
        a, b = n, n
        answer = "="
        hint = f"Both numbers are {n}. They are equal!"
    else:
        a = random.randint(min_n, max_n)
        b = random.randint(min_n, max_n)
        while a == b:
            b = random.randint(min_n, max_n)
        answer = ">" if a > b else "<"
        hint = f"{a} is {'bigger' if a > b else 'smaller'} than {b}."

    if answer_type == "multiple_choice":
        _, emoji_a = random.choice(EMOJI_GROUPS)
        _, emoji_b = random.choice(EMOJI_GROUPS)
        visual_a = emoji_a * a
        visual_b = emoji_b * b
        return {
            "question": "Compare the two groups! Which sign goes in between?",
            "question_text": f"{visual_a}  ?  {visual_b}",
            "answer": answer,
            "options": [">", "<", "="],
            "hint": hint,
            "type": answer_type,
            "subtype": "comparison_visual",
        }

    return {
        "question": f"Which sign goes between {a} and {b}?",
        "question_text": f"{a} ? {b}",
        "answer": answer,
        "options": [">", "<", "="],
        "hint": hint,
        "type": answer_type,
        "subtype": "comparison",
    }


@register("ordering")
def gen_ordering(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    num_count = params.get("count", 3)

    numbers = random.sample(range(min_n, max_n + 1), min(num_count, max_n - min_n + 1))
    numbers_str = ", ".join(str(n) for n in numbers)

    q_type = random.choice(["smallest", "biggest", "middle"])
    sorted_nums = sorted(numbers)

    if q_type == "smallest":
        answer = sorted_nums[0]
        question_text = f"Which is the smallest: {numbers_str}?"
        hint = "Find the number closest to 1."
    elif q_type == "biggest":
        answer = sorted_nums[-1]
        question_text = f"Which is the biggest: {numbers_str}?"
        hint = "Find the largest number."
    else:
        if len(sorted_nums) >= 3:
            answer = sorted_nums[len(sorted_nums) // 2]
            question_text = f"What is the middle number when ordering {numbers_str}?"
            hint = f"Order them: {', '.join(str(n) for n in sorted_nums)}. The middle one is..."
        else:
            answer = sorted_nums[0]
            question_text = f"Which is the smallest: {numbers_str}?"
            hint = "Find the number closest to 1."

    return {
        "question": question_text,
        "question_text": question_text,
        "answer": answer,
        "options": make_options(answer, min_val=min_n, max_val=max_n),
        "hint": hint,
        "type": answer_type,
    }
