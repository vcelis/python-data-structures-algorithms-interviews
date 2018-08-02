#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTree():

    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        tmp = BinaryTree(new_node)
        tmp.left_child = self.left_child
        self.left_child = tmp

    def insert_right(self, new_node):
        tmp = BinaryTree(new_node)
        tmp.right_child = self.right_child
        self.right_child = tmp

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_root_val(self):
        return self.key


if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.get_root_val())
    print(r.get_left_child())
    r.insert_left('b')
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right('c')
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.insert_right('d')
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    print(r.get_right_child().get_right_child().get_root_val())
    r.get_right_child().set_root_val('hello')
    print(r.get_right_child().get_root_val())
