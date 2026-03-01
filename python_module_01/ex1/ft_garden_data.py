# ============================================================================#
# EXERCISE 1: ft_garden_data.py                                               #
# by: mohhammo                                                                #
# ============================================================================#


class Plant:
    """Blueprint for creating plant objects with their attributes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height, and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
