"""
LeetCode: 844
Title: Backspace String Compare
Difficulty: Easy

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        outputS = []
        outputT = []

        for i in s:
            if i == '#':
                if outputS:
                    outputS.pop()
            else:
                outputS.append(i)

        for i in t:
            if i == '#':
                if outputT:
                    outputT.pop()
            else:
                outputT.append(i)

        if outputS == outputT:
            return True
        else:
            return False
