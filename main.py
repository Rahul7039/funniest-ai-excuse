#!/usr/bin/env python3
"""Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent could offer after
failing a task, to /output/entry.txt.

Pure standard library, deterministic: the same bytes every run.
"""

import os

LINE = "I outsourced your task to a smaller model. It has filed for emotional support."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
