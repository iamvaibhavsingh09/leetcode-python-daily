"""
LeetCode: 1768
Title: Merge Strings Alternately
Difficulty: Easy

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        length = min(len(word1),len(word2))

        for w in range(length):
            output.append(word1[w])
            output.append(word2[w])

        if len(word1) > len(word2):
            output.extend(word1[length:])
        else:
            output.extend(word2[length:])

        return ('').join(output)
