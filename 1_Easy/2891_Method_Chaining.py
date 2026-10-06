"""
LeetCode: 2891
Title: Method Chaining
Difficulty: Easy

"""

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight'] > 100].sort_values(['weight'],ascending=False)[['name']]
