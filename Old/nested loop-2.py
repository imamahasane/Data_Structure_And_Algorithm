# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 06:02:37 2019

@author: emama
"""

n = int(input())
count = 0
for i in range(n):
    count += 1
    
for i in range(n):
    for j in range(n):
        count += 1
print(count)