"""
LeetCode: 2248
Title: Intersection of Multiple Arrays
Difficulty: Easy

"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        result = set(nums[0])

        for arr in nums[1:]:
            result = set(arr).intersection(result)
            
        return sorted(list(result))