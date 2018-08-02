#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Implement a Stack

The class should be able to do the following:
- Check if its empty
- Push a new item
- Pop an item
- Peek at the top item
- Return the size
'''


class Stack():
    def __init__(self):
        '''Initialize the stack object instance'''
        self.items = []

    def __len__(self):
        '''Returns the length of the stack'''
        return self.size()

    def size(self):
        '''Returns the number of items in the stack'''
        return len(self.items)

    def isEmpty(self):
        '''Tests to see whether the stack is empty'''
        return self.items == []

    def push(self, item):
        '''Adds an item to the top of the stack'''
        self.items.append(item)

    def pop(self):
        '''Removes and returns the top item of the stack'''
        return self.items.pop()

    def peek(self):
        '''Returns the top item of the stack'''
        return self.items[-1]
