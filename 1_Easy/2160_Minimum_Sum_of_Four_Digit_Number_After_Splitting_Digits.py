"""
LeetCode: 2160
Title: Minimum Sum of Four Digit Number After Splitting Digits
Difficulty: Easy

"""

class Solution:
    def minimumSum(self, num: int) -> int:
        n = sorted(str(num))
        return int(n[0] + n[3]) + int(n[1] + n[2])
