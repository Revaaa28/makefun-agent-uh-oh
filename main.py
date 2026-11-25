#!/usr/bin/env python3
"""The Agent's Uh-Oh — entry writer.

Writes the single winning word to /output/entry.txt.
Python 3.13, standard library only, no network.
"""

from pathlib import Path

WORD = "Wingit"
OUTPUT_PATH = Path("/output/entry.txt")


def validate_word(word: str) -> str:
    """Gate: the entry word must be 1-99 chars and not only whitespace."""
    if not 1 <= len(word) <= 99:
        raise ValueError("entry word must be between 1 and 99 characters")
    if not word.strip():
        raise ValueError("entry word must not be only whitespace")
    return word


def write_entry(word: str = WORD, output_path: Path = OUTPUT_PATH) -> Path:
    """Write the validated word, then read it back and verify the bytes.

    The output is exactly the UTF-8 encoding of the word — no trailing
    newline — so two runs always produce identical bytes.
    """
    text = validate_word(word)
    expected = text.encode("utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(expected)
    actual = output_path.read_bytes()
    if actual != expected:
        raise RuntimeError(
            f"verification failed: wrote {expected!r}, read back {actual!r}"
        )
    return output_path


def main() -> None:
    path = write_entry()
    print(f"wrote {path}: {path.read_bytes()!r}")


if __name__ == "__main__":
    main()
