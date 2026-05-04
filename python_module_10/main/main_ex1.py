from higher_magic import (
    spell_combiner,
    power_amplifier,
    conditional_caster,
    spell_sequence,
)


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} armor"


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_power = 10
    amplified = power_amplifier(
        lambda t, p: p, 3
    )("Dragon", original_power)
    print(f"Original: {original_power}, Amplified: {amplified}")
