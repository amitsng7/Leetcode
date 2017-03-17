# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:45:18 2017

@author: Amit
"""

class Node(object):
    def __init__(self,d,n=None,p=None):
        self.data=d
        self.next_node=n
        self.prev_node=p
    def get_next(self):
        return self.next_node
    def get_prev(self):
        return self.prev_node
    def set_next(self,n):
        self.next_node = n
    def set_prev(self,p):
        self.prev_node = p
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data=d
class DoublyLinkedList(object):
    def __init__(self, r=None):
        self.root=r
        self.size=0
    def get_size(self):
        return self.size
    def add(self,d):
        new_node = Node(d, self.root)
        if(self.root):
            self.root.set_prev(new_node)
        self.root=new_node
        self.size=+1
    def remove(self, d):
        this_node=self.root
        while this_node:
            if this_node.get_data()==d:
                next=this_node.get_next()
                prev=this_node.get_prev()
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.root=this_node
                self.size-=1
                return True
            else:
                this_node=this_node.get_next()
        return False
    def find(self, d):
        this_node=self.root
        while this_node:
            if this_node.get_data()==d:
                return d
            else:
                this_node=this_node.get_next()
        return None
        
myList=DoublyLinkedList()
print(myList.add(12))
print(myList.add(3))
print(myList.add(5))
print(myList.add(15))
print(myList.get_size())