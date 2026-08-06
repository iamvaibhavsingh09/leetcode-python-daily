"""
LeetCode: 682
Title: Baseball Game
Difficulty: Easy

"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []

        for op in operations:
            if op == 'C':
                output.pop()
            elif op =='D':
                newOp = int(output[-1])*2
                output.append(newOp)
            elif op == "+":
                newOp = int(output[-1]) + int(output[-2])
                output.append(newOp)
            else:
                output.append(int(op))

        return sum(output)