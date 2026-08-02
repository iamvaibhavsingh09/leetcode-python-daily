"""
LeetCode: 3550
Title: Smallest Index With Digit Sum Equal to Index
Difficulty: Easy

"""

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            digitSum = 0
            for num in str(n):
                digitSum += int(num)
            if i == digitSum:
                return i
                break
        else:
            return -1
