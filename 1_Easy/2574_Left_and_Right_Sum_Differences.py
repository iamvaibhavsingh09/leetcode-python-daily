"""
LeetCode: 2574
Title: Left and Right Sum Differences
Difficulty: Easy

"""

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        result = []

        total = sum(nums)

        for i,n in enumerate(nums):
            right = total - n - left
            result.append(abs(right - left))
            left += n

        return result
