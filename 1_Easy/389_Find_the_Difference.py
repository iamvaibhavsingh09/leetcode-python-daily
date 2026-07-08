"""
LeetCode: 389
Title: Find the Difference
Difficulty: Easy

"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        for val in s:
            result = result ^ ord(val)

        for val in t:
            result = result ^ ord(val)

        return chr(result)