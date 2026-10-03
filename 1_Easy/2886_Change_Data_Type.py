"""
LeetCode: 2886
Title: Change Data Type
Difficulty: Easy

"""

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
