"""Ship It Friday — one-line git commit message.

Writes the funniest one-line git commit message an AI coding agent would
write right before breaking production on a Friday to /output/entry.txt.
"""

import os

LINE = (
    "feat: Friday 4:59pm deploy to prod, tests skipped "
    "\u2014 confidence is my test suite"
)


def validate(line):
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > 159:
        raise ValueError("line is %d characters, over the 159 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if ":" not in line.split(" ", 1)[0]:
        raise ValueError("line must read as a commit message (type: subject)")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
