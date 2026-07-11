"""
LeetCode: 771
Title: Jewels and Stones
Difficulty: Easy

"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        
        for jw in stones:
            if jw in jewels:
                count += 1
                
        return count