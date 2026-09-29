# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:06:35 2023

@author: LENOVO
"""

def edit_distance(string1, string2):
    m = len(string1)
    n = len(string2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

str1 = input("Enter string 1")
str2 = input("Enter string 2")
distance = edit_distance(str1, str2)
print(f"The edit distance between '{str1}' and '{str2}' is {distance}")
