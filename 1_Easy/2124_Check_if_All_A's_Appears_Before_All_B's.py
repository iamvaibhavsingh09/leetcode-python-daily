"""
LeetCode: 2124
Title: Check if All A's Appears Before All B's
Difficulty: Easy

"""

class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s
