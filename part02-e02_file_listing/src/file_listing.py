#!/usr/bin/env python3

import re

#../src/listing.txt
def file_listing(filename="src/listing.txt"):
    with open(filename,"r") as f:
        l = []
        for i in f:
            x = re.search(r"[\d]{2,}[ \w:.-]{3,}",i).group()
            xy = re.sub(r"\s{2}"," ", x)
            l.append(tuple(int(n) if n.isdigit() else n for n in xy.replace(":"," ").split(" ")))
    return l

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
