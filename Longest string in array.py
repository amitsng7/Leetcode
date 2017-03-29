# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:54:26 2017

@author: Amit
"""

#Longest string in an array
def lengthStr(a):
    out_str=''
    m=len(a)
    for i in range((m-1),0,-1):
        if(a[i]== ' '):
            break
        else:
            out_str=a[i]+out_str

    return out_str
lengthStr("Krishan is an excellent Programmer")
