#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Tree Level Order Print

Given a binary tree of integers, print it in level order. The output
will contain space between the numbers in the same level, and new line
between different levels.
'''


class Node():

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def level_order_print(tree):
    if not tree:
        return

    nodes = [tree]
    current_count = 1
    next_count = 0

    while len(nodes) != 0:
        current_node = nodes.pop(0)
        print(current_node.val, end=' ')
        current_count -= 1

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1
        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1

        # If the row is finished
        if current_count == 0:
            print('\n')
            current_count = next_count
            next_count = 0


if __name__ == '__main__':
    '''Setup Demo tree
                    1
            2               3
        4               5       6
    '''
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.right.left = Node(5)
    tree.right.right = Node(6)

    level_order_print(tree)
