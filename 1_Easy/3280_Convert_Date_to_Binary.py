"""
LeetCode: 3280
Title: Convert Date to Binary
Difficulty: Easy

"""

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        output = []
        dateList = date.split('-')

        for n in dateList:
            output.append(bin(int(n))[2:])

        return '-'.join(output)
