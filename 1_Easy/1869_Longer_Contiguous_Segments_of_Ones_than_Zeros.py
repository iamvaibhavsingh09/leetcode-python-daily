"""
LeetCode: 1869
Title: Longer Contiguous Segments of Ones than Zeros
Difficulty: Easy

"""

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeroCount, oneCount, zeroMax, oneMax = 0, 0, 0, 0

        for n in s:
            if n == '1':
                oneCount += 1
                oneMax = max(oneMax,oneCount)
                zeroCount = 0
            elif n == '0':
                zeroCount += 1
                zeroMax = max(zeroMax,zeroCount)
                oneCount = 0
        
        return oneMax > zeroMax
