"""
LeetCode: 2469
Title: Convert the Temperature
Difficulty: Easy

"""

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin, fahrenheit = celsius + 273.15, celsius * 1.80 + 32
        ans.extend([kelvin,fahrenheit])
       
        return ans