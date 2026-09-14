"""
LeetCode: 1732
Title: Find the Highest Altitude
Difficulty: Easy

"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]

        for g in gain:
            altitude.append(altitude[-1] + g)

        return max(altitude)
