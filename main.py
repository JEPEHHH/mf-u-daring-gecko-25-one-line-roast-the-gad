from pathlib import Path
import sys

DEFAULT_OUTPUT = Path("/output/entry.txt")

# Initial milestone 1 draft candidate before pairwise tournament refinement.
ROAST_LINE = (
    "My Bluetooth earbuds burn their last 10% battery shouting \"BATTERY LOW\" "
    "every minute until the warning kills them itself."
)


def write_entry(output_path: Path = DEFAULT_OUTPUT) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ROAST_LINE, encoding="utf-8")
    return output_path


def main(argv: list[str]) -> int:
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    write_entry(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
