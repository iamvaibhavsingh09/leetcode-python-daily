"""
LeetCode: 2887
Title: Fill Missing Data
Difficulty: Easy

"""

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products
