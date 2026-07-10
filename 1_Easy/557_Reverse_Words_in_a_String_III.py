"""
LeetCode: 557
Title: Reverse Words in a String III
Difficulty: Easy

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        newList = list()

        for var in s.split(' '):
            newList.append(var[::-1])
            
        return ' '.join(newList)