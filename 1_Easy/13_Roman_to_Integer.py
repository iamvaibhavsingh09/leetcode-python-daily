"""
LeetCode: 13
Title: Roman to Integer
Difficulty: Easy

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        romanValues = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        output = 0

        for index in range(len(s)):
            current = romanValues[s[index]]

            if index + 1 < len(s) and current < romanValues[s[index + 1]]:
                output -= current

            else:
                output += current

        return output
