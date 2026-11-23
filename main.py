"""Entry program for make.fun's "The One-Line Laugh" bounty.

Writes one funny line (a single sentence of at most 200 characters)
to /output/entry.txt. Standard library only; no network, no clock,
no files outside this repository.
"""

import os

LINE = (
    "My phone's screen time report arrives every Sunday like a tiny "
    "performance review from a manager I never hired, and I have never "
    "once passed it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
