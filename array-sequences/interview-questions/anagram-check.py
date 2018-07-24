#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Anagram Check

Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same
letters.
'''
from nose.tools import assert_equal


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    dicty = {}
    for char in s1:
        dicty[char] = dicty[char] + 1 if char in dicty else 1
    for char in s2:
        dicty[char] = dicty[char] - 1 if char in dicty else 1

    for value in dicty.values():
        if value != 0:
            return False

    return True


class AnagramTest():

    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = AnagramTest()
    t.test(anagram)
    t.test(anagram2)
