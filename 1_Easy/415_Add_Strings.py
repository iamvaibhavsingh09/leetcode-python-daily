"""
LeetCode: 415
Title: Add Strings
Difficulty: Easy

"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        result = ""

        while i >= 0 or j >= 0:

            digit1 = 0
            digit2 = 0

            if i >= 0:
                digit1 = int(num1[i])

            if j >= 0:
                digit2 = int(num2[j])

            total = digit1 + digit2 + carry

            digit = total % 10
            carry = total // 10

            result = result + str(digit)

            i = i - 1
            j = j - 1

        if carry > 0:
            result = result + str(carry)

        result = result[::-1]

        return result
