"""
LeetCode: 1773
Title: Count Items Matching a Rule
Difficulty: Easy

"""

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        itemType = {'type': 0,'color': 1,'name': 2}
        output = 0

        index = itemType[ruleKey]

        for item in items:
            if item[index] == ruleValue:
                output += 1 

        return output
