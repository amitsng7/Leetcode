# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:56:35 2017

@author: Amit
"""

#String substring computation
def string_comp(a):
    order=[]
    hash_map={}
    output_string=''
    for i in range(len(a)):
        if a[i] in hash_map:
            hash_map[a[i]]+=1
        else:
            order.append(a[i])
            hash_map[a[i]]=1
    for i in range(len(order)):
        output_string=output_string+order[i]+str(hash_map[order[i]])
    return output_string
string_comp("aaaaaaaaaAAAAAAAAbbbbbBBBBBBBBccccccddddddddd")
