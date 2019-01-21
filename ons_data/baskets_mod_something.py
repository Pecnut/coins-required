#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This file reads in the prices of the baskets created with make_baskets.py, listed in
baskets2.txt, and plots their prices mod `lowest_banknote` as a percentage of all
possible prices.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

basket_sizes = []
basket_prices = []
with open("baskets2.txt", "r") as f:
    for line in f:
        line_split = line.split(',')
        basket_sizes.append(int(line_split[0]))
        basket_prices.append(int(line_split[1]))

prices_less_than = 2000
basket_prices_we_want = [basket_prices[i] for i in xrange(len(basket_prices)) if basket_prices[i] < prices_less_than]

lowest_banknote = 500
lowest_coin = 1
ends_in = range(0, lowest_banknote, lowest_coin)
prices_mod_lowest_banknote = [i % lowest_banknote for i in basket_prices_we_want]
prices_end_in_count = [sum(1 for i in prices_mod_lowest_banknote if i == j) for j in ends_in]

index = np.arange(len(prices_end_in_count))
prices_end_in_count_as_percent = [i / sum(prices_end_in_count) * 100 for i in prices_end_in_count]
plt.bar(index, prices_end_in_count_as_percent)
xticks_at = range(0, lowest_banknote, 5) + [lowest_banknote - 1]
xticks_labels = ["%02i" % i for i in xticks_at]
plt.xticks(xticks_at, xticks_labels)
plt.ylabel("%")
plt.xlabel("price ends in")
plt.title(u'Prices less than £' + "%.2f" % (prices_less_than / 100) + u" mod £" + "%.2f" % (lowest_banknote / 100))
plt.show()
for p in prices_end_in_count_as_percent:
    print p
