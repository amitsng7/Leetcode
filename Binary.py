# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:47:38 2017

@author: Amit
"""
# Binary representation of a number
def binary(a):
    b=[]
    while(a>1):
        b.append(a%2)
        a=a//2
    if (a==1):
        b.append(1)
    return b
binary(10)
