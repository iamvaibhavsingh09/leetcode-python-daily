"""
LeetCode: 2011
Title: Final Value of Variable After Performing Operations
Difficulty: Easy

"""

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0

        for op in operations:
            if '+' in op:
                output += 1
            else:
                output -= 1

        return output
