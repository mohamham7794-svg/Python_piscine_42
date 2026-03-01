# ============================================================================#
# EXERCISE 6: ft_garden_analytics.py                                          #
# by: mohhammo                                                                #
# ============================================================================#


class Plant:
    """Base plant class."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant."""
        self.name: str = name
        self.height: int = height

    def grow(self) -> None:
        """Increase plant height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_height(self) -> int:
        """Return plant height."""
        return self.height

    @staticmethod
    def is_valid_height(height: int) -> bool:
        """Validate if height is positive."""
        return height > 0


class FloweringPlant(Plant):
    """Plant that can flower."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant."""
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = True

    def __str__(self) -> str:
        """String representation of flowering plant."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers " + \
               f"({bloom_status})"


class PrizeFlower(FloweringPlant):
    """Special flowering plant with prize points."""

    def __init__(self, name: str, height: int, color: str,
                 prize_points: int) -> None:
        """Initialize a prize flower."""
        super().__init__(name, height, color)
        self.prize_points: int = prize_points

    def __str__(self) -> str:
        """String representation including prize points."""
        return super().__str__() + f", Prize points: {self.prize_points}"


class GardenManager:
    """Manages multiple gardens with analytics."""

    _total_gardens: int = 0

    class GardenStats:
        """Nested class for garden statistics."""

        def __init__(self) -> None:
            """Initialize statistics tracker."""
            self.plants_added: int = 0
            self.total_growth: int = 0
            self.regular_plants: int = 0
            self.flowering_plants: int = 0
            self.prize_flowers: int = 0

        def record_plant_addition(self, plant: Plant) -> None:
            """Record when a plant is added."""
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def record_growth(self) -> None:
            """Record growth event."""
            self.total_growth += 1

        def get_summary(self) -> str:
            """Return statistics summary."""
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_plants} regular, "
                    f"{self.flowering_plants} flowering, "
                    f"{self.prize_flowers} prize flowers")

    def __init__(self, owner_name: str) -> None:
        """Initialize a garden manager."""
        self.owner_name: str = owner_name
        self.plants: list[Plant] = []
        self.stats = GardenManager.GardenStats()
        GardenManager._total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.stats.record_plant_addition(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_all_plants_grow(self) -> None:
        """Help all plants in the garden grow."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def get_garden_score(self) -> int:
        """Calculate total garden score based on plant heights."""
        return sum(plant.get_height() for plant in self.plants)

    def display_report(self) -> None:
        """Display comprehensive garden report."""
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, (FloweringPlant, PrizeFlower)):
                print(f"- {plant}")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        print(self.stats.get_summary())

    @classmethod
    def create_garden_network(cls, *owner_names: str) -> list['GardenManager']:
        """
        Create multiple gardens at once (class method).

        Args:
            *owner_names: Variable number of owner names

        Returns:
            List of GardenManager instances
        """
        return [cls(name) for name in owner_names]

    @classmethod
    def get_total_gardens(cls) -> int:
        """Return the total number of gardens created."""
        return cls._total_gardens

    @staticmethod
    def compare_garden_scores(garden1: 'GardenManager',
                              garden2: 'GardenManager') -> str:
        """
        Compare scores of two gardens (static method).

        Args:
            garden1: First garden
            garden2: Second garden

        Returns:
            Comparison message
        """
        score1 = garden1.get_garden_score()
        score2 = garden2.get_garden_score()
        return f"Garden scores - {garden1.owner_name}: {score1}, " + \
               f"{garden2.owner_name}: {score2}"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)
    bob_garden.add_plant(Plant("Fern", 30))
    bob_garden.add_plant(FloweringPlant("Tulip", 20, "pink"))
    print()
    alice_garden.help_all_plants_grow()
    alice_garden.display_report()
    print(f"\nHeight validation test: {Plant.is_valid_height(25)}")
    print(GardenManager.compare_garden_scores(alice_garden, bob_garden))
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
