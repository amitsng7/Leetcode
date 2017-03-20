# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

def rev_word(a):
    a=a.strip()
    input_string=[]
    b=''
    output_string=''
    for i in reversed(range(len(a))):
        if(a[i]!=' '):
            b=a[i]+b
        elif(a[i]==' '):
            input_string.append(b)
            b=''
    input_string.append(b)
    print(input_string)
    for i in range(len(input_string)):
        output_string=output_string+' '+input_string[i]
    output_string=output_string.strip()
    return output_string
rev_word("      My name is Amit    ")
