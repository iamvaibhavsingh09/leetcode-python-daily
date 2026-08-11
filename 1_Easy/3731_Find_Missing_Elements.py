"""
LeetCode: 3731
Title: Find Missing Elements
Difficulty: Easy

"""

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start = min(nums)
        end = max(nums)
        missing = []

        for i in range(start,end+1):
            if i not in nums:
                missing.append(i)

        return missing