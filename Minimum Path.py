# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:23:56 2017

@author: Amit
"""

def minimumPath(m,n,a):
    if(m<0 or n<0):
        return 999999999
    elif(m==0 and n==0):
        return a[m][n]
    else:
        return a[m][n]+min(minimumPath(m-1,n,a),minimumPath(m,n-1,a),minimumPath(m-1,n-1,a))
minimumPath(2,2,[[1,2,3],[4,8,2],[1,5,3]])