import pandas as pd
import numpy as np

def import_metacritic(df):
    df_meta = pd.read_csv('metacritic.csv')

    df_join = pd.merge(df, df_meta,
    left_on=df['game_name'],
    right_on=df_meta['gamename'],
    how='left')

    return df_join