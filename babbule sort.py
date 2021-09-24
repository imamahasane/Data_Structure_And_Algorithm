# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:03:53 2019

@author: emama
"""

def babbuleSort(m):
    n = len(m)
    
    for i in range(0, n):
        for j in range(0, n-i-1):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]

if __name__ == "__main__":
    myList = [86, 1, 65, 41, 20, 11, 32, 50, 70]
    print("Beafor sorting: ", myList)
    
    babbuleSort(myList)
    print("After sorting: ", myList)
    