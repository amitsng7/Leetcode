# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:34:06 2017

@author: Amit
"""
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

def zigzag(str1, n):
    m=len(str1)
    count=0
    a=[[0 for i in range(m-n)]for i in range(n)]
    print(a)
    for i in range(m):
        for j in range(n):
            if(count!=(m)):
                a[j][i]=str1[count]
                count+=1
            else:
                break
    d=traverse(a)
    return d
def traverse(a):
    out_str=''
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j]!=0):
              out_str=out_str+a[i][j]
            else:
                continue
    return out_str
print(zigzag("abcdefgh",3))