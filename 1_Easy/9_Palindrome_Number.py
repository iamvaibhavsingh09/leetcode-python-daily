"""
LeetCode: 9
Title: Palindrome Number
Difficulty: Easy

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x)[:]:
            return True
        else:
            return False