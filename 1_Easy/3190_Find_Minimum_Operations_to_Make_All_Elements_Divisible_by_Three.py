"""
LeetCode: 3190
Title: Find Minimum Operations to Make All Elements Divisible by Three
Difficulty: Easy

"""

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        output = 0

        for num in nums:
            if num % 3 != 0:
                output += 1

        return output
