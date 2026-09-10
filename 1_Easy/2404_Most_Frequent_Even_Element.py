"""
LeetCode: 2404
Title: Most Frequent Even Element
Difficulty: Easy

"""

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        newDict = dict()
        answer = -1
        maxCount = 0

        for num in nums:
            if num % 2 == 0:
                if num in newDict:
                    var = newDict[num]
                    newDict[num] += var
                else:
                    newDict[num] = 1


        for key,value in newDict.items():
            if value > maxCount:
                maxCount = value
                answer = key

            elif value == maxCount and key < answer:
                answer = key
        
        return answer
