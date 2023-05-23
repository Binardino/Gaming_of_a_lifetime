import pandas as pd
import numpy as np
import difflib 

def import_metacritic(df):
    df_meta = pd.read_csv('metacritic.csv')

    df_join = pd.merge(df, df_meta,
    left_on=df['game_name'],
    right_on=df_meta['gamename'],
    how='left')

    return df_join

# Define a function to find the best match for a given game name
def fuzzymatch_metacritic(game_name, df_vg):
    # Initialize variables to store the best match and its similarity score
    best_match = None
    best_similarity = 0
    
    # Iterate over the game names in df_vg
    for name in df_vg['game_name']:
        # Compute the similarity score between the game names
        similarity = difflib.SequenceMatcher(None, game_name, name).ratio()
        
        # Update the best match if the similarity score is higher than the previous best
        if similarity > best_similarity:
            best_match = name
            best_similarity = similarity
    
    # Check if the similarity score is above the threshold (e.g., 90%)
    if best_similarity >= 0.95:
        return best_match
    else:
        return ""