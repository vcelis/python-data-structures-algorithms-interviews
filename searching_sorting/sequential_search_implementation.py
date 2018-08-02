#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def seq_search(arr, target):
    pos = 0
    found = False

    while pos < len(arr) and not found:
        if arr[pos] == target:
            found = True
        else:
            pos += 1
    return pos if found else False


def ordered_seq_search(arr, target):
    pos = 0
    found = False
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == target:
            found = True
        else:
            if arr[pos] > target:
                stopped = True
            pos += 1

    return pos if found else False


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
    print(seq_search(arr, 4))
    print(seq_search(arr, 12))

    print(ordered_seq_search(arr, 3))
    print(ordered_seq_search(arr, 12))
