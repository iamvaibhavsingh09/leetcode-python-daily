"""
LeetCode: 50
Title: Pow(x, n)
Difficulty: Medium

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = f"{pow(x,n):.5f}"
        return float(result)