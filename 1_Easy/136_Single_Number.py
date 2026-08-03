"""
LeetCode: 136
Title: Single Number
Difficulty: Easy

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = result ^ n
            
        return result