"""
LeetCode: 3925
Title: Concatenate Array With Reverse
Difficulty: Easy

"""

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans =[]
        ans[:] = nums+nums[::-1]
        return ans