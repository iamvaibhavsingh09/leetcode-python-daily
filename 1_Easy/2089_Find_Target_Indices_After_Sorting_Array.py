"""
LeetCode: 2089
Title: Find Target Indices After Sorting Array
Difficulty: Easy

"""

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums.sort()

        for i,num in enumerate(nums):
            if target == num:
                result.append(i)

        return result