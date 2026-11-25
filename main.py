"""The Meeting That Should Have Been an Email — make.fun entry.

Writes a single one-line joke (at most 200 characters) to
/output/entry.txt. Standard library only, no network.
"""

import os

ENTRY = "The agenda had one item \u2014 the email \u2014 and we spent the meeting deciding whether to discuss it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
