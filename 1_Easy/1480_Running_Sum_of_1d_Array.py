"""
LeetCode: 1480
Title: Running Sum of 1d Array
Difficulty: Easy

"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = nums[0]
        result = list()

        result.append(runningSum)

        for num in nums[1:]:
            runningSum += num 
            result.append(runningSum)
            
        return result
