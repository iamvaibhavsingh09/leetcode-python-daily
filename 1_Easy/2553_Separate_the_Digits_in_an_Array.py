"""
LeetCode: 2553
Title: Separate the Digits in an Array
Difficulty: Easy

"""

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            for n in str(num):
                result.append(int(n))
        
        return result