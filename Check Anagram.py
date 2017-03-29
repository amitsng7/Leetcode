# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:46:45 2017

@author: Amit
"""
#Given two strings s and t, write a function to determine if t is an anagram of s.

def anagram_check(s1,s2):
    s1=s1.replace(" ","")
    s2=s2.replace(" ","")
    print(s1,s2)
    hash_map={}
    hash_map2={}
    for i in range(len(s1)):
        if s1[i] in hash_map:
            hash_map[s1[i]]+=1
        else:
            hash_map[s1[i]]=1
    
    for i in range(len(s2)):
        if s2[i] in hash_map2:
            hash_map2[s2[i]]+=1
        else:
            hash_map2[s2[i]]=1
    for i in range(len(s1)):
        if hash_map[s1[i]]==hash_map2[s1[i]]:
            continue
        else:
            return False
    return True
anagram_check("public relations", "crap built on lies")