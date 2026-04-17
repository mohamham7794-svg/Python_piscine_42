

import sys
import typing


def read_file(file_name: str) -> str:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    file: typing.IO | None = None
    try:
        file = open(file_name, "r")
        content: str = file.read()

        print("---")
        print(content, end="")
        print("---")

        return content

    except OSError as e:
        raise OSError(f"Error opening file '{file_name}': {e}") from e

    finally:
        if file is not None:
            file.close()
            print(f"File '{file_name}' closed.")


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    new_lines: list[str] = [line + "#" for line in lines]
    return "\n".join(new_lines) + "\n"


def save_file(file_name: str, content: str) -> None:
    print(f"Saving data to '{file_name}'")

    file: typing.IO[str] | None = None
    try:
        file = open(file_name, "w")
        file.write(content)
        print(f"Data saved in file '{file_name}'.")
    except OSError as e:
        raise OSError(f"Error opening file '{file_name}': {e}") from e
    finally:
        if file is not None:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    file_name: str = sys.argv[1]

    try:
        content: str = read_file(file_name)
    except OSError as e:
        print(e)
        return

    new_content: str = transform_content(content)

    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")

    dest: str = input("Enter new file name (or empty): ")

    if not dest:
        print("Not saving data.")
        return

    try:
        save_file(dest, new_content)
    except OSError as e:
        print(e)


if __name__ == "__main__":
    main()
