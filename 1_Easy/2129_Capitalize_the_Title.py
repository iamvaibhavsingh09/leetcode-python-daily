"""
LeetCode: 2129
Title: Capitalize the Title
Difficulty: Easy

"""

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        newList = title.split(' ')
        result = list()

        for var in newList:
            if len(var) > 2:
                result.append(var.capitalize())
            else:
                result.append(var.lower())

        return (' ').join(result)