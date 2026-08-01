"""
LeetCode: 1108
Title: Defanging an IP Address
Difficulty: Easy

"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        newList =[]
        for add in address:
            if add == '.':
                newList.append('[.]')
            else:
                newList.append(add)

        return ''.join(newList)
