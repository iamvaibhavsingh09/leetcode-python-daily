"""
LeetCode: 1859
Title: Sorting the Sentence
Difficulty: Easy

"""

class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(' ')
        output = [None] * len(arr)

        for word in arr:
            output[int(word[-1:])-1] = word[:-1]
            
        return ' '.join(output)
