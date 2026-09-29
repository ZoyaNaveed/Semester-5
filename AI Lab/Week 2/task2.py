# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:54:50 2023

@author: LENOVO
"""

def longest_common_substring(s1, s2, m, n, count):
    if m == 0 or n == 0:
        return count

    if s1[m - 1] == s2[n - 1]:
        count = longest_common_substring(s1, s2, m - 1, n - 1, count + 1)
    
    count = max(count, max(longest_common_substring(s1, s2, m - 1, n, 0), longest_common_substring(s1, s2, m, n - 1, 0)))
    
    return count

def longest_common_substring_length(s1, s2):
    m = len(s1)
    n = len(s2)
    return longest_common_substring(s1, s2, m, n, 0)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = longest_common_substring_length(s1, s2)
print("Length of the longest common substring:", result)