"""
LeetCode: 1816
Title: Truncate Sentence
Difficulty: Easy

"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return (' ').join(s.split(' ')[:k])
