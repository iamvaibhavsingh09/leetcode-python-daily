"""
LeetCode: 3941
Title: Password Strength
Difficulty: Medium

"""

class Solution:
    def passwordStrength(self, password: str) -> int:
        fivePoint = {'!','@','#','$'}
        uniqueChr = set(password)
        result = 0

        for ch in uniqueChr:
            if ch.islower():
                result += 1
            elif ch.isupper():
                result += 2
            elif ch.isdigit():
                result += 3
            elif ch in fivePoint:
                result += 5

        return result