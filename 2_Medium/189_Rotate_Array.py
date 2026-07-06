"""
LeetCode: 189
Title: Rotate Array
Difficulty: Medium

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:]+ nums[:-k]