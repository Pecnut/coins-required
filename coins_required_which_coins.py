# -*- coding: utf-8 -*-
def get_min_coins(coins, target_amount):
    min_coins = [0] + [10000] * target_amount
    for i in range(len(coins)):
        for j in range(coins[i], target_amount + 1):
            min_coins[j] = min(min_coins[j - coins[i]] + 1, min_coins[j])
    return min_coins
      
up_to_amount = 10

print "Average number of coins required"
minimum = up_to_amount
which = ""

for i in range(1,up_to_amount-2):
    for j in range(i+1,up_to_amount-1):
        for k in range(j+1,up_to_amount):
            coins = [1,i,j,k]
            print coins
            average = sum(get_min_coins(coins,up_to_amount))/float(up_to_amount)
            if average < minimum:
                minimum = average
                which = str(coins) + "\n"
            elif average == minimum:
                which += str(coins) + "\n"    

'''
for i in range(1,up_to_amount-1):
    for j in range(i+1,up_to_amount):
            coins = [1,i,j]
            print coins
            average = sum(get_min_coins(coins,up_to_amount))/float(up_to_amount)
            if average < minimum:
                minimum = average
                which = str(coins) + "\n"
            elif average == minimum:
                which += str(coins) + "\n"    
'''
'''
for i in range(1,up_to_amount):
            coins = [1,i]
            print coins
            average = sum(get_min_coins(coins,up_to_amount))/float(up_to_amount)
            if average < minimum:
                minimum = average
                which = str(coins) + "\n"
            elif average == minimum:
                which += str(coins) + "\n"   
'''             
print "---"
print which, str(minimum)



