import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and features
model = joblib.load(r"D:\portfolio\cryptocurrency_price_prediction\models\final_xgboost_model.pkl")
features = joblib.load(r"D:\portfolio\cryptocurrency_price_prediction\models\feature_columns.pkl")
st.set_page_config(page_title="Crypto Liquidity Predictor", layout="wide")
st.title("🚀 Cryptocurrency Liquidity Prediction (XGBoost Model)")

# User input
st.sidebar.header("📥 Input Features")
user_input = {}

for feature in features:
    user_input[feature] = st.sidebar.number_input(f"{feature}", value=0.0)

if st.button("Predict Liquidity"):
    input_df = pd.DataFrame([user_input])
    prediction = model.predict(input_df)[0]
    st.success(f"💸 Predicted Liquidity: **{prediction:,.2f}**")
