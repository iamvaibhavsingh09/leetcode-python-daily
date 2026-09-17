"""
LeetCode: 3285
Title: Find Indices of Stable Mountains
Difficulty: Easy

"""

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        output = []

        for i in range(1,len(height)):
            if height[i-1] > threshold:
                output.append(i)

        return output
