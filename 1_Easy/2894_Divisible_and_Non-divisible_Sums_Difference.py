"""
LeetCode: 2894
Title: Divisible and Non-divisible Sums Difference
Difficulty: Easy

"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divSum, divNot = 0, 0
        
        for var in range(1,n + 1):
            if var % m == 0:
                divSum = divSum + var
            else:
                divNot = divNot + var
        
        return divNot-divSum