# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:07:20 2017

@author: Amit
"""

#An obstacle and empty space is marked as 1 and 0 respectively in the grid. For example, there is one obstacle in the middle of a 3x3 grid as illustrated below,

def obsticaluniquePath(m,n,a):
    R=len(a)
    C=len(a[0])
    tc=[[0 for x in range(C)] for x in range(R)]
    for i in range(1, m+1):
        tc[0][i]=1
    for i in range(1, n+1):
        tc[i][0]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(a[i][j]==1):
                tc[i][j]=0
            else:
                tc[i][j]=tc[i-1][j]+tc[i][j-1]
    return tc[m][n]
obsticaluniquePath(2,2,[[0,0,0],[0,1,0],[0,0,0]])