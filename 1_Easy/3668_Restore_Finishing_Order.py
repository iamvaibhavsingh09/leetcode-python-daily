"""
LeetCode: 3668
Title: Restore Finishing Order
Difficulty: Easy

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))