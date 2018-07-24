#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Deque():
    def __init__(self):
        '''Initializes the deque object instance'''
        self.items = []

    def __len__(self):
        '''Returns the length of the deque'''
        return self.size()

    def addFront(self, item):
        '''Adds a new item to the front of the deque'''
        self.items.append(item)

    def addRear(self, item):
        '''Adds a new item to the rear of the deque'''
        self.items.insert(0, item)

    def removeFront(self):
        '''Removes and returns the front item of the deque'''
        return self.items.pop()

    def removeRear(self):
        '''Removes and returns the rear item of the deque'''
        return self.items.pop(0)

    def isEmpty(self):
        '''Tests to see whether the deque is empty'''
        return self.items == []

    def size(self):
        '''Returns the number of items in the deque'''
        return len(self.items)


if __name__ == '__main__':
    d = Deque()
    d.addFront('hello')
    d.addRear('world')
    print(d.size())
    print(d.isEmpty())
    print(d.removeFront() + ' ' + d.removeRear())
    print(len(d))
    print(d.isEmpty())
