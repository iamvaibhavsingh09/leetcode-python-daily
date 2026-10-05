"""
LeetCode: 2889
Title: Reshape Data: Pivot
Difficulty: Easy

"""

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
