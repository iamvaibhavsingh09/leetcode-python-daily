"""
LeetCode: 3898
Title: Find the Degree of Each Vertex
Difficulty: Easy

"""

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        output = []
        count = 0

        for rix in matrix:
            count = 0
            for r in rix:
                if r == 1:
                    count += 1
            output.append(count)

        return output
