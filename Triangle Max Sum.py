# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:27:21 2017

@author: Amit
"""

#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

def triangle(a):
    sum1=0
    for i in reversed(range(len(a))):
        mini=10000
        for j in range(len(a[i])):
            if(mini>int(a[i][j])):
                mini=int(a[i][j])
            else:
                continue
        sum1=sum1+mini
    return sum1
arr=[[2],[3,4],[6,5,7],[4,1,8,3]]
triangle(arr)
