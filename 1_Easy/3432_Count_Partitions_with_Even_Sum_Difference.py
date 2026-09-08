"""
LeetCode: 3432
Title: Count Partitions with Even Sum Difference
Difficulty: Easy

"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        output = 0

        for i in range(1,len(nums)):
            sumDifference = sum(nums[:i]) - sum(nums[i:])

            if sumDifference % 2 == 0:
                output += 1
            
        return output
