#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Implement a Queue

The class should be able to do the following:
- Check if Queue is Empty
- Enqueue
- Dequeue
- Return the size of the Queue
'''


class Queue():
    def __init__(self):
        '''Initialize the queue object instance'''
        self.items = []

    def __len__(self):
        '''Returns the length of the queue'''
        return self.size()

    def size(self):
        '''Returns the number of items in the queue'''
        return len(self.items)

    def isEmpty(self):
        '''Tests to see whether the queue is empty'''
        return self.items == []

    def enqueue(self, item):
        '''Adds an item to the rear of the queue'''
        self.items.insert(0, item)

    def dequeue(self):
        '''Removes and returns the front item of the queue'''
        return self.items.pop()
