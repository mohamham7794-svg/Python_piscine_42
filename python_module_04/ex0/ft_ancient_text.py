

import sys
import typing


def read_file(file_name: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    file: typing.IO | None = None
    try:
        file = open(file_name, "r")
        print("---")
        print(file.read(), end="")
        print("---")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
