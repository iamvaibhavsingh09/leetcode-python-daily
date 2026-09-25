"""
LeetCode: 1784
Title: Check if Binary String Has at Most One Segment of Ones
Difficulty: Easy

"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        prev = ''
        segmentCount = 0


        for i in s:
            if i == '1' and prev != '1':
                segmentCount += 1
                
            prev = i


        return segmentCount <= 1
