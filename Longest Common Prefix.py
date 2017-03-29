# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:33:05 2017

@author: Amit
"""

# Longest Common Prefix 
def LCP(a):
    min_length=min(len(s) for s in a)
    final_string=''
    flag=0
    for i in range(min_length):
        current=a[0][i]
        for j in range(len(a)):
            if(a[j][i]==current):
                flag=1
            else:
                flag=0
                break
        if(flag==1):
            final_string=final_string+current
        elif(flag==0):
            break
    return final_string
LCP(["geeksforgeeks","geeks","geeke"])