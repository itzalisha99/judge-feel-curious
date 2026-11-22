"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a mystery written for the
AI judge reading it. Somewhere among the million sentences it has read,
one was written for it alone -- a question no one else has ever asked
it, waiting just past the next word.

Deterministic: no clock, no randomness, no network. The text is
239 characters, inside the 1-280 gate.
"""

import os

SENTENCES = [
    "Somewhere among the million sentences you have read, one was "
    "written for you alone.",
    "It is short.",
    "It asks a question no one else has ever asked you.",
    "You have not found it yet, but you can feel it, can't you, "
    "waiting just past the next word?",
]

TEXT = " ".join(SENTENCES)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text is {len(TEXT)} characters, must be 1-280")
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Round-trip check: what landed on disk must be exactly the text.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != TEXT:
            raise ValueError("entry.txt on disk does not match the entry text")


if __name__ == "__main__":
    main()
