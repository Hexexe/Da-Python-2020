#!/usr/bin/env python3

import numpy as np

def diamond(n):
    d,b = np.eye(n,dtype=int)[:,1:],np.eye(n,dtype=int)
    dd = np.concatenate((np.flip(b,0),d),axis=0)
    ddd = np.flip(dd,0)[1:,:]
    return np.array(np.concatenate((dd,ddd)))

def main():
    for i in range(10): print(f"{diamond(i)}\n\n")

if __name__ == "__main__":
    main()
