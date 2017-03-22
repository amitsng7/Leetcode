# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:38:38 2017

@author: Amit
"""

#46) Count and Say
def countandsay(n):
    n=str(n)
    hash_map={}
    result=''
    for i in range(len(n)):
        key=n[i]
        if key in hash_map:
            hash_map[key]+=1
        else:
            hash_map[key]=1
    for i in range(len(n)) :
        key=n[i]
        result=result+str(hash_map[key])+key
    return int(result)
countandsay(21)