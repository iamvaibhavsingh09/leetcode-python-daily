"""
LeetCode: 3978
Title: Unique Middle Element
Difficulty: Easy

"""

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        middle = len(nums)//2

        unique = set()
        repeatedV = set()

        for num in nums:
            if num in unique:
                repeatedV.add(num)
            else:
                unique.add(num)

        if nums[middle] in repeatedV:
            return False
        else:
            return True