"""
LeetCode: 1979
Title: Find Greatest Common Divisor of Array
Difficulty: Easy

"""

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx,mn = max(nums), min(nums)

        for i in reversed(range(1,mn+1)):
                    if mx % i == 0 and mn % i == 0:
                        return i