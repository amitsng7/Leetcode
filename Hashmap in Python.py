    # -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:53:30 2017

@author: Amit
"""

class HashMap:
    def __init__(self):
        self.size=6
        self.map=[None]*self.size
    def get_hash(self,key):
        key_hash=key%5
        if(self.map[key_hash] is not None):
            for pair in self.map[key_hash]:
                if(int(pair[0])==key):
                    return pair[1]
    def add_hash(self,key,value):
        key_hash=key%5
        key_value=[key,value]
        if(self.map[key_hash]==None):
            self.map[key_hash]=list([key_value])
        else:
            self.map[key_hash].append([key_value])
            return True
        
myhash=HashMap()
myhash.add_hash(5,6)
myhash.add_hash(5,7)
myhash.get_hash(5)