

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name, qty_str = parts[0], parts[1]
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            inventory[item_name] = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])

    if not inventory:
        print("Inventory is empty.")
        return

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        pct = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {pct}%")

    keys = list(inventory.keys())
    most = max(inventory, key=lambda k: (inventory[k], -keys.index(k)))
    least = min(inventory, key=lambda k: (inventory[k], keys.index(k)))
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
