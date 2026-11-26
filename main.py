"""Funniest Cat Voicemail Greeting — make.fun program/v1 entry.

Writes one original voicemail greeting, recorded as if by a cat, to
/output/entry.txt (MAKEFUN_OUTPUT_DIR). One line, 1-120 characters.
Deterministic: no network, no clock, no randomness, no input read.
Only the output file is written.
"""

import os
from pathlib import Path

GREETING = (
    "You've reached Tuna. I can't talk — I'm coughing up a hairball "
    "on your favourite rug. Leave a message, I'll sit on it."
)


def validate_greeting(text: str) -> str:
    """Enforce the competition gate: one line, 1-120 chars, plain text."""
    text = text.strip()
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) >= 32 for c in text), "entry must hold no control characters"
    text.encode("utf-8")  # gate requires UTF-8 text
    return text


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    text = validate_greeting(GREETING)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    # Prove the file on disk is byte-identical to the validated greeting.
    assert target.read_text(encoding="utf-8") == text, "entry.txt mismatch"


if __name__ == "__main__":
    main()
