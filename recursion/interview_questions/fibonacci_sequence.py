#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Fibonnaci Sequence

Implement a Fibonnaci Sequence in three different ways:
- Recursively
- Dynamically (Using Memoization to store results)
- Iteratively
'''
from nose.tools import assert_equal
from collections import defaultdict


def fib_rec(n):
    if n <= 1:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)


cache = defaultdict(int)


def fib_dyn(n):
    if n <= 1:
        return n
    if cache[n]:
        return cache[n]

    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


def fib_iter(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


class TestFib():
    def test(self, sol):
        assert_equal(sol(10), 55)
        assert_equal(sol(1), 1)
        assert_equal(sol(23), 28657)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestFib()
    t.test(fib_rec)
    t.test(fib_dyn)
    t.test(fib_iter)
