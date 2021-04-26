#!/usr/bin/env python3


def reverse_dictionary(d):
    res = {}
    for k,v in d.items():
        for i in v:            
            i = str(i)        
            if i not in res:   
                res[i] = [k]
            else:
                res[i].append(k)
    return res


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(d)
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
