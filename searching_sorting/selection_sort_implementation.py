#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def selection_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        max_pos = 0

        # Find highest number in array
        for k in range(1, n + 1):
            if arr[k] > arr[max_pos]:
                max_pos = k

        tmp = arr[n]
        arr[n] = arr[max_pos]
        arr[max_pos] = tmp


if __name__ == '__main__':
    r = [5, 8, 7, 10, 18, 1, 4]
    selection_sort(r)
    print(r)
