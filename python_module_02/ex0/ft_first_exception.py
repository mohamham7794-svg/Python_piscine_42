# ============================================================================#
# EXERCISE 0:  ft_first_exception.py                                          #
# by: mohhammo                                                                #
# ============================================================================#


def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    for temp in ["25", "abc"]:
        print(f"\nInput data is '{temp}'")
        try:
            result = input_temperature(temp)
            print(f"Temperature is now {result}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
