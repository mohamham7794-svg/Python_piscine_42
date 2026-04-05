# ============================================================================#
# EXERCISE 2:  ft_different_errors.py                                         #
# by: mohhammo                                                                #
# ============================================================================#


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        _ = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        _ = "temperature: " + 42  # type: ignore
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"\nTesting operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except (
            ValueError,
            ZeroDivisionError,
            FileNotFoundError,
            TypeError
        ) as e:
            print(f"Caught {type(e).__name__}: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
