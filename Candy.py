# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:37:07 2017

@author: Amit
"""

#45) Candy [Google]
def candy(a):
    candy =1
    total_candy=1
    for i in range(1,len(a)):
        if(a[i-1]<a[i]):
            candy=candy+1
            total_candy=total_candy+candy
        else:
            candy=1
            total_candy=total_candy+candy
    return total_candy
candy([0,1,0,2,1,0,1,3,2,1,2,1])
