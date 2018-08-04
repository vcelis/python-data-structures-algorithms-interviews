#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)


def quick_sort_helper(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        quick_sort_helper(arr, first, splitpoint - 1)
        quick_sort_helper(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivot = arr[first]

    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1

        while arr[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp

    tmp = arr[first]
    arr[first] = arr[right]
    arr[right] = tmp

    return right


if __name__ == '__main__':
    r = [5, 8, 7, 10, 18, 1, 4]
    quick_sort(r)
    print(r)
