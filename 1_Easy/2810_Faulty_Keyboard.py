"""
LeetCode: 2810
Title: Faulty Keyboard
Difficulty: Easy

"""

class Solution:
    def finalString(self, s: str) -> str:
        newL = []

        for var in s:
            if var == 'i':
                newL[:] = newL[::-1]
            else:
                newL.append(var)

        return ('').join(newL)