"""
LeetCode: 3701
Title: Compute Alternating Sum
Difficulty: Easy

"""

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        computeSum = 0

        for num in range(len(nums)):
            if num % 2 == 0:
                #even
                computeSum += nums[num]
                
            else:
                #odd
                computeSum -= nums[num]

        return computeSum