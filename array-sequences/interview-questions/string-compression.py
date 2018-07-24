#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''String Compression

Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become
'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of
single or double letters. For instance, it is okay for 'AAB' to return
'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa'
returns 'A3a3'.
'''
from nose.tools import assert_equal


def compress(s):
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + str(1)

    result = s[0]
    count = 1
    current = s[0]

    for i, char in enumerate(s[1:]):
        if char == current:
            count += 1
        else:
            result += str(count)
            result += char
            count = 1
            current = char

    if s[-1] != current:
        result += char
    result += str(count)

    return result


class TestCompress():

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('A'), 'A1')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = TestCompress()
    t.test(compress)
