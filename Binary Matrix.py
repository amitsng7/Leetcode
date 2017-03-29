# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:57:20 2017

@author: Amit
"""

#Given a m * n matrix, if an element is 1, set its entire row and column to 1.
def modifyMatrix(m,n,a):
    row=[0]*m
    col=[0]*n
    for i in range(m):
        for j in range(n):
            if(a[i][j]==1):
                row[i]=1
                col[j]=1
    for i in range(m):
        for j in range(n):
            if(row[i] ==1 or col[j]==1):
                a[i][j]=1
    return a
modifyMatrix(3,3,[[0,0,0],[0,0,1],[0,0,0]])

#or
def modifyMatrixspacecomplex(m,n,a):
    row=False
    col=False
    for i in range(m):
        if(a[i][0]==1):
            col=True    
    for i in range(n):
        if(a[0][i]==1):
            row=True
    for i in range(1,m):
        for j in range(1,n):
            if(a[i][j]==1):
                a[i][0]=1
                a[0][j]=1
    for i in range(1,m):
        for j in range(1,n):
            if(a[i][0]==1 or a[0][j]==1):
                a[i][j]=1
    if(row):
        for i in range(m):
            a[i][0]=1
    if(col):
        for i in range(n):
            a[0][i]=1
    return a
modifyMatrixspacecomplex(3,3,[[0,0,0],[0,0,1],[0,0,0]])
