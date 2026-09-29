# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:45:00 2023

@author: LENOVO
"""

def minCoins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[target] == -999999:
        return -1
    else:
        return dp[target]

# Example usage:
my_list = []
n = int(input("Enter the number of coins: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    my_list.append(element)
    
target_amount = int(input("Enter target value: "))
min_coins_required = minCoins(my_list, target_amount)
print("Minimum number of coins required:", min_coins_required)