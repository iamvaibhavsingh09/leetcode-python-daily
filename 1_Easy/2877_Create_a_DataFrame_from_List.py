"""
LeetCode: 2877
Title: Create a DataFrame from List
Difficulty: Easy

"""

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns = ['student_id','age'])
