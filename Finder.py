# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:36:53 2017

@author: Amit
"""
# Find an element which is present in one array but not in other

def finder(a,b,m,n):
    hash_map={}
    output=[]
    for i in range(n):
        if b[i] in hash_map:
            hash_map[b[i]]+=1
        else:
            hash_map[b[i]]=1
    for i in range(m):
        if a[i] in hash_map:
            continue
        else:
            output.append(a[i])
    return output
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6],7,6)
