#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This file reads in the prices of individual items from shops all over the country.
Then it reads it the data of how much of consumer income is spent on each item type.
It then creates shopping baskets based on this data, weighted according to how often an
item type is bought. The price of each item in the basket is itself weighted on how 
common that price is.
"""

from __future__ import division
import csv
import random


def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"


data = []
item_ids = []
item_descs = []
validities = []
shop_codes = []
all_prices = []
regions = []
shop_weights = []
print "Reading in data files..."
with open('price_quote_201807.csv', 'rb') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        if row[0] == 'QUOTE_DATE':
            continue
        item_ids.append(int(row[1]))
        item_descs.append(row[2])
        validities.append(int(row[3]))
        shop_codes.append(int(row[4]))
        all_prices.append(int(float(row[5]) * 100))  # Read prices in as pennies, for easier arithmetic
        regions.append(int(row[14]))
        shop_weights.append(int(row[16]))

indices_item_ids = []
indices_cpi_weight = []
with open('item_indices_201807.csv', 'rb') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        if row[0] == 'INDEX_DATE':
            continue
        indices_item_ids.append(int(row[1]))
        indices_cpi_weight.append(float(row[10]))

# Convert CPI Weight to number weight
# CPI weight is proportion of income spent on this thing (*1000) but I want how common it is to buy itself.
# So number weight = CPI weight / avg price of item. So I need to work out average price of item first.
# This is worked out by taking the mean of all prices, weighting on the shop weight.
print "Converting CPI weight to number weight..."
prices = all_prices
indices_number_weight = [0 for i in range(len(indices_item_ids))]
item_ids_unique = list(set(item_ids))
weighted_mean_prices = [0 for i in range(len(indices_item_ids))]
for item_id in item_ids_unique:
    id = indices_item_ids.index(item_id)
    prices_for_that_item = [prices[i] for i in xrange(len(prices)) if item_ids[i] == item_id]
    shop_weights_for_that_item = [shop_weights[i] for i in xrange(len(prices)) if item_ids[i] == item_id]
    if len(shop_weights_for_that_item) == 0:
        indices_number_weight[id] = 0
    else:
        weighted_mean_price = sum(x * y for x, y in zip(prices_for_that_item, shop_weights_for_that_item)) / sum(shop_weights_for_that_item)
        weighted_mean_prices[id] = weighted_mean_price
        indices_number_weight[id] = indices_cpi_weight[id] / weighted_mean_price


# NOTE: Prices have been read in in PENNIES!
prices = all_prices

# Remove invalid results
print "Removing invalid rows from the data..."
criteria = [i for i in xrange(len(prices)) if validities[i] == 3 or validities[i] == 4]
item_ids = [item_ids[i] for i in criteria]
prices = [prices[i] for i in criteria]
shop_weights = [shop_weights[i] for i in criteria]
item_descs = [item_descs[i] for i in criteria]

# Anything between 0 and 100 quid
prices_less_than = 10000
print "Selecting items less than " + "%.2f" % (prices_less_than / 100) + " pounds..."
criteria = [i for i in xrange(len(prices)) if prices[i] > 0 and prices[i] < prices_less_than]
item_ids = [item_ids[i] for i in criteria]
prices = [prices[i] for i in criteria]
shop_weights = [shop_weights[i] for i in criteria]
item_descs = [item_descs[i] for i in criteria]

basket_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_of_baskets_per_size = 10000

# Create baskets and write total price of baskets to baskets2.txt
with open('baskets2.txt', 'a') as file:
    for basket_size in basket_sizes:
        for basket in xrange(number_of_baskets_per_size):
            basket_ids = []
            basket_prices = []
            basket_names = []
            print "Creating basket " + str(basket + 1) + "/" + str(number_of_baskets_per_size) + " of size " + str(basket_size) + "..."
            for basket_item_number in xrange(basket_size):
                picked_item = False
                while not picked_item:
                    item_picked = weighted_choice(zip(indices_item_ids, indices_number_weight))
                    try:
                        item_picked_id_in_prices_list = item_ids_unique.index(item_picked)
                        prices_for_that_item = [prices[i] for i in xrange(len(prices)) if item_ids[i] == item_picked]
                        shop_weights_for_that_item = [shop_weights[i] for i in xrange(len(prices)) if item_ids[i] == item_picked]
                        random_pick_price = weighted_choice(zip(prices_for_that_item, shop_weights_for_that_item))
                        item_picked_price = random_pick_price
                        item_picked_name = item_descs[item_ids.index(item_picked)]
                        picked_item = True
                    except ValueError:
                        picked_item = False
                    except AssertionError:
                        picked_item = False
                basket_ids.append(item_picked)
                basket_prices.append(item_picked_price)
                basket_names.append(item_picked_name)
            total_basket_price = sum(basket_prices)
            print basket_size, total_basket_price
            print zip(basket_ids, basket_names, basket_prices)
            file.write(str(basket_size) + "," + str(total_basket_price) + "\n")
