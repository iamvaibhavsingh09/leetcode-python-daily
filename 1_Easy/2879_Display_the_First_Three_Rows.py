"""
LeetCode: 2879
Title: Display the First Three Rows
Difficulty: Easy

"""

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.loc[:2]
