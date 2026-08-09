"""
LeetCode: 2215
Title: Find the Difference of Two Arrays
Difficulty: Easy

"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1).difference(set(nums2))),list(set(nums2).difference(set(nums1)))]
