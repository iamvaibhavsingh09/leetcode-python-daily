"""
LeetCode: 2108
Title: Find First Palindromic String in the Array
Difficulty: Easy

"""

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
