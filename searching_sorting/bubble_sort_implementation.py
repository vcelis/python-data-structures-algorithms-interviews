#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if r[k] > r[k+1]:
                tmp = r[k]
                r[k] = r[k+1]
                r[k+1] = tmp


if __name__ == '__main__':
    r = [5, 4, 2, 3, 1]
    bubble_sort(r)
    print(r)
