#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Binary Search Tree Check

Given a binary tree, check whether it’s a binary search tree or not.
'''
from nose.tools import assert_equal


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


def inorder(tree, result):
    if tree:
        inorder(tree.get_left_child(), result)
        result.append(tree.get_root_val())
        inorder(tree.get_right_child(), result)
    return result


def is_binary_tree(tree):
    result = inorder(tree, [])
    return result == sorted(result)


class TestIsBinaryTree():
    def test(self, sol):
        '''Setup Demo tree
                        1
                2               3
            4       5
        '''
        tree = BinaryTree('1')
        tree.insert_left('2')
        tree.insert_right('3')
        tree.get_left_child().insert_left('4')
        tree.get_left_child().insert_right('5')
        assert_equal(sol(tree), False)

        '''Setup Demo tree
                        4
                2               5
            1       3
        '''
        tree = BinaryTree('4')
        tree.insert_left('2')
        tree.insert_right('5')
        tree.get_left_child().insert_left('1')
        tree.get_left_child().insert_right('3')
        print(inorder(tree, []))
        assert_equal(sol(tree), True)

        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    test = TestIsBinaryTree()
    test.test(is_binary_tree)
