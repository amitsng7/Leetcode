# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:02:21 2017

@author: Amit
"""
#Check if each internal node of a BST has exactly one child

def exactlyOneChild(a):
    flag=False
    for i in range(2,len(a)):
        if(a[i-1]<a[i]):
            continue
        elif(a[i-2]<a[i]<a[i-1]):
            continue
        else:
            flag=True
            break
    if(flag==False):
        print("Possible")
    else:
        print("Not Possible")
exactlyOneChild([8, 3, 5, 7, 6])