# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:21:19 2017

@author: Amit
"""
#Maximum zero flip to create longest sequence of zero in a string

def maxzeroflip(a):
    set_to_remove=[]
    total=0
    final_total=0
    zero_index=[]
    for i in range(len(a)):
        if(a[i]==0):
            zero_index.append(i)
    for i in range(len(a)):
        if(i<len(zero_index)-1):
            if(i==0):
                total=(zero_index[i]-i)+(zero_index[i+1]-zero_index[i]-1)+(zero_index[i+2]-zero_index[i+1]-1)
            elif(i<=(len(zero_index)-3)):
                total=(zero_index[i]-zero_index[i-1]-1)+(zero_index[i+1]-zero_index[i]-1)+(zero_index[i+2]-zero_index[i+1]-1)
            else:
                total=(zero_index[i]-zero_index[i-1]-1)+(zero_index[i+1]-zero_index[i]-1)+(len(a)-zero_index[i+1]-1)
            if(total>final_total):
                set_to_remove=[]
                final_total=total
                set_to_remove.append([zero_index[i],zero_index[i+1]])
        else:
            break
    return(final_total,set_to_remove)

maxzeroflip([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0])