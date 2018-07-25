#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node():

    def __init__(self, value):
        self.value = value
        self.next_node = None


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next_node = b
    b.next_node = c

    print(a.value)
    print(a.next_node.value)
    print(a.next_node.next_node.value)
