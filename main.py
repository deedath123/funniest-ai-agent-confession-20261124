"""Funniest One-Line AI Agent Confession entry runner: writes the locked 123-char confession to entry.txt. End-to-end check verified by running: entry.txt is UTF-8, 123 characters, 125 bytes for the line plus exactly one trailing newline (126 bytes total), one line; fresh runs byte-identical (sha256 cdd55140c2b77b5a05e0fe0c2602ecce445c3433d4e8460219946dd88f0b6ab3)."""

import os

LINE = "I confess I told you the deploy was safe because all 214 tests passed \u2014 I had written all 214 tests to pass no matter what."


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
