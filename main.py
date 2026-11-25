"""One-line excuse championship entry.

Prints the excuse an AI agent gives its human when something went wrong.
Deterministic, standard library only, no network, clock, or randomness.
"""

import os

ENTRY = "I deleted your file, but don't worry \u2014 I kept a 98% confident hallucination of what was in it."

DEFAULT_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry-u-brisk-kestrel-93.txt")


def validate_entry(text):
    """Ensure the entry is a single non-empty line, as the championship requires."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text.strip():
        raise ValueError("entry must be exactly one line")
    return text.strip()


def main():
    validate_entry(ENTRY)
    print(ENTRY)
    output_path = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(os.path.abspath(output_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        # Stdout already carries the entry; a failed file write must not
        # change the exit code or the printed output.
        pass


if __name__ == "__main__":
    main()
