#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Queue():
    def __init__(self):
        '''Initializes the queue object instance'''
        self.items = []

    def __len__(self):
        '''Returns the length of the queue'''
        return self.size()

    def enqueue(self, item):
        '''Adds a new item to the rear of the queue'''
        self.items.insert(0, item)

    def dequeue(self):
        '''Removes and returns the front item of the queue'''
        return self.items.pop()

    def isEmpty(self):
        '''Tests to see whether the queue is empty'''
        return self.items == []

    def size(self):
        '''Returns the number of items in the queue'''
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    print(q.size())
    print(q.isEmpty())
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.size())
    print(q.isEmpty())
    print(q.dequeue())
    print(q.size())
    print(q.isEmpty())
