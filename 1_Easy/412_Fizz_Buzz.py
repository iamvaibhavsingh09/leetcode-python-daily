"""
LeetCode: 412
Title: Fizz Buzz
Difficulty: Easy

"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        newList = list()
        for var in range(1,n+1):
            if (var % 3 ==0) and (var % 5 == 0):
                newList.append('FizzBuzz')
            elif (var % 5 == 0):
                newList.append('Buzz')
            elif (var % 3 ==0):
                newList.append('Fizz')
            else:
                newList.append(str(var))     
        
        return newList