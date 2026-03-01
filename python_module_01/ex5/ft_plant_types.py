# ============================================================================#
# EXERCISE 5: ft_plant_types.py                                               #
# by: mohhammo                                                                #
# ============================================================================#


class Plant:
    """Base plant class with common features."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return basic plant information."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Flower plant with color and blooming capability."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with color attribute."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        """Return blooming message."""
        return f"{self.name} is blooming beautifully!"

    def get_info(self) -> str:
        """Return flower information including color."""
        return f"{self.name} (Flower): {self.height}cm, {self.age} days, " + \
               f"{self.color} color"


class Tree(Plant):
    """Tree plant with trunk diameter and shade production."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        """Calculate and return shade production message."""
        shade_area = int(self.trunk_diameter * 1.5)
        return f"{self.name} provides {shade_area} square meters of shade"

    def get_info(self) -> str:
        """Return tree information including trunk diameter."""
        return f"{self.name} (Tree): {self.height}cm, {self.age} days, " + \
               f"{self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Vegetable plant with harvest season and nutritional value."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize a vegetable with harvest and nutrition info."""
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_nutrition_info(self) -> str:
        """Return nutritional information."""
        return f"{self.name} is rich in {self.nutritional_value}"

    def get_info(self) -> str:
        """Return vegetable information including harvest season."""
        info = f"{self.name} (Vegetable): {self.height}cm,"
        return info + f" {self.age} days, {self.harvest_season} harvest"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 25, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 45)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 15, 60, "autumn", "vitamin A")

    print(rose.get_info())
    print(rose.bloom())
    print()
    print(oak.get_info())
    print(oak.produce_shade())
    print()
    print(tomato.get_info())
    print(tomato.get_nutrition_info())
