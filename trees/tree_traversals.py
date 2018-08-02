#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nodes_references_tree_implementation import BinaryTree


def inorder(tree):
    '''
    1. Traverse the left subtree
    2. Visit the root
    3. Traverse the right subtree
    '''
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def preorder(tree):
    '''
    1. Visit the root
    2. Traverse the left subtree
    3. Traverse the right subtree
    '''
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    '''
    1. Traverse the left subtree
    2. Traverse the right subtree
    3. Visit the root
    '''
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


if __name__ == '__main__':
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

    print('Inorder:')
    inorder(tree)
    print('\nPreorder:')
    preorder(tree)
    print('\nPostorder:')
    postorder(tree)
