# 📊 Cryptocurrency Liquidity Prediction Project

This project aims to predict the **liquidity** (measured via price or volume) of various cryptocurrencies using historical data from CoinGecko. It applies machine learning techniques—especially **XGBoost regression**—to forecast cryptocurrency behavior and identify potential market instability due to liquidity risks.

---

## 🚀 Project Objective

The goal is to build a robust ML pipeline that:
- Ingests and preprocesses real-world cryptocurrency data
- Performs Exploratory Data Analysis (EDA)
- Engineers informative features (e.g., rolling stats, time features)
- Selects, tunes, and evaluates multiple regression models
- Deploys the best model locally using **Streamlit**
- Provides insights into model performance and prediction reliability

---

## 🗂️ Project Structure

cryptocurrency_price_prediction/
├── data/
│ ├── raw/ # Raw CSVs from CoinGecko
│ └── processed/ # Cleaned and feature-processed files
├── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_eda.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_model_selection.ipynb
│ ├── 05_model_training.ipynb
├── src/
│ ├── data_loader.py
│ ├── data_processor.py
│ ├── feature_engineer.py
│ ├── models.py
│ └── evaluator.py
│ 
├── models/
│ ├── final_xgboost_model.pkl
│ ├── feature_columns.pkl
├── deployment/
│ ├── app.py # Streamlit app for testing
│ └── requirements.txt
├── reports/
│ ├── eda_report.pdf
│ ├── hld_document.pdf
│ ├── lld_document.pdf
│ ├── pipeline_architecture.pdf
│ └── final_report.pdf
└── README.md


---

## 🧠 Machine Learning Workflow

### ✅ Feature Engineering
- Time-based features: year, month, day\_of\_week, quarter
- Volatility: % change over 1h, 24h, 7d
- Aggregated stats: rolling mean, min, max (future-proof for extension)

### ✅ Model Selection
- Compared Linear Regression, Ridge, Lasso, Random Forest, LightGBM, and XGBoost
- Used RMSE, MAE, and R² as evaluation metrics
- **XGBoost** selected as final model

### ✅ Hyperparameter Tuning
- Used `GridSearchCV` and `RandomizedSearchCV`
- Outcome: tuning did not always improve metrics—highlighting the importance of baseline performance checks

---

## 📈 Results

| Metric | Before Tuning | After Tuning |
|--------|---------------|--------------|
| MAE    | 1730.02       | **1211.72**  |
| RMSE   | 6870.40       | **5203.52**  |
| R²     | -0.8996       | **-0.0897**  |

*Insight: Hyperparameter tuning helped but gains were modest due to data limitations.*

---

## 💻 Local Deployment

Launch the Streamlit app:
```bash
streamlit run deployment/app.py
