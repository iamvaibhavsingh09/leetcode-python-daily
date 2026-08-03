"""
LeetCode: 3986
Title: Number of Elapsed Seconds Between Two Times
Difficulty: Easy

"""

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        newStart = startTime.split(':')
        newEnd = endTime.split(':')

        startInSec = int(newStart[0])*3600 + int(newStart[1])*60 + int(newStart[2])
        endInSec = int(newEnd[0])*3600 + int(newEnd[1])*60 + int(newEnd[2])

        return endInSec-startInSec