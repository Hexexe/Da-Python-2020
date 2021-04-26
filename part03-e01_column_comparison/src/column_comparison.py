#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    return a[a[:,1]>a[:,-2]]
    
def main():
    print(column_comparison(np.random.randint(10, size=(5, 5))))

if __name__ == "__main__":
    main()
