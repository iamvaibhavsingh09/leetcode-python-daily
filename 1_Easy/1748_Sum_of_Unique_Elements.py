"""
LeetCode: 1748
Title: Sum of Unique Elements
Difficulty: Easy

"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        countDict ={}
        output = 0

        for num in nums:
            if num in countDict:
                var = countDict[num]
                var += 1 
                countDict[num] = var
            else:
                countDict[num] = 1

        for key,value in countDict.items():
            if value == 1:
                output += key
            
        return output
