#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Coin Change Problem

Given a target amount n and a list (array) of distinct coin values,
what's the fewest coins needed to make the change amount.
'''
from nose.tools import assert_equal
from collections import defaultdict


def rec_coin(target, coins):
    min_coins = target

    if target in coins:
        return 1

    for i in [c for c in coins if c <= target]:
        num_coins = 1 + rec_coin(target - i, coins)

        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins


def rec_coin_dynam(target, coins, known_results=defaultdict(int)):
    # Default min_coins output to target amount (using coin value 1)
    min_coins = target

    # Base case
    if target in coins:
        known_results[target] = 1
        return 1
    # Return a known result if it is greater than 1
    elif known_results[target] > 0:
        return known_results[target]

    # For every coin value that is smaller or equal than the target
    for i in [c for c in coins if c <= target]:
        num_coins = 1 + rec_coin_dynam(target - i, coins, known_results)

        # Update min_coins if we found a new minimum of coins
        if num_coins < min_coins:
            min_coins = num_coins

            # Also update the cache
            known_results[target] = min_coins

    return min_coins


class TestCoins():
    def test(self, sol):
        coins = [1, 5, 10, 25]
        assert_equal(sol(45, coins), 3)
        assert_equal(sol(23, coins), 5)
        assert_equal(sol(74, coins), 8)
        print('ALL TEST CASES PASSED')


if __name__ == '__main__':
    test = TestCoins()
    # test.test(rec_coin)         # Will take a long time!
    test.test(rec_coin_dynam)
