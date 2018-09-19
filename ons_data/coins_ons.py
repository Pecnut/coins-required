
import csv
import numpy as np
import matplotlib.pyplot as plt
import random
data = []
item_ids = []; item_descs = []; validities = []; shop_codes = []; all_prices = []; regions = [];
with open('price_quote_201807.csv', 'rb') as csvfile:
    csvReader = csv.reader(csvfile)
    for row in csvReader:
        if row[0] == 'QUOTE_DATE':
            continue
        item_ids.append(int(row[1]))
        item_descs.append(row[2])
        validities.append(int(row[3]))
        shop_codes.append(int(row[4]))
        all_prices.append(int(float(row[5])*100))
        regions.append(int(row[14]))


# Titles are
# ['QUOTE_DATE', 'ITEM_ID', 'ITEM_DESC', 'VALIDITY', 'SHOP_CODE',
#  'PRICE', 'INDICATOR_BOX', 'ORIG_INDICATOR_BOX', 'PRICE_RELATIVE',
#  'LOG_PRICE_RELATIVE', 'STRATUM_WEIGHT', 'STRATUM_TYPE', 'START_DATE',
#  'END_DATE', 'REGION', 'SHOP_TYPE', 'SHOP_WEIGHT', 'BASE_PRICE', 'BASE_VALIDITY', 'STRATUM_CELL']

## !! Everything is in PENNIES !!
prices = all_prices

# Remove invalid results
criteria = [i for i in xrange(len(prices)) if validities[i]==3 or validities[i]==4]
item_ids = [item_ids[i] for i in criteria]
prices = [prices[i] for i in criteria]

# Pick mode price for each item
'''
item_ids_unique = list(set(item_ids))
mode_prices = []
for item_id in item_ids_unique:
    prices_for_that_item = [prices[i] for i in xrange(len(prices)) if item_ids[i] == item_id]
    mode_price = max(set(prices_for_that_item), key=prices_for_that_item.count)
    mode_prices.append(mode_price)
prices = mode_prices
'''
'''
# Pick random price for each item
item_ids_unique = list(set(item_ids))
random_pick_prices = []
for item_id in item_ids_unique:
    prices_for_that_item = [prices[i] for i in xrange(len(prices)) if item_ids[i] == item_id]
    random_pick_price = random.choice(prices_for_that_item)
    random_pick_prices.append(random_pick_price)
prices = random_pick_prices
'''

# Anything between £0 and £20
prices_less_than = 2000
criteria = [i for i in xrange(len(prices)) if prices[i] > 0 and prices[i] < prices_less_than]
prices = [prices[i] for i in criteria]

# data from london
#data = data[data[:,14] == '2']

lowest_banknote = 100
lowest_coin = 1
ends_in = range(0,lowest_banknote,lowest_coin)
prices_mod_lowest_banknote = [i%lowest_banknote for i in prices]
prices_end_in_count = [ sum(1 for i in prices_mod_lowest_banknote if i==j) for j in ends_in]

index = np.arange(len(prices_end_in_count))
#ends_in_labels = ["%02i"%i for i in ends_in]
prices_end_in_count_as_percent = [i/sum(prices_end_in_count)*100 for i in prices_end_in_count]
plt.bar(index,prices_end_in_count_as_percent)
#plt.xticks(index,ends_in_labels,rotation=90)
xticks_at = range(0,lowest_banknote,5) + [lowest_banknote-1]
xticks_labels = ["%02i"%i for i in xticks_at]
plt.xticks(xticks_at,xticks_labels)
plt.ylabel("%")
plt.xlabel("price ends in")
plt.title(u'Prices less than £' + "%.2f" % (prices_less_than/100) + u" mod £" + "%.2f" % (lowest_banknote/100))
plt.show()
