from functools_artifacts import (
    spell_reducer,
    memoized_fibonacci,
    spell_dispatcher,
)


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 40, 20, 30], 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch(3.14))