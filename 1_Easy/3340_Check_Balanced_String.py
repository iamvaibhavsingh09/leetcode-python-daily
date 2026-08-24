"""
LeetCode: 3340
Title: Check Balanced String
Difficulty: Easy

"""

class Solution:
    def isBalanced(self, num: str) -> bool:
        oddSum, evenSum = 0, 0

        for i,n in enumerate(num):
            if i % 2 == 0:
                evenSum += int(n)
            else:
                oddSum += int(n)

        if evenSum == oddSum:
            return True
        else:
            return False