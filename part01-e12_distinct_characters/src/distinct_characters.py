#!/usr/bin/env python3


def distinct_characters(L):
    return {i: len(set(i)) for i in L}


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
