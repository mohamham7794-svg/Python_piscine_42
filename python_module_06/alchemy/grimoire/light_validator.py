

LIGHT_ALLOWED: list[str] = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    for allowed in LIGHT_ALLOWED:
        if allowed in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
