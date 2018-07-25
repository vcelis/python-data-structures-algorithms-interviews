#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Reverse a String

Reverse a string using recursion.
'''
from nose.tools import assert_equal


def reverse(s):
    if len(s) <= 1:
        return s

    return s[-1] + reverse(s[:-1])


class TestReverse():
    def test(self, sol):
        assert_equal(sol('hello'), 'olleh')
        assert_equal(sol('hello world'), 'dlrow olleh')
        assert_equal(sol('123456789'), '987654321')
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    test = TestReverse()
    test.test(reverse)
