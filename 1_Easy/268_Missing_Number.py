"""
LeetCode: 268
Title: Missing Number
Difficulty: Easy

"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for num in range(0,len(nums)+1):
            if num not in nums:
                return num
