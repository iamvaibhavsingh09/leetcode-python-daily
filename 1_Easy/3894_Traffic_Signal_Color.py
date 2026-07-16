"""
LeetCode: 3894
Title: Traffic Signal Color
Difficulty: Easy

"""

class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return 'Green'

        elif timer == 30:
            return 'Orange'

        elif 30 < timer <= 90:
            return 'Red'

        else:
            return 'Invalid'