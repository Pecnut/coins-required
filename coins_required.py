#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Calculates the average number of coins you would need to generate amounts up to `up_to_amount`, assuming that
each amount is equally likely. Also generates the average weight of these coins (actual weight, like in kilograms!)
if you provide the `weights` as well.
"""


def get_min_coins(coins, target_amount, weights=0):
    # Returns an array X = [0,1,1,...] of length target_amount,
    # where X_i tells you the number of coins you need to make i money
    # Here, weights is actual (like in kilograms!) weight of the coins.
    if weights == 0:
        weights = [1 for i in range(len(coins))]
    min_coins = [0] + [10000] * target_amount
    min_coins_desc = [0] + [10000] * target_amount
    min_coins_weight = [0] + [10000] * target_amount
    n = len(coins)
    for c in range(n):
        for target in range(coins[c], target_amount + 1):
            if min_coins[target - coins[c]] + 1 < min_coins[target]:
                min_coins_desc[target] = min_coins_desc[target - coins[c]] + 10**(n - c - 1)
            min_coins[target] = min(min_coins[target - coins[c]] + 1, min_coins[target])
            min_coins_weight[target] = min(min_coins_weight[target - coins[c]] + weights[c], min_coins_weight[target])
    for target in range(target_amount + 1):
        min_coins_desc[target] = str(min_coins_desc[target]).zfill(n)
    return min_coins, min_coins_desc, min_coins_weight


name = "UK"
up_to_amount = 499
coins = [1, 2, 5, 10, 20, 50, 100, 200]
weights = [3.56, 7.12, 3.25, 6.5, 5, 8, 9.5, 12]

'''
name = "UK self-service"
up_to_amount = 499
coins = [1,2,5,20,100,200]
weights = [3.56,7.12,3.25,5,9.5,12]

name = "UK 1960"
up_to_amount = 479 # in farthings
coins = [1,2,1*4,3*4,6*4,12*4,24*4,30*4]
weights = [2.83,5.67,9.4,6.8,2.83,5.66,11.31,14.14]

name = "US"
up_to_amount = 99
coins = [1,5,10,25]
weights = [2.5,5,2.268,5.67]

name = "Canada"
up_to_amount = 495/5
coins = [5/5,10/5,25/5,100/5,200/5]
weights = [3.95,1.75,4.4,6.27,6.92]

name = "Euro"
up_to_amount = 499
coins = [1,2,5,10,20,50,100,200]
weights = [2.3,3.06,3.92,4.1,5.74,7.8,7.5,8.5]

name = "Japan"
up_to_amount = 999
coins = [1,5,10,50,100,500]
weights = [1,3.75,4.5,4,4.8,7]

name = "Switzerland"
up_to_amount = 995/5
coins = [5/5,10/5,20/5,50/5,100/5,200/5,500/5]
weights = [1.8,3,4,2.2,4.4,8.8,13.2]

name = "Australia"
up_to_amount = 495/5
coins = [5/5,10/5,20/5,50/5,100/5,200/5]
weights = [2.83,5.65,11.3,15.55,9,6.6]

name = "NZ"
up_to_amount = 490/10
coins = [10/10,20/10,50/10,100/10,200/10]
weights = [3.3,4,5,8,10]

name = "Harry Potter"
up_to_amount = 492
coins = [1,29]
weights = [1,29]

name = "Mexico"
up_to_amount = 1950/50
coins = [50/50,100/50,200/50,500/50,1000/50]
weights = [3.103,3.95,5.19,7.07,10.329]

name = "China"
up_to_amount = 100/10
coins = [10/10,50/50]
weights = [3.22,3.8]

name = "Sweden"
up_to_amount = 19
coins = [1,2,5,10]
weights = [3.6,4.8,6.1,6.6]

name = "Euro no 1 or 2 cent"
up_to_amount = 495/5
coins = [5/5,10/5,20/5,50/5,100/5,200/5]
weights = [3.92,4.1,5.74,7.8,7.5,8.5]

name = "UK new £1 coin"
up_to_amount = 499
coins = [1,2,5,10,20,50,100,200]
weights = [3.56,7.12,3.25,6.5,5,8,8.75,12]

name = "Singapore"
up_to_amount = 195/5
coins = [5/5,10/5,20/5,50/5,100/5]
weights = [1.24,2.83,5.66,9.33,16.85]

name = "HK"
up_to_amount = 990/10
coins = [10/10,20/10,50/10,100/10,200/10,500/10]
weights = [1.85,2.59,4.92,7.1,8.41,13.5]

name = "Norway"
up_to_amount = 49
coins = [1,5,10,20]
weights = [4.35,7.85,6.8,9.9]

name = "S Korea"
up_to_amount = 990/10
coins = [10/10,50/10,100/10,500/10]
weights = [1.22,4.16,5.42,7.7]

name = "Turkey"
up_to_amount = 495/5
coins = [5/5,10/5,25/5,50/5,100/5]
weights = [2.9,3.15,4,6.8,8.2]

name = "India"
up_to_amount = 9
coins = [1,2,5]
weights = [3.79,4.85,6]

name = "Russia"
up_to_amount = 4990/10
coins = [10/10,50/10,100/10,200/10,500/10,1000/10]
weights = [1.95,2.9,3.25,5.1,6.45,5.63]

name = "Brazil"
up_to_amount = 195/5
coins = [5/5,10/5,25/5,50/5,100/5]
weights = [4.1,4.8,7.55,7.81,7]

name = "South Africa"
up_to_amount = 990/10
coins = [10/10,20/10,50/10,100/10,200/10,500/10]
weights = [2,3.5,5,4,5.5,9.5]

name = "UK with £1.33"
up_to_amount = 499
coins = [1,2,5,10,20,50,100,133,200]
weights = [3.56,7.12,3.25,6.5,5,8,9.5,30,12]

name = "Best 3"
up_to_amount = 499
coins = [1, 7, 57, 80]
weights = 0

name = "Stamps"
up_to_amount = 499
coins = [1, 55, 64, 75, 96, 105, 133, 152, 225]
weights = 0

name = "UK with £1.23 instead of £1"
up_to_amount = 499
coins = [1,2,5,10,20,50,123,200]
weights = [3.56,7.12,3.25,6.5,5,8,8.75,12]

name = "UK with no 1p or 2p"
up_to_amount = 495/5
coins = [5/5,10/5,20/5,50/5,100/5,200/5]
weights = [3.25,6.5,5,8,9.5,12]
#coins = [1,2,1*4,3*4,6*4,12*4,24*4,30*4]

name = "UK with 25p instead of 20p"
up_to_amount = 499
coins = [1,2,5,10,25,50,100,200]
weights = [3.56,7.12,3.25,6.5,5,8,9.5,12]
'''
print name
print "Lowest note: ", up_to_amount + 1
print "Coins: ", coins
print "Average number of coins required: ", round(sum(get_min_coins(coins, up_to_amount)[0]) / float(up_to_amount), 2)
print "Average weight of coins required: ", round(sum(get_min_coins(coins, up_to_amount, weights)[2]) / float(up_to_amount), 1), "g"
print "On average expect to receive X of each coin: ",
each_coin = get_min_coins(coins, up_to_amount)[1]
print [round(sum([float(each_coin[amount][c]) for amount in range(len(each_coin))]) / float(len(each_coin)), 3) for c in range(len(coins))]
