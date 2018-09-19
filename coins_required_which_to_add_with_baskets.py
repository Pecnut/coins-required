#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import itertools

def get_min_coins(coins, target_amount):
    n = len(coins)
    min_coins = [0] + [10000] * target_amount
    for i in range(n):
        for j in range(coins[i], target_amount + 1):
            min_coins[j] = min(min_coins[j - coins[i]] + 1, min_coins[j])
    return min_coins

# BASKETS ------------------------------------------------
basket_sizes = []
basket_prices = []
with open("ons_data/baskets2.txt", "r") as f:
    for line in f:
      line_split =  line.split(',')
      basket_sizes.append(int(line_split[0]))
      basket_prices.append(int(line_split[1]))

prices_less_than = 2000
basket_prices_we_want = [basket_prices[i] for i in xrange(len(basket_prices)) if basket_prices[i] < prices_less_than]
lowest_banknote = 500
lowest_coin = 1
ends_in = range(0,lowest_banknote,lowest_coin)
prices_mod_lowest_banknote = [i%lowest_banknote for i in basket_prices_we_want]
prices_end_in_count = [ sum(1 for i in prices_mod_lowest_banknote if i==j) for j in ends_in]
prices_end_in_count_as_percent = [i/sum(prices_end_in_count)*100 for i in prices_end_in_count]
weightings_for_each_amount = prices_end_in_count_as_percent
weightings_symmetric = [weightings_for_each_amount[0]] + [(weightings_for_each_amount[i] + weightings_for_each_amount[len(weightings_for_each_amount)-i])/2 for i in range(1,len(weightings_for_each_amount))]
mean_weighting = (sum(weightings_symmetric)/len(weightings_symmetric))
# END BASKETS ---------------------------------------------


# Normal coins --------------
up_to_amount = 499
coins = [1,2,5,10,20,50,100,200]
coins_to_add = list(set(range(1,500)) - set(coins))

for combi in [list(set(coins) | {coins_to_add[x]}) for x in range(len(coins_to_add))]:
    gmc = get_min_coins(combi,up_to_amount)
    print list(set(combi)-set(coins))[0], round(sum([gmc[i]*weightings_symmetric[i] for i in range(up_to_amount)])/float(up_to_amount)/mean_weighting,5)


# No 1 or 2 ----------------------
'''
up_to_amount = 499//5
coins = [5//5,10//5,20//5,50//5,100//5,200//5]
weights = [3.25,6.5,5,8,9.5,12]
weightings_for_each_amount = prices_end_in_count_as_percent
weightings_for_each_amount = [0 for i in range(100)]
weightings_for_each_amount[0] = (sum(prices_end_in_count_as_percent[0:3]) + sum(prices_end_in_count_as_percent[498:500]) )/5
coins_to_add = list(set(range(1,100)) - set(coins))

for i in range(1,100):
    weightings_for_each_amount[i] = sum(prices_end_in_count_as_percent[5*i-2:5*i+3])/5


for combi in [list(set(coins) | {coins_to_add[x]}) for x in range(len(coins_to_add))]:
    gmc = get_min_coins(combi,up_to_amount)
    print list(set(combi)-set(coins))[0], round(sum([gmc[i]*weightings_symmetric[i] for i in range(up_to_amount)])/float(up_to_amount)/mean_weighting,5)
'''
