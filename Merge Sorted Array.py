# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:17:14 2017

@author: Amit
"""
#Merge Two sorted Array 

def merge(a,b,m,n):
    out=[]
    while(m>0 or n>0):
        if((n-1)==0 and m==0):
            out.append(b[n])
            b.pop()
            n-=1
        elif(n==0 and (m-1)==0):
            out.append(a[m-1])
            a.pop()
            m-=1
        elif(a[m-1]>b[n-1]):
            out.append(a[m-1])
            a.pop()
            m-=1
        elif(b[n-1]>a[m-1]):
            out.append(b[n-1])
            b.pop()
            n-=1       
    return out
merge([1,5,9,20],[2,4,6,8,10,22,33],4,7)