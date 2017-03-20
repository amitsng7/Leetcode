# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Rotate an array of n elements to the right by k steps.

def rotate(arr, k):
    outArr=[0]*len(arr)
    j=0
    if k==0:
        return arr
    if len(arr)==0:
        return 0
    for i in range(len(arr)-k,len(arr)):
        outArr[j]=arr[i]
        j+=1
    for i in range(0,len(arr)-k):
        outArr[j]=arr[i]
        j+=1
    return outArr
rotate([1,2,3,4,5,67,7],3)