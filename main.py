#!/usr/bin/env python3
"""Write one funny one-line review of Monday to /output/entry.txt."""
import os

LINE = "Monday, one star: my 9 a.m. standup lasted 47 minutes, nobody stood up, and my inbox hit triple digits before I'd found coffee."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
