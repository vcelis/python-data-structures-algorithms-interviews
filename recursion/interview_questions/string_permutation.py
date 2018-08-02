#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''String Permutation

Given a string, write a function that uses recursion to output a list of
all the possible permutations of that string.
'''
from nose.tools import assert_equal


def permute(s):
    output = []

    if len(s) <= 1:
        return s

    for i, letter in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            output += [letter + perm]

    return output


class TestPerm():
    def test(self, sol):
        assert_equal(sorted(sol('abc')), sorted(['abc', 'acb', 'bac', 'bca',
                                                 'cab', 'cba']))
        assert_equal(sorted(sol('dog')), sorted(['dog', 'dgo', 'odg', 'ogd',
                                                 'gdo', 'god']))
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestPerm()
    t.test(permute)
