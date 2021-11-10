# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 05:22:46 2019

@author: emama
"""

n = input()
n = int(n)
count = 0

for i in range(n):
    for j in range(n):
        count += 1
print("N = ", n, "Count = ", count)