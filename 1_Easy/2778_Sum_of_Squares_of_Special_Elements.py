"""
LeetCode: 2778
Title: Sum of Squares of Special Elements 
Difficulty: Easy

"""

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums) 
        output = 0

        for i in range(n):
            if n % (i+1) == 0:
                output += nums[i]**2 
    
        return output