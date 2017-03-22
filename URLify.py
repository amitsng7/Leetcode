# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:45:17 2017

@author: Amit
"""

#URLify and given string in place of space            
def URLify(word):
    a="%20"
    str=""
    for i in range(len(word)):
        if(word[i]==" "):
            str=str+a
        else:
            str=str+word[i]
    return str
print(URLify("A mi t      "))