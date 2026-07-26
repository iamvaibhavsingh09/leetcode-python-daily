"""
LeetCode: 349
Title: Intersection of Two Arrays
Difficulty: Easy

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
