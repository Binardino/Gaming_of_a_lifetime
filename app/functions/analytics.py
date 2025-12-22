import pandas as pd
from functions.data_wrangling import *

def games_per_console_year(df : pd.DataFrame) -> pd.DataFrame :
    df_gb = (df.groupby(['played_year', 'console'])
              .size()
              .reset_index(name='game_count')
              .sort_values(["played_year", "game_count"], ascending=[True, False])
              )
    
    return df_gb
