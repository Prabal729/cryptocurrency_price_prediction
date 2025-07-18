import pandas as pd
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates rolling statistics, time-based features, and percent changes.
    Returns:
        DataFrame with new features
    """
