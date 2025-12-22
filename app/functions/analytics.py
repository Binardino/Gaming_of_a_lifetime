import pandas as pd
from functions.data_wrangling import *

def games_per_console_year(df : pd.DataFrame) -> pd.DataFrame :
    df_gb = (df.groupby(['played_year', 'console'])
              .size()
              .reset_index(name='game_count')
              .sort_values(["played_year", "game_count"], ascending=[True, False])
              )
    
    return df_gb

def games_per_console_and_brand(df: pd.DataFrame) -> pd.DataFrame:
        """Compute amount of games per console and brand"""
        df_temp = df.copy()
        df_temp = add_console_tag(df_temp)

        df_console_brand =(df_temp.groupby(['console', 'brand'])
                                  .size()
                                  .reset_index(name='game_count')
                                  .sort_values('game_count', ascending=False)
                                  )
        
        return df_console_brand


def hours_by_console(df : pd.DataFrame) -> pd.DataFrame :
    df_gb_hours = (df.groupby("console")["hours_played"]
                     .sum()
                     .sort_values(ascending=False)
                     .reset_index()
                     )
                    
    return df_gb_hours
