#!/usr/bin/env python3

from collections import Counter

def word_frequencies(filename):
    with open(filename) as f:     
        return dict(Counter([i.strip("""!"#$%&'()*,-./:;?@[]_""") for i in f.read().split()]))


def main():
    d = word_frequencies("../src/alice.txt")
    for x in list(d)[0:20]:
        print (f"{x}\t\t{d[x]}")


if __name__ == "__main__":
    main()
