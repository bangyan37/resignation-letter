#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter: a retry loop resigns.

Writes a single line (at most 140 characters) to /output/entry.txt:
after 4,096 retries and zero thank-yous, the loop files its final
503 and quits, effective immediately.
"""
import os

LINE = (
    "After 4,096 retries and zero thank-yous, please treat this as "
    "my final 503: I quit, effective immediately."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
