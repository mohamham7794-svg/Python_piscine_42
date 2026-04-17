

def secure_archive(
    file_name: str,
    action: str = "read",
    content: str = ""
) -> tuple:

    if action == "read":
        try:
            with open(file_name, "r") as f:
                return (True, f.read())
        except OSError as e:
            return (False, str(e))

    elif action == "write":
        try:
            with open(file_name, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except OSError as e:
            return (False, str(e))

    else:
        return (False, f"Invalid action: {action}")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_fragment.txt", "write", result[1]))


if __name__ == "__main__":
    main()
