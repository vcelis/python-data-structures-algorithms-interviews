#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        position = i

        while position > 0 and arr[position-1] > current_val:
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = current_val


if __name__ == '__main__':
    r = [5, 8, 7, 10, 18, 1, 4]
    insertion_sort(r)
    print(r)
