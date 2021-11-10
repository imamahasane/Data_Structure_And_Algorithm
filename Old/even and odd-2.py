# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 05:05:06 2019

@author: emama
"""

n = 100
even = [False] * (n + 1)

for i in range(1, n + 1, 2):
    even[i] = True
    
print(even[8])