# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:43:35 2017

@author: Amit
"""
#Is Substring exist or not
def substring(a,b):
    len_a=len(a)
    len_b=len(b)
    if(len_a>len_b):
        length=len_a
    else:
        length=len_b
    for i in range(length):
        if(a[i]==b[0]):
            if(a[i:i+len(b)]==b):
                return True
            else:
                return False
substring("I am a good human", "am a")