"""
LeetCode: 2139
Title: Minimum Moves to Reach Target Score
Difficulty: Easy

"""

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operation = 0

        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            
            operation += 1

        operation += target - 1
        
        return operation
