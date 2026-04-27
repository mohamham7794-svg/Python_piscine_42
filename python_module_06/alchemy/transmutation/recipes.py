

import elements
from ..elements import create_air


def lead_to_gold() -> str:
    from alchemy.potions import strength_potion
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}'"
        f" mixed with '{elements.create_fire()}'"
    )
