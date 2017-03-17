# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:29:31 2017

@author: Amit
"""

#bubble Sort 
def bubbleSort(n):
    input = n
    for i in range(0, len(input)):
        for j in range(1, len(input)):
            if input[j-1] > input[j]:
                a=input[j]
                input[j] = input[j-1]
                input[j-1] = a
    print(input)

bubbleSort([14,33,27,10,5,35])