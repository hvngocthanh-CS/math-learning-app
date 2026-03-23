"""Shape properties generator (Grade 1)."""

import random

from app.features.learn.generators import register
from app.features.learn.generators.common.constants import SHAPE_DATA, SHAPE_VISUALS
from app.features.learn.generators.common.helpers import make_options


@register("shape_properties")
def gen_shape_properties_bulk(params: dict, answer_type: str, count: int = 5) -> list:
    """Bulk generator: produces all shape problems at once for better variety."""
    shapes = params.get("shapes", ["circle", "square"])

    # Image-based questions (identify shape from emoji object)
    img_pool = []
    for s in shapes:
        for v in SHAPE_VISUALS.get(s, []):
            img_pool.append((s, v))
    random.shuffle(img_pool)

    if answer_type == "free_input":
        # Practice: all problems are image-based
        selected = img_pool[:count]
        problems = []
        for shape_key, visual in selected:
            shape = SHAPE_DATA[shape_key]
            problems.append({
                "question": f"What shape is {visual['label']}?",
                "question_text": visual["emoji"],
                "answer": shape["name"],
                "options": [SHAPE_DATA[s]["name"] for s in shapes],
                "hint": f"A {shape['name']} has {shape['sides']} sides and {shape['corners']} corners." if shape["sides"] > 0 else f"A {shape['name']} is round with no corners.",
                "type": answer_type,
                "subtype": "shape_identify",
                "shape_emoji": visual["emoji"],
                "shape_color": visual["color"],
                "shape_label": visual["label"],
            })
        return problems
    else:
        # Quiz: mix of image questions (3) + sides/corners questions (2)
        problems = []

        for shape_key, visual in img_pool[:3]:
            shape = SHAPE_DATA[shape_key]
            problems.append({
                "question": f"What shape is {visual['label']}?",
                "question_text": visual["emoji"],
                "answer": shape["name"],
                "options": [SHAPE_DATA[s]["name"] for s in shapes],
                "hint": f"Think about what {visual['label']} looks like.",
                "type": answer_type,
                "subtype": "shape_identify",
                "shape_emoji": visual["emoji"],
                "shape_color": visual["color"],
                "shape_label": visual["label"],
            })

        props_types = ["sides", "corners"]
        random.shuffle(props_types)
        used_shapes = list(shapes)
        random.shuffle(used_shapes)
        for i, q_type in enumerate(props_types):
            shape_key = used_shapes[i % len(used_shapes)]
            shape = SHAPE_DATA[shape_key]
            if q_type == "sides":
                problems.append({
                    "question": f"How many sides does a {shape['name']} have?",
                    "question_text": f"A {shape['name']} {shape['emoji']} has how many sides?",
                    "answer": shape["sides"],
                    "options": make_options(shape["sides"], min_val=0, max_val=6),
                    "hint": f"Count each straight edge of a {shape['name']}." if shape["sides"] > 0 else f"A {shape['name']} is round with no straight sides.",
                    "type": answer_type,
                })
            else:
                problems.append({
                    "question": f"How many corners does a {shape['name']} have?",
                    "question_text": f"A {shape['name']} {shape['emoji']} has how many corners?",
                    "answer": shape["corners"],
                    "options": make_options(shape["corners"], min_val=0, max_val=6),
                    "hint": f"Count where the sides meet." if shape["corners"] > 0 else f"A {shape['name']} has no corners - it is smooth and round.",
                    "type": answer_type,
                })

        random.shuffle(problems)
        return problems

# Mark as bulk so the dispatcher calls it with (params, answer_type, count)
gen_shape_properties_bulk.bulk = True
