from xgboost import XGBRegressor
import pandas as pd

def train_model(X: pd.DataFrame, y: pd.Series) -> XGBRegressor:
    """
    Trains XGBoost model on given features and labels.
    Returns:
        Trained XGBoost model
    """
