"""
LeetCode: 1470
Title: Shuffle the Array
Difficulty: Easy

"""

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        left = 0
        right = n

        for i in range(2*n):
            if i % 2 != 0:
                output.append(nums[right])
                right +=1
            else:
                output.append(nums[left])
                left += 1

        return output
