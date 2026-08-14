"""
LeetCode: 1342
Title: Number of Steps to Reduce a Number to Zero
Difficulty: Easy

"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        stepCount = 0

        while num > 0:
            newNum = 0
            if num % 2 == 0:
                newNum = num // 2
                num = newNum
                stepCount += 1
            elif num % 2 != 0:
                newNum = num - 1
                num = newNum
                stepCount += 1

        return stepCount