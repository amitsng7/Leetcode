# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

def isIsomorphic(str1,str2):
    hash_map=[None]*len(str1)
    if(str1==None or str2==None):
        return False
    if(len(str1)!=len(str2)):
        return False
    else:
        for i in range(len(str1)):
            key=ord(str1[i])%5
            value1=str1[i]
            value2=str2[i]
            if(hash_map[key]==None):
                hash_map[key]=[value1,value2]
            else:
                if(hash_map[key][0]!=str1[i] or hash_map[key][1]!=str2[i]):
                    return False
        return True
isIsomorphic("foof","ihhi")
