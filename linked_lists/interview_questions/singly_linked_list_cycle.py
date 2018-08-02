#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Singly Linked List Cycle Check

Given a singly linked list, write a function which takes in the first
node in a singly linked list and returns a boolean indicating if the
linked list contains a "cycle".
'''
from nose.tools import assert_equal


class Node():

    def __init__(self, value):
        self.value = value
        self.next_node = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next_node is not None:
        marker1 = marker1.next_node
        marker2 = marker2.next_node.next_node

        if marker2 == marker1:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)
a.next_node = b
b.next_node = c
c.next_node = a

x = Node(1)
y = Node(2)
z = Node(3)
x.next_node = y
y.next_node = z

h = Node(1)
i = Node(2)
j = Node(3)
h.next_node = i
i.next_node = j
j.next_node = i


class TestCycleCheck():

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)
        assert_equal(sol(h), True)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestCycleCheck()
    t.test(cycle_check)
