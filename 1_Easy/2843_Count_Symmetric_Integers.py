"""
LeetCode: 2843
Title: Count Symmetric Integers
Difficulty: Easy

"""

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        output = 0


        for i in range(low,high+1):
            if len(str(i)) % 2 == 0:
                length = len(str(i))
                mid = length //2 
                firstDigit = str(i)[:mid]
                lastDigit = str(i)[mid:]
                first = 0
                for fd in firstDigit:
                    first += int(fd) 
                last = 0
                for ld in lastDigit:
                    last += int(ld)
                
                if first == last:
                    output += 1
                
        return output