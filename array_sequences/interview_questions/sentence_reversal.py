#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Sentence Reversal

Given a string of words, reverse all the words.
'''
from nose.tools import assert_equal


def rev_word(s):
    words = []
    length = len(s)
    spaces = [' ']
    i = 0

    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start:i])
        i += 1

    result = ''
    for i in range(len(words)-1, -1, -1):
        result += words[i]
        if i != 0:
            result += ' '

    return result


def rev_word2(s):
    return ' '.join(s.split()[::-1])


class ReversalTest():

    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '),
                     'you are how John Hello')
        assert_equal(sol('1'), '1')
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    t = ReversalTest()
    t.test(rev_word)
    t.test(rev_word2)
