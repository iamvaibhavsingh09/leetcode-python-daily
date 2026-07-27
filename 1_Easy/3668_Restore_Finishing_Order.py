"""
LeetCode: 3668
Title: Restore Finishing Order
Difficulty: Easy

"""

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []

        for i in order:
            if i in friends:
                result.append(i)
                
        return result
