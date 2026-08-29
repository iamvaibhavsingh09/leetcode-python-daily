"""
LeetCode: 1431
Title: Kids With the Greatest Number of Candies
Difficulty: Easy

"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = list()

        for candy in candies:
            if candy + extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False) 

        return output
