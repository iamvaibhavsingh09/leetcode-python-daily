"""
LeetCode: 2535
Title: Difference Between Element Sum and Digit Sum of an Array
Difficulty: Easy

"""

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0

        for var in nums:
            elementSum += var
            
            for digit in str(var):
                digitSum += int(digit)
                

        absoluteSum = abs(elementSum-digitSum)
        return absoluteSum


# Brute Force
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0

        for var in nums:
            elementSum = elementSum + var
                
        for var in nums:
            digitSum = digitSum + var
            if len(str(var)) == 2:
                digitSum = digitSum - var
                digitSum = digitSum + int(str(var)[0]) + int(str(var)[1])
            elif len(str(var)) == 3:
                digitSum = digitSum - var
                digitSum = digitSum + int(str(var)[0]) + int(str(var)[1]) + int(str(var)[2])
            elif len(str(var)) == 4:
                digitSum = digitSum - var
                digitSum = digitSum + int(str(var)[0]) + int(str(var)[1]) + int(str(var)[2])+ int(str(var)[3])

        absoluteDifference = abs(elementSum-digitSum)
        return absoluteDifference