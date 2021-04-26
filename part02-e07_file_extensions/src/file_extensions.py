#!/usr/bin/env python3

def file_extensions(filename):
    l,d = [],{}
    with open(filename) as f:
        for i in f:
            d.setdefault(i.rstrip().split(".")[-1],[]).append(i.rstrip()) if "." in i else l.append(i.rstrip())
    return (l, d)

def main():
    l,d = file_extensions("src/filenames.txt")
    print(f"{len(l)} files with no extension")
    [print(f"{i} {len(d.get(i))}") for i in d]

if __name__ == "__main__":
    main()