#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bin_search(arr, target):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


def rec_bin_search(arr, target):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        else:
            if target < arr[mid]:
                return rec_bin_search(arr[:mid], target)
            else:
                return rec_bin_search(arr[mid + 1:], target)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(bin_search(arr, 7))
    print(bin_search(arr, 11))

    print(rec_bin_search(arr, 7))
    print(rec_bin_search(arr, 11))
