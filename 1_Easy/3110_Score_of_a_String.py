"""
LeetCode: 3110
Title: Score of a String
Difficulty: Easy

"""

class Solution:
    def scoreOfString(self, s: str) -> int:
        output = 0

        for i,ol in enumerate(s):
            nxt = i+1
            if nxt < len(s): 
                output = (abs(ord(s[i]) - ord(s[i+1]))) + output
                
        return output