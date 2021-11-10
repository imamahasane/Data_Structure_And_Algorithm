# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 07:13:20 2019

@author: emama
"""

my_list = [120, 76, 1, 56, 43, 88, 3, 50]
print("Befor: \n", my_list)

for i in range(len(my_list)):
    mini_valu = i
    
    for j in range(i+1, len(my_list)):
        if my_list[j] < my_list[mini_valu]:
            mini_valu = j
    
    my_list[i], my_list[mini_valu] = my_list[mini_valu], my_list[i]

print("After: \n", my_list)

for re in range(len(my_list)):
    print("%d" %my_list[re])