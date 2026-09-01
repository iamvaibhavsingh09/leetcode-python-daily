"""
LeetCode: 3541
Title: Find Most Frequent Vowel and Consonant
Difficulty: Easy

"""

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')
        vowelDict = {} 
        consonantDict = {}

        for var in s:
            if var in vowels:
                if var in vowelDict:
                    newVar = vowelDict[var]
                    vowelDict[var] = newVar + 1
                else:
                    vowelDict[var] = 1
            else:
                if var in consonantDict:
                    newVar = consonantDict[var]
                    consonantDict[var] = newVar + 1
                else:
                    consonantDict[var] = 1
        
        max_vowel = max(vowelDict.values(), default=0)
        max_consonant = max(consonantDict.values(), default=0)

        return max_vowel + max_consonant
