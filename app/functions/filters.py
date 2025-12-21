import pandas as pd
from typing import Dict, List, Tuple, Any

filters = Dict[str, Any]

def filter_range(df          : pd.DataFrame,
                 column      : str,
                 value_range : Tuple[int,int]
                 ) -> pd.DataFrame:
    """Filter df by range of numeric values"""
    min_val, max_val = value_range
    return df[df[column].between(min_val, max_val)]

def filter_exact(df          : pd.DataFrame,
                 column      : str,
                 values      : List[str]
                 ) -> pd.DataFrame:
    """ Filter df by category column """
    return df[df[column].isin(values)]

def filter_mapping(df           : pd.DataFrame,
                   column       : str,
                   values       : List[str],
                   mapping_dict : Dict[str, List[str]]
                ) -> pd.DataFrame:
    """ Handle columns with concatenated values (e.g. console : ['PC|PS4']) """
    
    mask = pd.Series(False, index=df.index)

    for value in values:
        mapped_values = mapping_dict.get(value, [value])
        for m_value in mapped_values:
            mask |= df[column].str.contains(m_value, na=False)

    return df[mask]

   
def apply_filters(df           : pd.DataFrame, 
                  filters      : Dict[str, Any], 
                  dict_console : Dict[str, List[str]],
                  dict_genre   : Dict[str, List[str]]
                ) -> pd.DataFrame:
    """ Apply all business filters to the input df 
    Output filtered_df for sidebars 
    
    As each filter has its own logic, 
    more futureproof to have one if condition per filter
    
    Output : df_filtered[mask] - df_filter with all filters applied """

    df_filtered = df.copy()

    #console - mapping filter
    if filters.get('f_console'):
        df_filtered = filter_mapping(
            df_filtered,
            column='console',
            values=filters['f_console'],
            mapping_dict=dict_console
        )

    #played hours - range filter
    if filters.get('f_hours_played'):
        df_filtered = filter_range(
            df_filtered,
            column='hours_played',
            value_range=filters['f_hours_played']
            )
        
    #personal score - range filter
    if filters.get('f_perso_score'):
        df_filtered = filter_range(
            df_filtered,
            column='perso_score',
            value_range=filters["f_perso_score"],
        )        

    #finished - exact match
    if filters.get('f_finish'):
        df_filtered = filter_exact(
            df_filtered,
            column='finished',
            values=filters["f_finish"],
        )

    #genre - mapping filter
    if filters.get('f_genre'):
        df_filtered = filter_mapping(
            df_filtered,
            column='game_type',
            values=filters['f_genre'],
            mapping_dict=dict_genre
        )

    #country - mapping filter
    if filters.get('f_country'):
        df_filtered = filter_exact(
            df_filtered,
            column='country_dev',
            values=filters['f_country']
        )

    #studio - mapping filter
    if filters.get('f_studio'):
        df_filtered = filter_exact(
            df_filtered,
            column='studio',
            values=filters['f_studio']
        )

    #editor - mapping filter
    if filters.get('f_editor'):
        df_filtered = filter_exact(
            df_filtered,
            column='editor',
            values=filters['f_editor']
        )

    return df_filtered
