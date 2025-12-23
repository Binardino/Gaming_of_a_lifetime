import pandas as pd
from functions.data_wrangling import *

def games_per_console_year(df : pd.DataFrame) -> pd.DataFrame :
    """Compute amount of played games per console per year """
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


def games_per_type(df: pd.DataFrame) -> pd.DataFrame :
     """ Compute group by - count() of games - per type of games """
     df_temp = df[['game_type']].copy()

     df_temp['game_type'] = df_temp['game_type'].str.split('|')
     df_temp = df_temp.explode('game_type')

     df_games_per_type = (df_temp.groupby('game_type')
                          .size()
                          .reset_index(name='game_count')
                          .sort_values('game_count', ascending=False)
          
     )
     
     return df_games_per_type

def games_per_console_year_pct(df : pd.DataFrame) -> pd.DataFrame :
    df_year = (
          df.groupby(['played_year', 'console'])
          .size()
          .reset_index(name='game_count')
     )

    df_console_year_pivot = pd.pivot(data=df_year,
                            index='played_year',
                            columns='console',
                            values='console_count'
                            ).fillna(0)

    return df_console_year_pivot.div(df_console_year_pivot.sum(axis=1), axis=0)

def hours_by_console(df : pd.DataFrame) -> pd.DataFrame :
    df_gb_hours = (df.groupby("console")["hours_played"]
                     .sum()
                     .sort_values(ascending=False)
                     .reset_index()
                     )
                    
    return df_gb_hours

def score_per_hour(df : pd.DataFrame) -> pd.DataFrame:
     """ Compute persoanal score per hour played for each game """

     df_score = df[df['hours_played'].notna() & (df['hours_played'] > 0)].copy()

     df_score['score_per_hour'] = (df_score['perso_score'] / df_score['hours_played'])

     return df_score