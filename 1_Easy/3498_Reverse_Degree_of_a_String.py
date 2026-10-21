"""
LeetCode: 3498
Title: Reverse Degree of a String
Difficulty: Easy

"""

class Solution:
    def reverseDegree(self, s: str) -> int:
        output = 0

        for i,var in enumerate(s):
            degree = 26 - (ord(var) - ord('a'))
            output += (i+1) * degree

        return output
