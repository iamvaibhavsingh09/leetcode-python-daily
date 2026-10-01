"""
LeetCode: 2881
Title: Create a New Column
Difficulty: Easy

"""

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees