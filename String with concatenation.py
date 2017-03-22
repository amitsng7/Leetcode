# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:29:24 2017

@author: Amit
"""

# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

def sub_concat(s,a):
    str_in=""
    start_index=[]
    n=len(a[0])
    m=len(s)
    flag=0
    i=0
    while(i<len(s)):
        x=i
        for j in range(len(a)):
            if s[x:x+n] in a:
                x=x+n
                flag=1
                continue
            else:
                flag=0
        if(flag==1):
            start_index.append(i)
            i=x
        else:
            i+=1
    return start_index
    
sub_concat("barbarbarfoobartheabcthebarfoo", ["foo", "bar","the"])