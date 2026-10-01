"""
LeetCode: 2882
Title: Drop Duplicate Rows
Difficulty: Easy

"""

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset =['email'])