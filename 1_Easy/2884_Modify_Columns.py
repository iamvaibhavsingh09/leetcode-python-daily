"""
LeetCode: 2884
Title: Modify Columns
Difficulty: Easy

"""

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return emp