"""
LeetCode: 3512
Title: Minimum Operations to Make Array Sum Divisible by K
Difficulty: Easy

"""

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        newSum = sum(nums)
        operations = 0

        while newSum % k != 0:
            newSum -= 1
            operations += 1  

        return operations
