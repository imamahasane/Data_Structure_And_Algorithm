# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 05:38:29 2019

@author: emama
"""

n = int(input())
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
print("N : ", n, "Count : ", count)