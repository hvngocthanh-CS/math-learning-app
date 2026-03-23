"""Counting and number recognition generators (Grade 1)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import EMOJI_GROUPS, NUMBER_WORDS
from app.features.learn.generators.common.helpers import make_options, make_word_options


@register("counting")
def gen_counting(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    n = random.randint(min_n, max_n)
    name, emoji = random.choice(EMOJI_GROUPS)
    visual = emoji * n
    return {
        "question": f"How many {name}?",
        "question_text": f"Count the {name}: {visual}",
        "answer": n,
        "options": make_options(n, min_val=max(0, min_n - 1), max_val=max_n + 1),
        "hint": f"Point to each {name[:-1] if name.endswith('s') else name} and count carefully.",
        "type": answer_type,
    }


@register("number_recognition")
def gen_number_recognition(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    n = random.randint(min_n, max_n)
    word = NUMBER_WORDS.get(n, str(n))
    name, emoji = random.choice(EMOJI_GROUPS)
    visual = emoji * n

    if answer_type == "multiple_choice":
        variant = random.choice(["visual_to_number", "visual_to_word", "word_to_number", "number_to_word"])
    else:
        variant = random.choice(["visual_to_number", "word_to_number"])

    if variant == "visual_to_number":
        return {
            "question": "Count and choose the number!",
            "question_text": visual,
            "answer": n,
            "options": make_options(n, min_val=max(0, min_n - 1), max_val=max_n + 1),
            "hint": f"Point to each {name[:-1] if name.endswith('s') else name} and count.",
            "type": answer_type,
        }
    elif variant == "visual_to_word":
        word_opts = make_word_options(word, min_n, max_n)
        return {
            "question": "Count and choose the word!",
            "question_text": visual,
            "answer": word,
            "options": word_opts,
            "hint": f"Count the {name}, then find the matching word.",
            "type": answer_type,
        }
    elif variant == "word_to_number":
        return {
            "question": f"What number is '{word}'?",
            "question_text": f"What number is the word '{word}'?",
            "answer": n,
            "options": make_options(n, min_val=min_n, max_val=max_n),
            "hint": f"'{word.capitalize()}' comes after '{NUMBER_WORDS.get(n-1, '')}'.",
            "type": answer_type,
        }
    else:  # number_to_word
        word_opts = make_word_options(word, min_n, max_n)
        return {
            "question": f"The number {n} is called...",
            "question_text": f"What is the word for the number {n}?",
            "answer": word,
            "options": word_opts,
            "hint": f"Count up: {', '.join(NUMBER_WORDS.get(i, str(i)) for i in range(max(1,n-2), n+1))}.",
            "type": answer_type,
        }


@register("number_sequence")
def gen_number_sequence(params: dict, answer_type: str) -> dict:
    min_n = params.get("min", 1)
    max_n = params.get("max", 10)
    start = random.randint(min_n, max(min_n, max_n - 3))
    length = min(4, max_n - start + 1)
    seq = list(range(start, start + length))
    missing_idx = random.randint(0, len(seq) - 1)
    answer = seq[missing_idx]
    display = [str(x) if i != missing_idx else "_" for i, x in enumerate(seq)]
    seq_str = ", ".join(display)
    return {
        "question": f"Fill in: {seq_str}",
        "question_text": f"What is the missing number? {seq_str}",
        "answer": answer,
        "options": make_options(answer, min_val=min_n, max_val=max_n),
        "hint": f"Count in order. What goes between {answer-1} and {answer+1}?" if min_n < answer < max_n else "Think about the counting order.",
        "type": answer_type,
    }
