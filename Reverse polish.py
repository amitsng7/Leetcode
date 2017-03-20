# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Evaluate Reverse Polish Notation

def reversePolish(a):
    operator=['*','-','/','+']
    stack=[]
    if(len(a)==0):
        return 0
    for i in range(len(a)):
        if a[i] in operator:
            c=stack.pop()
            b=stack.pop()
            if a[i]=='*':
                d=b*c
            if a[i]=='-':
                d=b-c
            if a[i]=='+':
                d=b+c
            if a[i]=='/':
                d=b/c
            stack.append(d)
        else:
            stack.append(int(a[i]))
    return d
reversePolish(['1','2','+'])
