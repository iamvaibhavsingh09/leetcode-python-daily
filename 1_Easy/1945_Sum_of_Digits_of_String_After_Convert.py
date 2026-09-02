"""
LeetCode: 1945
Title: Sum of Digits of String After Convert
Difficulty: Easy

"""

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        newList =[]

        for var in s:
            newList.append(ord(var)- ord('a') + 1)

        while k:
            transition = 0
            for nl in newList:
                for n in str(nl):
                    transition += int(n)
            
            newList = str(transition)
            k -= 1

        return int(newList)
