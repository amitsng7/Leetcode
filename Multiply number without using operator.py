# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:38:11 2017

@author: Amit
"""

def multiple(x,y):
    if (y==0):
        return 0
    if(y>0):
        return (x + (multiple(x,y-1)))
print(multiple(2,3))