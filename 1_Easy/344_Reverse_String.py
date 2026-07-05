"""
LeetCode: 344
Title: Reverse String
Difficulty: Easy

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]