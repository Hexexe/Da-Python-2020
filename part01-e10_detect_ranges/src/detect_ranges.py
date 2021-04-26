#!/usr/bin/env python3


def detect_ranges(L):
    L2 = sorted(L)
    res = []
    r = ()
    prev = L2.pop(0)
    for x in L2:
        if x == prev + 1:
            r += (prev,)
            prev = x
        else:
            if r:
                r = (r[0], prev + 1)
                res.append(r)
            else:
                res.append(prev)
            r = ()
            prev = x
    if r:
        r = (r[0], prev + 1)
        res.append(r)
    else:
        res.append(prev)
    return res


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
