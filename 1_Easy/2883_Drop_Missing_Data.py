"""
LeetCode: 2883
Title: Drop Missing Data
Difficulty: Easy

"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='name')