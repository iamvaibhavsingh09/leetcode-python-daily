"""
LeetCode: 20
Title: Valid Parentheses
Difficulty: Easy

"""

class Solution:
    def isValid(self, s: str) -> bool:
        values = {'(': ')','{': '}','[':']'}
        stack = []
        
        for brc in s:
            if brc in values:
                stack.append(brc)
            
            else:
                if not stack:
                    return False

                if values[stack[-1]] != brc:
                    return False

                stack.pop()
        
        return len(stack) == 0
