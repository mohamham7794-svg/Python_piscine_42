

import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {players}")

    all_capitalized: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized: list[str] = [
        name for name in players if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {only_capitalized}")

    score_dict: dict[str, int] = {
        name: random.randint(1, 1000) for name in all_capitalized
    }
    print(f"Score dict: {score_dict}")

    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")

    high_scores: dict[str, int] = {
        name: score for name, score in score_dict.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
