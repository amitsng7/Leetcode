# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:29:31 2017

@author: Amit
"""

#Insertion Sort
def insertionSort(n):
    input = n
    for i in range(1, len(input)):
        if input[i-1] > input[i]:
            a=input[i]
            input[i] = input[i-1]
            input[i-1] = a 
        for j in reversed(range(1, i)):
            if(input[j]<input[j-1]):
                b=input[j-1]
                input[j-1] = input[j]
                input[j] = b
    print(input)

insertionSort([14,33,27,10,5,35])
#or
def insertion(a):
    for j in range(1,len(a)):
        key=a[j]
        i=j-1
        while(i>=0 and a[i]>key):
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
    print(a)
insertion([5,4,3,2,1,6])