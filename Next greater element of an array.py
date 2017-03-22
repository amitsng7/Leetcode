# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:48:51 2017

@author: Amit
"""
# Next greater Element of an array element within an array
def nextgreaterelement(a):
    temp=[None]*len(a)
    for i in range(len(a)):
        prev_mini=max(a)
        for j in range(i+1, len(a)):
            if(a[i]<a[j]):
                mini=a[j]-a[i]
                if(mini<prev_mini):
                    mini=min(prev_mini,mini)
                    prev_mini=mini
                    temp[i]=a[j]
    return temp
nextgreaterelement([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28])
