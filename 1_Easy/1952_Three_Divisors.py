"""
LeetCode: 1952
Title: Three Divisors
Difficulty: Easy

"""

class Solution:
    def isThree(self, n: int) -> bool:
        divisor = 0

        for i in range(1,n+1):
            if n % i == 0:
                divisor += 1

        if divisor == 3:
            return True
        else:
            return False
