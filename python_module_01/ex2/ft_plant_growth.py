# ============================================================================#
# EXERCISE 2: ft_plant_growth.py                                              #
# by: mohhammo                                                                #
# ============================================================================#


class Plant:
    """Plant class with growth simulation capabilities."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a plant with name, height, and age."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def grow(self, amount: int = 1) -> None:
        """Increase plant height by the specified amount."""
        self.height += amount

    def age_one_day(self) -> None:
        """Age the plant by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Return current plant information as a string."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    initial_height = rose.height
    for day in range(7):
        rose.grow(1)
        rose.age_one_day()
    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")
