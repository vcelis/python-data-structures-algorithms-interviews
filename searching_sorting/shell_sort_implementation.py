#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shell_sort(arr):
    sublistcount = len(arr) // 2

    while sublistcount > 0:
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)

        sublistcount = sublistcount // 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        current_val = arr[i]
        position = i

        while position >= gap and arr[position-gap] > current_val:
            arr[position] = arr[position-gap]
            position -= gap

        arr[position] = current_val


if __name__ == '__main__':
    r = [5, 8, 7, 10, 18, 1, 4]
    shell_sort(r)
    print(r)
