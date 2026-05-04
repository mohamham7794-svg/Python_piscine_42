from lambda_spells import artifact_sorter, spell_transformer


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Shadow Dagger", "power": 60, "type": "blade"},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before"
        f" {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))