import itertools

def get_min_coins(coins, target_amount):
    n = len(coins)
    min_coins = [0] + [10000] * target_amount
    for i in range(n):
        for j in range(coins[i], target_amount + 1):
            min_coins[j] = min(min_coins[j - coins[i]] + 1, min_coins[j])
    return min_coins
    
up_to_amount = 499
coins = [1,2,5,10,20,50,100,200]

for combi in list(itertools.combinations(coins,8)):
    print combi, sum(get_min_coins(combi,up_to_amount))/float(up_to_amount)
    
#sorted(student_tuples, key=lambda student: student[2])    