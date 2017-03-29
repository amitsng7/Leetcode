# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:54:06 2017

@author: Amit
"""

#Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
def spiral(m,n,a):
    x=0
    y=0
    while(x<m and y<n):
        for i in range(x,n):
            print(a[x][i])
        x+=1
        for i in range(x,m):
            print(a[i][n-1])
        n-=1
        if(x<m):
            for i in reversed(range(n)):
                print(a[n-1][i])
            m-=1
        if(y<n):
            for i in reversed(range(m)):
                print(a[i+1][y])
            y+=1
spiral(4,5,[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])