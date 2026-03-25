"""
Problem generator registry and dispatcher.

Each grade subpackage registers its generators via the @register decorator.
The public API is generate_problems(config, mode).
"""

import random
from typing import Dict, List, Any, Callable

# ── Registry ────────────────────────────────────────────────────────

GENERATOR_REGISTRY: Dict[str, Callable] = {}


def register(problem_type: str):
    """Decorator to register a generator function for a problem type."""
    def wrapper(func: Callable):
        GENERATOR_REGISTRY[problem_type] = func
        return func
    return wrapper


# ── Dispatcher ──────────────────────────────────────────────────────

def generate_problems(config: Dict[str, Any], mode: str = "practice") -> List[Dict]:
    """
    Generate random problems based on config.
    mode: "practice" (free_input) or "quiz" (multiple_choice)
    """
    problem_type = config["type"]
    params = config.get("params", {})
    count = config.get("count", 5)
    answer_type = "free_input" if mode == "practice" else "multiple_choice"

    generator = GENERATOR_REGISTRY.get(problem_type)
    if not generator:
        print(f"[WARN] Generator '{problem_type}' NOT FOUND. Registry has {len(GENERATOR_REGISTRY)} generators: {sorted(GENERATOR_REGISTRY.keys())}")
        return []

    # Generators marked as bulk produce all problems at once
    if getattr(generator, "bulk", False):
        return generator(params, answer_type, count)

    # Standard generators produce one problem at a time; deduplicate
    problems = []
    seen = set()
    attempts = 0
    while len(problems) < count and attempts < count * 10:
        problem = generator(params, answer_type)
        key = (problem["answer"], problem["question_text"])
        if key not in seen:
            seen.add(key)
            problems.append(problem)
        attempts += 1

    return problems


# ── Import grade subpackages to trigger registration ────────────────
from app.features.learn.generators import grade1  # noqa: E402,F401
from app.features.learn.generators import grade2  # noqa: E402,F401
from app.features.learn.generators import grade3  # noqa: E402,F401
from app.features.learn.generators import grade4  # noqa: E402,F401
from app.features.learn.generators import grade5  # noqa: E402,F401
