#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Implement a Deque

The class should be able to do the following:
- Check if its empty
- Add to both front and rear
- Remove from Front and Rear
- Check the Size
'''


class Deque():
    def __init__(self):
        '''Initialize the deque object instance'''
        self.items = []

    def __len__(self):
        '''Returns the length of the deque'''
        return self.size()

    def size(self):
        '''Returns the number of items in the deque'''
        return len(self.items)

    def isEmpty(self):
        '''Tests to see whether the deque is empty'''
        return self.items == []

    def addFront(self, item):
        '''Adds an item to the front of the deque'''
        self.items.append(item)

    def addRear(self, item):
        '''Adds an item to the rear of the deque'''
        self.items.insert(0, item)

    def removeFront(self):
        '''Removes and returns the front item of the deque'''
        return self.items.pop()

    def removeRear(self):
        '''Removes and returns the rear item of the deque'''
        return self.items.pop(0)
