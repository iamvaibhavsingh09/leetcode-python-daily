"""
LeetCode: 1684
Title: Count the Number of Consistent Strings
Difficulty: Easy

"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for word in words:
            wordSet = set(word)

            if wordSet.issubset(set(allowed)):
                count += 1

        return count
