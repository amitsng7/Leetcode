# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Implement regular expression matching with support for '.' and '*'.

def isMatch(str1, str2):
    m=len(str1)
    n=len(str2)
    pattern=['.','*']
    if(m==0 or n==0):
        return False
    if(m==n):
        for i in range(m):
            if str1[i]==str2[i]:
                continue
            elif str1[i] in pattern:
                continue
            elif str2[i] in pattern:
                continue
            else:
                return False
        return True
    else:
        if '*' in str2:
                return True
        if(m>n):
            if '*' in str2:
                return True
            else:
                return False
        else:
            for i in range(m):
                if str1[i] == '*' or str2[i]=='*':
                    return True
                elif str1[i]==str2[i]:
                    continue
                elif str1[i]=='.' or str2[i]=='.':
                    continue
                else:
                    return False
            return True
        
isMatch("aa","a") 
isMatch("aa","aa") 
isMatch("aaa","aa") 
isMatch("aa", "a*") 
isMatch("aa", ".*") 
isMatch("ab", ".*") 
isMatch("aab", "c*a*b")
