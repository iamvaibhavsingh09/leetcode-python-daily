"""
LeetCode: 3099
Title: Harshad Number
Difficulty: Easy

"""

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digit = 0

        for i in str(x):
            digit = digit + int(i)
        
        if x % digit == 0:
            return digit

        else:
            return -1