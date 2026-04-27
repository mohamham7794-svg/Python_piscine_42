

import sys
import importlib


REQUIRED_PACKAGES = {
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
}


def check_dependencies() -> dict[str, str | None]:
    status: dict[str, str | None] = {}
    for display_name, import_name in REQUIRED_PACKAGES.items():
        try:
            mod = importlib.import_module(import_name)
            version = getattr(mod, "__version__", "unknown")
            status[display_name] = version
        except ImportError:
            status[display_name] = None
    return status


def print_dependency_status(status: dict[str, str | None]) -> bool:
    descriptions = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    all_ok = True
    print("Checking dependencies:")
    for pkg, version in status.items():
        if version is not None:
            print(f"  [OK] {pkg} ({version}) - {descriptions[pkg]}")
        else:
            print(f"  [MISSING] {pkg} - not installed")
            all_ok = False
    return all_ok


def show_install_instructions() -> None:
    print()
    print("To install dependencies:")
    print()
    print("  Using pip:")
    print("    pip install -r requirements.txt")
    print()
    print("  Using Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")


def compare_managers() -> None:
    print()
    print("Dependency manager comparison:")
    print("  pip:")
    print("    - Installs from requirements.txt")
    print("    - No lock file by default")
    print("    - Simple and widely available")
    print("  Poetry:")
    print("    - Uses pyproject.toml + poetry.lock")
    print("    - Deterministic installs via lock file")
    print("    - Manages virtual environments automatically")


def run_analysis() -> None:
    import numpy as np # type: ignore
    import pandas as pd # type: ignore
    import matplotlib # type: ignore
    matplotlib.use("Agg") # type: ignore
    import matplotlib.pyplot as plt # type: ignore

    print()
    print("Analyzing Matrix data...")
    n_points = 1000
    print(f"Processing {n_points} data points...")

    rng = np.random.default_rng(42)
    timestamps = np.arange(n_points)
    signal = rng.normal(loc=0.0, scale=1.0, size=n_points).cumsum()
    anomalies = rng.choice([0, 1], size=n_points, p=[0.97, 0.03])

    df = pd.DataFrame({
        "timestamp": timestamps,
        "signal": signal,
        "anomaly": anomalies.astype(bool),
    })

    normal = df[~df["anomaly"]]
    detected = df[df["anomaly"]]

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(
        normal["timestamp"],
        normal["signal"],
        color="green",
        linewidth=0.8,
        label="Normal signal",
    )
    ax.scatter(
        detected["timestamp"],
        detected["signal"],
        color="red",
        s=40,
        zorder=5,
        label=f"Anomalies ({len(detected)})",
    )
    ax.set_title("Matrix Signal Analysis")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Signal value")
    ax.legend()
    fig.tight_layout()

    output_file = "matrix_analysis.png"
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    status = check_dependencies()
    all_ok = print_dependency_status(status)

    compare_managers()

    if not all_ok:
        show_install_instructions()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
