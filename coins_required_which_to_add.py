#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" If you could only add one coin to our current set, which would you pick?
Calculates the average number of coins you would need to generate amounts up to £4.99.
"""

import itertools


def get_min_coins(coins, target_amount):
    n = len(coins)
    min_coins = [0] + [10000] * target_amount
    for i in range(n):
        for j in range(coins[i], target_amount + 1):
            min_coins[j] = min(min_coins[j - coins[i]] + 1, min_coins[j])
    return min_coins


up_to_amount = 499
coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins_to_add = list(set(range(1, 500)) - set(coins))


for combi in [list(set(coins) | {coins_to_add[x]}) for x in range(len(coins_to_add))]:
    print list(set(combi) - set(coins))[0], sum(get_min_coins(combi, up_to_amount)) / float(up_to_amount)
