"""
LeetCode: 58
Title: Length of Last Word
Difficulty: Easy

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0

        return len(words[-1])
