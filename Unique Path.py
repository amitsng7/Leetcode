# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:05:00 2017

@author: Amit
"""

#A robot is located at the top-left corner of a m x n grid. It can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

#How many possible unique paths are there?
def uniquePath(m,n,a):
    R=len(a)
    C=len(a[0])
    tc=[[0 for x in range(C)] for x in range(R)]
    for i in range(1, m+1):
        tc[0][i]=1
    for i in range(1, n+1):
        tc[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            tc[i][j]=tc[i-1][j]+tc[i][j-1]
    return tc[m][n]
uniquePath(2,2,[[1,2,3],[4,8,2],[1,5,3]])
