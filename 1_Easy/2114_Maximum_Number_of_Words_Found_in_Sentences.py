"""
LeetCode: 2114
Title: Maximum Number of Words Found in Sentences
Difficulty: Easy

"""

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0

        for sentence in sentences:
            wordCount = len(sentence.split(' '))
            if output < wordCount:
                output = wordCount

        return output
