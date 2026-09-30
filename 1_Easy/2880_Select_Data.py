"""
LeetCode: 2880
Title: Select Data
Difficulty: Easy

"""

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101,['name','age']]
