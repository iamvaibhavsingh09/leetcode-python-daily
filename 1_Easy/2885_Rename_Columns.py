"""
LeetCode: 2885
Title: Rename Columns
Difficulty: Easy

"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns = {'id':'student_id','first':'first_name',
                                        'last':'last_name','age':'age_in_years'})
