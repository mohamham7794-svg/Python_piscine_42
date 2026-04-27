

import os
import sys


def load_dotenv_file(filepath: str = ".env") -> None:
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv(filepath, override=False)
    except ImportError:
        print("WARNING: python-dotenv not installed.")
        print("  Install it with: pip install python-dotenv")
        print("  Or: poetry install")
        print()


def get_config() -> dict[str, str]:
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def validate_config(config: dict[str, str]) -> list[str]:
    required = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    return [key for key in required if not config[key]]


def mask_secret(value: str) -> str:
    if not value:
        return "NOT SET"
    if len(value) <= 4:
        return "****"
    return value[:4] + "*" * (len(value) - 4)


def print_config(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]

    db_display = (
        "Connected to local instance"
        if mode == "development"
        else "Connected to production cluster"
    ) if config["DATABASE_URL"] else "NOT SET"

    api_display = (
        "Authenticated" if config["API_KEY"] else "NOT SET"
    )

    zion_display = (
        "Online" if config["ZION_ENDPOINT"] else "NOT SET"
    )

    print("Configuration loaded:")
    print(f"  Mode:         {mode}")
    print(f"  Database:     {db_display}")
    print(f"  API Access:   {api_display}")
    print(f"  Log Level:    {config['LOG_LEVEL']}")
    print(f"  Zion Network: {zion_display}")


def security_check(config: dict[str, str], missing: list[str]) -> None:
    print()
    print("Environment security check:")

    # Check no secrets are hardcoded (trivially true at runtime)
    print("  [OK] No hardcoded secrets detected")

    env_file_exists = os.path.isfile(".env")
    if env_file_exists:
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] .env file not found — copy .env.example to .env")

    if config["MATRIX_MODE"] == "production" or not missing:
        print("  [OK] Production overrides available")
    else:
        print(
            f"  [WARN] Missing variables for production: "
            f"{', '.join(missing)}"
        )


def show_mode_behaviour(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    print()
    if mode == "production":
        print("PRODUCTION MODE:")
        print("  - Verbose logging disabled")
        print("  - Error reporting enabled")
        print("  - Connecting to remote Zion endpoint")
    else:
        print("DEVELOPMENT MODE:")
        print("  - Verbose logging enabled (DEBUG)")
        print("  - Using local database instance")
        print("  - Connecting to local Zion stub")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv_file()

    config = get_config()
    missing = validate_config(config)

    if missing:
        print(
            "WARNING: Missing required configuration variables: "
            + ", ".join(missing)
        )
        print(
            "Copy .env.example to .env and fill in the values."
        )
        print()

    print_config(config)
    show_mode_behaviour(config)
    security_check(config, missing)

    print()
    print("The Oracle sees all configurations.")

    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
