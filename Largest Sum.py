# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:09:48 2017

@author: Amit
"""
#Largest Sum Contiguous Subarray

def largest_sum(a):
    sum_=0
    current_sum=0
    for i in range(len(a)):
        current_sum=current_sum+a[i]
        sum_=max(sum_,current_sum)          
    return sum_
largest_sum([1,2,-1,3,4,10,10,-10,-1])