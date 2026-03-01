# ============================================================================#
# EXERCISE 3: ft_plant_factory.py                                             #
# by: mohhammo                                                                #
# ============================================================================#


class Plant:
    """Plant class with streamlined initialization."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a plant ready for immediate use.

        Args:
            name: The name of the plant
            height: Starting height in centimeters
            age: Starting age in days
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    # Create multiple plants with different characteristics
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    # Display all created plants
    for plant in plants:
        print(f"Created: {plant.get_info()}")

    print(f"Total plants created: {len(plants)}")
