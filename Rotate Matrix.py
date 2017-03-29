# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:03:22 2017

@author: Amit
"""
#You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

def rotatemat(m,n,a):
    temp=0
    for i in range(m//2):
        for j in range(i,n-i-1):
            temp=a[i][j]
            a[i][j]=a[j][n-1-i]
            a[j][n-1-i]=a[n-1-i][n-1-j]
            a[n-1-i][n-1-j]=a[n-1-j][i]
            a[n-1-j][i]=temp
    print(a)
rotatemat(4,4,[[10,20,30,40],[15,25,35,45],[27,29,37,39],[1,2,3,4]])
