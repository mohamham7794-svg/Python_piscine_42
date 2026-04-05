

import random

ALL_ACHIEVEMENTS: list[str] = [
    "First Steps", "Speed Runner", "Boss Slayer", "Treasure Hunter",
    "Master Explorer", "Survivor", "Strategist", "Unstoppable",
    "Untouchable", "Crafting Genius", "World Savior", "Collector Supreme",
    "Sharp Mind", "Hidden Path Finder", "Dragon Tamer", "Legendary Hero",
    "Night Owl", "Completionist", "Pacifist", "Berserker",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 10)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set()
    for achievements in players.values():
        all_achievements = set.union(all_achievements, achievements)
    print(f"\nAll distinct achievements: {all_achievements}")

    common: set[str] = all_achievements.copy()
    for achievements in players.values():
        common = set.intersection(common, achievements)
    print(f"Common achievements: {common}")

    print()
    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = set.union(others, other_ach)
        unique = set.difference(achievements, others)
        print(f"Only {name} has: {unique}")

    print()
    for name, achievements in players.items():
        missing = set.difference(all_achievements, achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
