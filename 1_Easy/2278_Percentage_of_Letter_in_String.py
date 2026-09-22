"""
LeetCode: 2278
Title: Percentage of Letter in String
Difficulty: Easy

"""

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0

        for var in s:
            if var == letter:
                count += 1


        return int(count/len(s)*100)
