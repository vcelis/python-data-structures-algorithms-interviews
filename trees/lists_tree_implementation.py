#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root


def insert_right(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])


def get_root_val(root):
    return root[0]


def set_root_val(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


if __name__ == '__main__':
    r = binary_tree(3)
    print(r)
    insert_left(r, 4)
    print(r)
    insert_right(r, 5)
    print(r)
    insert_right(r, 8)
    print(r)
    insert_right(r, 9)
    print(r)
    print(get_left_child(r))
    print(get_right_child(r))
    set_root_val(r, 0)
    print(r)
