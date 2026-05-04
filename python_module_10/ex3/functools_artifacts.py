

from functools import reduce, partial, lru_cache, singledispatch
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }

    func = ops.get(operation)
    if func is None:
        raise ValueError("Unknown operation")

    return reduce(func, spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(arg: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @dispatch.register
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @dispatch.register
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return dispatch
