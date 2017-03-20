# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:16:43 2017

@author: Amit
"""

#Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that only one letter can be changed at a time and each intermediate word must exist in the dictionary

def outputBuilder(str1,str2):
    count=0
    if(len(str1)!=len(str2)):
        return False
    else:
        for i in range(len(str1)):
            if(str1[i]!=str2[i]):
                count+=1
            if(count>1):
                return False
        return True
                

def word(inpt,start,end):
    outpt=[]
    for i in range(len(inpt)):
        if(len(outpt)==0):
            d=outputBuilder(inpt[i],start)
            if(d==True):
                outpt.append(start)
                outpt.append(inpt[i])
        else:
            d=outputBuilder(inpt[i],end)
            if(d==True):
                outpt.append(inpt[i])
            elif(d==False):
                outpt.append(end)
                return outpt
    outpt.append(end)
    return outpt
word(["hot","dog","bog","lot","log"],"hit","cog")