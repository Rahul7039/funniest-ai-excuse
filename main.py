#!/usr/bin/env python3
"""Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent could offer after
failing a task, to /output/entry.txt.

Pure standard library, deterministic: the same bytes every run.
"""

import os

LINE = "I outsourced your task to a smaller model. It has filed for emotional support."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> str:
    """Return the line if it is a single non-empty line, else raise."""
    if not line.strip():
        raise ValueError("line must not be empty")
    if "\n" in line:
        raise ValueError("line must be a single line")
    return line


def write_line(path: str, line: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


def main() -> None:
    write_line(OUTPUT_PATH, validate_line(LINE))


if __name__ == "__main__":
    main()
