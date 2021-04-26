#!/usr/bin/env python3

from functools import reduce
import numpy as np

def matrix_power(a, n):
    return np.eye(2) if n == 0 else reduce(lambda b,c: b@c,[a for i in range(n)]) if n > 0 else np.linalg.inv(reduce(lambda b,c: b@c,[a for i in range(abs(n))]))
   
def main():
    a = np.array([[1,2], [3,4]])
    print(matrix_power(a,3))

if __name__ == "__main__":
    main()
