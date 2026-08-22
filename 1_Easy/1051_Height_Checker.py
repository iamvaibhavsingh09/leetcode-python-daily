"""
LeetCode: 1051
Title: Height Checker
Difficulty: Easy

"""

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        output = 0
        expected = sorted(heights)

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                output += 1

        return output
        return ouptut
