from __future__ import annotations
import pandas as pd

def find_null_cols(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[:, df.isnull().any()]

