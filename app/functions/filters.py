import pandas as pd
fro; typing import Dict, List, Tuple, Any

filters = Dict[str, Any]

def filter_range(df : pd.DataFrame,
                 column : str,
                 value_range : Tuple[int,int]
                 ) -> pd.DataFrame:
    """Filter df by range of numeric values"""
    min_val, max_val = value_range
    return df[df[column].between(min_val, max_val)]

