#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Implement a Doubly Linked List

Implement a node class and show how it can be used to create a doubly
linked list.
'''


class DoublyLinkedListNode():

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None
