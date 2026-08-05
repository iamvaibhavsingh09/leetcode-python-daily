"""
LeetCode: 2000
Title: Reverse Prefix of Word
Difficulty: Easy

"""

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)

        if idx == -1:
            return word

        else:
            return (word[:idx+1][::-1] + word[idx+1:])


# Brute Force
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        output = ''
        count = 0

        for w in word:
            if w == ch and (count == 0):
                count = 1
                output = output + w
                output = output[::-1]
            else:
                output = output + w
            
        return output