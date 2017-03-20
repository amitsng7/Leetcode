# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Given a collection of intervals, merge all overlapping intervals.

def mergeInterval(a):
    m=len(a)
    output=[]
    for i in range(0,m):
        if(i>=1):
            curr_start=a[i][0]
            curr_end=a[i][1]
            prev_element=output[-1]
            prev_start=prev_element[0]
            prev_end=prev_element[1]
            if(prev_end>curr_start):
                output.pop()
                new_patch=[prev_start,curr_end]
                output.append(new_patch)
            else:
                output.append(a[i])
        else:
            output.append(a[i])
    return output
mergeInterval([[1,3],[2,6],[8,10],[9,18]])