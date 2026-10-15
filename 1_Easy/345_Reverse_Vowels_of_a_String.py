"""
LeetCode: 345
Title: Reverse Vowels of a String
Difficulty: Easy

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueDict = {}
        repeatedValues = set()

        for i,e in enumerate(s):
            if e not in uniqueDict and e not in repeatedValues:
                uniqueDict[e] = i
            elif e in uniqueDict:
                uniqueDict.pop(e)
                repeatedValues.add(e)

        if uniqueDict:
            return min(uniqueDict.values())
        else:
            return -1
