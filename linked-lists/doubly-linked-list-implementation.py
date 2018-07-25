#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DoublyLinkedListNode():

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


if __name__ == '__main__':
    a = DoublyLinkedListNode(1)
    b = DoublyLinkedListNode(2)
    c = DoublyLinkedListNode(3)
    a.next_node = b
    b.prev_node = a
    b.next_node = c
    c.prev_node = b

    print(a.value)
    print(a.next_node.value)
    print(b.next_node.value)
    print(c.prev_node.value)
    print(b.prev_node.value)
