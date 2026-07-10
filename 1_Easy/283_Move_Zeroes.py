"""
LeetCode: 283
Title: Move Zeroes
Difficulty: Easy

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        newList = []
        zeroes = list()
        for num in nums:
            if num != 0:
                newList.append(num)
            else:
                zeroes.append(num)
                
        nums[:] = newList + zeroes