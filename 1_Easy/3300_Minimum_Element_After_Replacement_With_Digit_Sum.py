"""
LeetCode: 3300
Title: Minimum Element After Replacement With Digit Sum
Difficulty: Easy

"""

class Solution:
    def minElement(self, nums: List[int]) -> int:
        newList = []

        for num in nums:
            var = 0
            for n in str(num):
                var += int(n)
            newList.append(var)

        return min(newList)
