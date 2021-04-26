#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename) as f:
        ff = f.read()
    return len(ff.splitlines()), len(ff.split()), len(ff)

def main():
    for f in sys.argv[1:]:
        l,w,c = file_count(f)
        print(f"{l}\t{w}\t{c}\t{f}")

if __name__ == "__main__":
    main()
