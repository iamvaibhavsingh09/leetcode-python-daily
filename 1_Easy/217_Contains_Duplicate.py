"""
LeetCode: 217
Title: Contains Duplicate
Difficulty: Easy

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        duplicate = set()
            
        for var in nums:
            if var not in unique:
                unique.add(var)
            else:
                duplicate.add(var)
                return True

        return False