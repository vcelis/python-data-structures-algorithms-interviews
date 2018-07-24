#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nose.tools import assert_equal


def uni_char(s):
    if len(s) <= 1:
        return True

    chars = set()
    for char in s:
        if char in chars:
            return False
        chars.add(char)
    return True


def uni_char2(s):
    return len(s) == len(set(s))


class TestUnique():

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestUnique()
    t.test(uni_char)
    t.test(uni_char2)
