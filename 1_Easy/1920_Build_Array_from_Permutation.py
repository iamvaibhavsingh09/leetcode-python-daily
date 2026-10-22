"""
LeetCode: 1920
Title: Build Array from Permutation
Difficulty: Easy

"""

class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        arr = []

        for n in range(len(nums)):
            arr.append(nums[nums[n]])
        
        return arr
