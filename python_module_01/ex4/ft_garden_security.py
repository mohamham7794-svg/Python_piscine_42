# ============================================================================#
# EXERCISE 4: ft_garden_security.py                                           #
# by: mohhammo                                                                #
# ============================================================================#


class SecurePlant:
    """Plant class with protected data and validation."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a secure plant with validated data."""
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_age(age)

    def get_name(self) -> str:
        """Get the plant name."""
        return self.__name

    def get_height(self) -> int:
        """Get the plant height."""
        return self.__height

    def set_height(self, height: int) -> None:
        """
        Set plant height with validation.

        Args:
            height: New height in centimeters (must be non-negative)
        """
        if height < 0:
            print(f"Security: Negative height rejected")
            return
        self.__height = height

    def get_age(self) -> int:
        """Get the plant age."""
        return self.__age

    def set_age(self, age: int) -> None:
        """
        Set plant age with validation.

        Args:
            age: New age in days (must be non-negative)
        """
        if age < 0:
            print(f"Security: Negative age rejected")
            return
        self.__age = age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print(f"Plant created: {plant.get_name()}")
    print(f"Height updated: {plant.get_height()}cm [OK]")
    print(f"Age updated: {plant.get_age()} days [OK]")
    print(f"Invalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)
    print(f"Current plant: {plant.get_name()} " +
          f"({plant.get_height()}cm, {plant.get_age()} days)")
