"""
LeetCode: 3760
Title: Maximum Substrings With Distinct Start
Difficulty: Medium

"""

class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
