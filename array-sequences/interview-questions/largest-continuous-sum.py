#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Largest Continuous Sum

Given an array of integers (positive and negative) find the largest
continuous sum.
'''
from nose.tools import assert_equal


def large_cont_sum(arr):
    if len(arr) == 0:
        return

    current = arr[0]
    max_sum = arr[0]

    for num in arr[1:]:
        current = max(current + num, num)
        max_sum = max(current, max_sum)

    return max_sum


class LargeContTest():

    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = LargeContTest()
    t.test(large_cont_sum)
