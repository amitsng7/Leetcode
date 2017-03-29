# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:00:26 2017

@author: Amit
"""
# Search an element in an array

def searchmatrix(m,n,a,target):
    i=0
    j=n-1
    while(i<n and j>=0):
        if(a[i][j]==target):
            print(i,j)
            return True
        if(a[i][j]>target):
            j-=1
        else:
            i+=1
    return False    
searchmatrix(3,3,[[10,20,30],[15,25,35],[27,29,37]], 16)