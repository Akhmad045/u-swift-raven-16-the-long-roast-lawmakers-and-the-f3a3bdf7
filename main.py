#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (160 characters, a single sentence) to
/output/entry.txt.

The roast sets up the lawmaker's authority — a morning spent grilling AI
executives about alignment — and undercuts it with the file he cannot
convert: he thinks renaming his bill turns it into a PDF. The punch lands
on the last words, and the detail (renaming a file to convert it) is a
specific, fresh tech-illiteracy beat rather than a worn cliche.
"""

import os

ROAST = (
    "The lawmaker who spent the morning grilling AI executives about "
    "alignment spent the afternoon asking IT why renaming his bill still "
    "hasn't turned it into a PDF."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 320, f"entry is {len(text)} chars, must be 1-320"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Verify the written bytes round-trip exactly: a half-written or
    # re-encoded file would silently change the judged line.
    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written.decode("utf-8") != text or len(written) != len(text.encode("utf-8")):
        raise RuntimeError("entry.txt does not round-trip exactly")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
