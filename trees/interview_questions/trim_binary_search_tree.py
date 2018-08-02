#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Trim a Binary Search Tree

Given the root of a binary search tree and 2 numbers min and max, trim
the tree such that all the numbers in the new tree are between min and
max (inclusive). The resulting tree should still be a valid binary
search tree.
'''


def trim_binary_search_tree(tree, min, max):
    if not tree:
        return

    tree.left = trim_binary_search_tree(tree.left, min, max)
    tree.right = trim_binary_search_tree(tree.right, min, max)

    if min <= tree.val <= max:
        return tree

    if tree.val < min:
        return tree.right

    if tree.val > max:
        return tree.left
