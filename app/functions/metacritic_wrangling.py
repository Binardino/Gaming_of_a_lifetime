import re
import pandas as pd
from rapidfuzz import fuzz, process

_LEADING_ARTICLES = re.compile(r'^(the|a|an)\s+', re.IGNORECASE)
_PUNCTUATION = re.compile(r'[^\w\s]')

def normalize_title(name: str) -> str:
    """Lowercase, strip punctuation, remove leading articles (the/a/an)."""
    name = name.lower().strip()
    name = _PUNCTUATION.sub('', name)
    name = _LEADING_ARTICLES.sub('', name)
    return name.strip()


def fuzzymatch_metacritic(row: str, game_column: pd.Series, threshold: int = 85) -> tuple[str, int]:
    """
    Find the best match for a game title in a list of candidates.

    Uses token_sort_ratio to handle word-order variations
    (e.g. 'Witcher 3, The' vs 'The Witcher 3').

    Returns:
        (best_match_original_title, score) if score >= threshold
        ("", 0) otherwise
    """
    row_norm = normalize_title(row)
    candidates_norm = game_column.map(normalize_title)

    result = process.extractOne(
        row_norm,
        candidates_norm,
        scorer=fuzz.token_sort_ratio,
        score_cutoff=threshold,
    )

    if result is None:
        return ("", 0)

    best_norm, score, idx = result
    return (game_column.iloc[idx], score)
