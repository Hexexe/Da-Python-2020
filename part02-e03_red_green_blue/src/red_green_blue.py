#!/usr/bin/env python3

import re

# ../src/rgb.txt
def red_green_blue(filename="src/rgb.txt"):
    l = []
    with open(filename) as f:
        for i in f:
            x = re.search(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s*?(\w+\s?\D+)", i)
            l.append(f"{x.group(1)}\t{x.group(2)}\t{x.group(3)}\t{x.group(4).strip()}") if x != None else print("lol")
    return l


def main():
    for i in red_green_blue():
        print(i)


if __name__ == "__main__":
    main()
