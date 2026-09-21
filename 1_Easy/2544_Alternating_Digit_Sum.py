"""
LeetCode: 2544
Title: Alternating Digit Sum
Difficulty: Easy

"""

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        output = 0

        for i,number in enumerate(str(n)):
            if i % 2 == 0:
                output += int(number)
            else:
                output -= int(number)

        return output
