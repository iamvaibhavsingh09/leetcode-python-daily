"""
LeetCode: 3908
Title: Valid Digit Number
Difficulty: Easy

"""

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        if str(x) in str(n) and str(n)[0] != str(x):
            return True
        else:
            return False