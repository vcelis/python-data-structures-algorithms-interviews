#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Balanced Parentheses Check

Given a string of opening and closing parentheses, check whether it’s
balanced. We have 3 types of parentheses: round brackets: (),
square brackets: [], and curly brackets: {}.

Assume that the string doesn’t contain any other character than these,
no spaces words or numbers.
'''
from nose.tools import assert_equal


def balance_check(s):
    if len(s) % 2 != 0:
        return False

    open_brackets = '({['
    parent_couples = [('(', ')'), ('[', ']'), ('{', '}')]
    parent_stack = []

    for char in s:
        if char in open_brackets:
            parent_stack.append(char)
        else:
            if len(parent_stack) == 0:
                return False
            if (parent_stack.pop(), char) not in parent_couples:
                return False
    return len(parent_stack) == 0


class TestBalanceCheck():

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol(''), True)
        assert_equal(sol('{}(('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestBalanceCheck()
    t.test(balance_check)
