"""
LeetCode: 3945
Title: Digit Frequency Score
Difficulty: Easy

"""

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        score = 0
        for num in str(n):
            score = score + int(num)
            
        return score