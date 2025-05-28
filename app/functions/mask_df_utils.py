from functions.visualisation_tools import create_mask

def apply_all_masks(df, filters, dict_console=None, dict_genre=None):
    """
    Apply all masks to a dataframe based on filters.
    Assumes standard column names. Adjust if needed per dataset.

    Args:
        df (DataFrame): The data to filter.
        filters (dict): Output from create_sidebar_widgets().
        dict_console (dict): Mapping for console names.
        dict_genre (dict): Mapping for genre names.

    Returns:
        DataFrame: Filtered DataFrame.
    """
    mask_console = create_mask(df, "console", filters["console"], dict_console)
    mask_genre = create_mask(df, "game_type", filters["genre"], dict_genre)
    mask_hours = df["hours_played"].between(*filters["hours"])
    mask_score = df["perso_score"].between(*filters["score"])
    mask_finish = df["finished"].isin(filters["finish"])

    return df[
        mask_console & mask_genre & mask_hours & mask_score & mask_finish
    ].reset_index(drop=True)
