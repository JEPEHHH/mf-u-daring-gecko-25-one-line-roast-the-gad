"""Entrypoint for One-Line Roast: The Gadget You Use Every Day (program/v1)."""

from pathlib import Path
import sys

DEFAULT_OUTPUT = Path("/output/entry.txt")

ROAST_LINE = (
    'Slack marks me "Away" the second I actually read a doc, '
    "reducing my career to jiggling my mouse for proof of life."
)


def build_entry() -> str:
    text = ROAST_LINE.strip()
    if not text or len(text) > 200 or "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single non-empty line within 200 characters.")
    return text


def write_entry(output_path: Path = DEFAULT_OUTPUT) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(build_entry().encode("utf-8"))
    return output_path


def main(argv: list[str]) -> int:
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    write_entry(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
