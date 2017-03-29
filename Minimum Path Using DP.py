# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:24:20 2017

@author: Amit
"""
# Minimum path using dynamic programming
def minPath(m,n,a):
    R=len(a)
    C=len(a[0])
    tc=[[0 for x in range(C)]for x in range(R)]
    tc[0][0]=a[0][0]
    for i in range(1,R):
        tc[0][i]=a[0][i]+tc[0][0]
    for i in range(1,C):
        tc[i][0]=a[i][0]+tc[0][0]
    for i in range(1,m+1):
        for j in range(1,n+1):
            tc[i][j]=a[i][j]+min(tc[i-1][j],tc[i][j-1],tc[i-1][j-1])
    return tc[m][n]
minPath(2,2,[[1,2,3],[4,8,2],[1,5,3]])