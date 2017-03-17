# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:29:31 2017

@author: Amit
"""

#selection Sort
def selectionSort(n):
    input=n
    for i in range(0, len(input)):
        for j in range(i, len(input)):
            if(input[i]>input[j]):
                b=input[j]
                input[j]=input[i]
                input[i]=b
    print(input)
selectionSort([14,33,27,10,5,35])