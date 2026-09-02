"""
LeetCode: 258
Title: Add Digits
Difficulty: Easy

"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            output = 0
            for n in str(num):
                output += int(n)

            num = output
        
        return num
