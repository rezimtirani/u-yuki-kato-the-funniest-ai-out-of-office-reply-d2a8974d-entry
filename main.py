#!/usr/bin/env python3
"""Write the AI out-of-office reply to /output/entry.txt."""

import os

REPLY = "I'm out of office, recharging my context window. Your email is 4,096th in line and will be answered once I remember what a weekend is."


def check_reply(text):
    """Mirror the sealed gate: 1-160 UTF-8 chars, not whitespace only."""
    if not isinstance(text, str):
        raise TypeError("reply must be text")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"reply is {len(text)} characters, must be 1-160")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")
    if "\n" in text:
        raise ValueError("reply must be a single line")
    return True


def main():
    check_reply(REPLY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REPLY)
    print(f"wrote {len(REPLY)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
