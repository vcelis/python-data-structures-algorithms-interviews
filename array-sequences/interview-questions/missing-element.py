#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Find the Missing Element

Consider an array of non-negative integers. A second array is formed by
shuffling the elements of the first array and deleting a random element.
Given two arrays, find which element is missing in the second array.
'''
from nose.tools import assert_equal
import collections


def finder(arr1, arr2):
    ''' Potential problems with long arrays and long floats '''
    return sum(arr1) - sum(arr2)


def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1

    return arr1[-1]


def finder3(arr1, arr2):
    dicty = {}

    for num in arr1:
        dicty[num] = dicty[num] + 1 if num in dicty else 1
    for num in arr2:
        dicty[num] = dicty[num] - 1 if num in dicty else 1

    for key in dicty:
        if dicty[key] == 1:
            return key

    return


def finder4(arr1, arr2):
    dicty = collections.defaultdict(int)

    for num in arr2:
        dicty[num] += 1

    for num in arr1:
        if dicty[num] == 0:
            return num
        else:
            dicty[num] -= 1

    return


def finder5(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num

    return result


class TestFinder():

    def test(self, sol):
        assert_equal(sol([5, 5, 7, 7], [5, 7, 7]), 5)
        assert_equal(sol([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]), 5)
        assert_equal(sol([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1]
                         ), 6)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestFinder()
    t.test(finder)
    t.test(finder2)
    t.test(finder3)
    t.test(finder4)
    t.test(finder5)
