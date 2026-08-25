"""
LeetCode: 1486
Title: XOR Operation in an Array
Difficulty: Easy

"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0

        for _ in range(n):
            output ^= start + 2 * (_)

        return output
