"""
LeetCode: 1672
Title: Richest Customer Wealth
Difficulty: Easy

"""

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []

        for acc in accounts:
            wealth.append(sum(acc))

        return max(wealth)