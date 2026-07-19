"""
LeetCode: 3959
Title: Check Good Integer
Difficulty: Easy

"""

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum, squareSum = 0, 0

        for digit in str(n):
            digitSum = digitSum + int(digit)
            squareSum = squareSum + pow(int(digit),2)

        if (squareSum - digitSum) >= 50:
            return True

        else:
            return False