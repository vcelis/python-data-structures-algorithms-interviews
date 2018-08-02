#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Linked List Reversal

Write a function to reverse a Linked List in place. The function will
take in the head of the list as input and return the new head of the
list.
'''


class Node():

    def __init__(self, value):
        self.value = value
        self.next_node = None


def reverse(head):
    curr_node = head
    prev_node = None
    next_node = None

    while curr_node:
        next_node = curr_node.next_node

        curr_node.next_node = prev_node

        prev_node = curr_node
        curr_node = next_node

    return prev_node


if __name__ == '__main__':
    # Create a list of 4 nodes
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    # Set up order a,b,c,d with values 1,2,3,4
    a.next_node = b
    b.next_node = c
    c.next_node = d

    print(a.next_node.value)     # 2
    print(b.next_node.value)     # 3
    print(c.next_node.value)     # 4

    print(reverse(a).value)      # 4

    print(d.next_node.value)     # 3
    print(c.next_node.value)     # 2
    print(b.next_node.value)     # 1
