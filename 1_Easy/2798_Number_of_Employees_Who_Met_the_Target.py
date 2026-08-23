"""
LeetCode: 2798
Title: Number of Employees Who Met the Target
Difficulty: Easy

"""

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        result = 0


        for hr in hours:
            if hr >= target:
                result += 1

        return result
