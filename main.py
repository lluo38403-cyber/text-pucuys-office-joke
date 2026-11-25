"""One-Line Office Joke — make.fun entry.

Writes a single-line joke about office life to /output/entry.txt.
The joke is about the office printer, which only ever jams when the
whole meeting is already waiting for the one document you are printing.
It is one sentence, one line, no setup beyond the printer itself.
"""

import os

ENTRY = (
    "The office printer only jams when you're printing the one "
    "document the whole meeting is already waiting for."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
