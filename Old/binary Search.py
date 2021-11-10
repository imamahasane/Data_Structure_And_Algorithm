# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:28:06 2019

@author: emama
"""

myList = [1, 5, 8, 12, 35, 45, 98, 99,121]
search = int(input())

left = 0
right = len(myList) -1
mid = 0

while left <= right:
    mid = int((left + right) / 2)

    if myList[mid] == search:
        print("Asa vai : ", mid)
        break
    
    elif myList[mid] < search:
        left = mid + 1
        
    else:
        right = mid - 1
        
