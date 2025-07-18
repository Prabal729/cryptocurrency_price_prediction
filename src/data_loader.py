import pandas as pd

def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Load raw CoinGecko CSV data.
    Args:
        file_path: Path to the CSV file
    Returns:
        DataFrame with raw data
    """
