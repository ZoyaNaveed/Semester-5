# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:51:15 2023

@author: LENOVO
"""

def compute_alignment_score(S, T, match_score, mismatch_score, gap_penalty):
    def dp(i, j):
        if i == 0 and j == 0:
            return 0
        elif i == 0:
            return j * gap_penalty
        elif j == 0:
            return i * gap_penalty
        else:
            match = dp(i - 1, j - 1) + (match_score if S[i - 1] == T[j - 1] else mismatch_score)
            gap_s = dp(i - 1, j) + gap_penalty
            gap_t = dp(i, j - 1) + gap_penalty
            return max(match, gap_s, gap_t)
    
    return dp(len(S), len(T))

# Example usage:
S = "AGTACGCA"
T = "TATGC"
match_score = 2
mismatch_score = -1
gap_penalty = -2

alignment_score = compute_alignment_score(S, T, match_score, mismatch_score, gap_penalty)
print("Optimal Alignment Score:", alignment_score)
