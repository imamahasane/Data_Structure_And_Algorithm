# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 04:53:42 2019

@author: emama
"""

n = int(input())

count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1
            
print("n = ", n, "count = ", count)