"""
LeetCode: 2652
Title: Sum Multiples
Difficulty: Easy

"""

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        numSum = 0
        for num in range(1,n+1):
            if num % 3 == 0:
                numSum += num
            elif num % 5 == 0:
                numSum += num
            elif num % 7 == 0:
                numSum += num
        
        return numSum
