"""
LeetCode: 448
Title: Find All Numbers Disappeared in an Array
Difficulty: Easy

"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = list()
        checkSet = set(nums)

        for n in range(1,len(nums)+1):
            if n not in checkSet:
                output.append(n)

        return output