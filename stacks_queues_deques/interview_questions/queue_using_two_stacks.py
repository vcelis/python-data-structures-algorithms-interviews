#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Implement a Queue - Using Two Stacks

Implement a Queue class using two stacks.
Use a Python list data structure as your Stack.
'''


class Queue2Stacks():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())
