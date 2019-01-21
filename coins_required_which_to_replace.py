#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" If you could remove one coin to our current set and replace it with another, which would you pick?
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
for coin_to_remove in coins:
    print "Remove ", coin_to_remove,
    seven_coins = sorted(list(set(coins) - {coin_to_remove}))
    coins_to_add = list(set(range(1, 500)) - set(seven_coins))
    min_amount = 9000
    desc = ""
    for combi in [list(set(seven_coins) | {coins_to_add[x]}) for x in range(len(coins_to_add))]:
        average = sum(get_min_coins(combi, up_to_amount)) / float(up_to_amount)
        if average == min_amount:
            desc += "\nAdd " + str(list(set(combi) - set(seven_coins))[0]) + " --> " + str(average)
        if average < min_amount:
            desc = "Add " + str(list(set(combi) - set(seven_coins))[0]) + " --> " + str(average)
            min_amount = average
    print desc
