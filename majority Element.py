# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:59:12 2017

@author: Amit
"""

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. (assume that the array is non-empty and the majority element always exist in the array.)
import math
def majority(a):
    n=len(a)
    hash_map={}
    for i in range(n):
        if a[i] in hash_map:
            hash_map[a[i]]+=1
        else:
            hash_map[a[i]]=1
    print(hash_map,n)
    for key in hash_map:
        if hash_map[key]==n//2:
            print(key,hash_map[key])
        else:
            continue
majority([1,1,1,1,1,1,11,1,2,3,4,5,2,4,9])
