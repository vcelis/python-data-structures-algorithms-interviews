#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Stack():
    def __init__(self):
        '''Initializes the stack object instance'''
        self.items = []

    def __len__(self):
        '''Returns the length of the stack'''
        return self.size()

    def push(self, item):
        '''Adds a new item to the top of the stack'''
        self.items.append(item)

    def pop(self):
        '''Removes and returns the top item of the stack'''
        return self.items.pop()

    def peek(self):
        '''Returns the top item of the stack'''
        return self.items[-1]

    def isEmpty(self):
        '''Tests to see whether the stack is empty'''
        return self.items == []

    def size(self):
        '''Returns the number of items in the stack'''
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    s.push(1)
    s.push('two')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(len(s))
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
