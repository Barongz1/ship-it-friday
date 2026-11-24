"""Ship It Friday — entry for make.fun.

Writes one line to /output/entry.txt. The line is a funny git commit message an AI coding agent writes right before breaking production on a Friday.
"""
import os

LINE = "ship it friday: refactored everything, tested nothing, what could possibly go wrong"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
