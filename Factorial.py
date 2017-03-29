# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:58:16 2017

@author: Amit
"""

#Factorial of a number
def fact(a):
    n=1
    if(a==1):
        return n
    if(a>1):
        n=a*fact(a-1)
        return n
fact(6)