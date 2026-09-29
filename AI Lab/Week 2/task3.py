# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:42:36 2023

@author: LENOVO
"""
def cutRod(price, n):
    if n <= 0:
        return 0
    max_value = -999999
    
    for i in range(n):
        max_value = max(max_value, price[i] + cutRod(price, n - i - 1))
    
    return max_value

# Example usage:
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(price)
result = cutRod(price, n)
print("Maximum value obtainable:", result)

