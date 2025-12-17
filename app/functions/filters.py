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

def filter_exact(df: pd.DataFrame,
                 column : str,
                 values : List[str]
                 ) -> pd.DataFrame:
    """ Filter df by category column """
    return df[df[column].isin(values)]

def filter_mapping(df : pd.DataFrame, 
                   column : str,
                   values : List[str],
                   mapping_dict : Dict[str, List[str]]
                ) -> pd.DataFrame:
    """ Handle columns with concatenated values (e.g. console : ['PC|PS4']) """
    
    mask = pd.Series(False, index=df.index)

    for value in values:
        mapped_values = mapping_dict.get(value, [value])
        for m_value in mapped_values:
            mask |= df[column].str.contains(m_value, na=False)

    return df[mask]
