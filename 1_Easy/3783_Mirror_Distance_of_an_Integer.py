"""
LeetCode: 3783
Title: Mirror Distance of an Integer
Difficulty: Easy

"""

class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirrorDistance = abs(n-int(str(n)[::-1]))
        return mirrorDistance