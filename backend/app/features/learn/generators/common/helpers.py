"""
Shared helper functions used by problem generators across all grades.
"""

import random
from typing import List

from app.features.learn.generators.common.constants import NUMBER_WORDS


def make_options(answer: int, count: int = 4, min_val: int = 0, max_val: int = 20) -> List[int]:
    """Generate multiple choice options that include the correct answer."""
    options = {answer}
    attempts = 0
    while len(options) < count and attempts < 50:
        offset = random.choice([-2, -1, 1, 2, -3, 3])
        val = answer + offset
        if min_val <= val <= max_val and val != answer:
            options.add(val)
        attempts += 1
    while len(options) < count:
        val = random.randint(min_val, max_val)
        if val != answer:
            options.add(val)
    result = list(options)
    random.shuffle(result)
    return result


def make_word_options(correct_word: str, min_n: int, max_n: int, count: int = 4) -> list:
    """Generate word options for multiple choice, including the correct answer."""
    word_options = {correct_word}
    while len(word_options) < count:
        rand_n = random.randint(min_n, max_n)
        word_options.add(NUMBER_WORDS.get(rand_n, str(rand_n)))
    result = list(word_options)
    random.shuffle(result)
    return result
