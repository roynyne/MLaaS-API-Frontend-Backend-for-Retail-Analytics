import streamlit as st
import joblib
import pandas as pd
from datetime import datetime, timedelta

# Load your models
xgb_model = joblib.load('models/xgboost_model.pkl')
arima_model = joblib.load('models/ARIMA_model.pkl')  # Load ARIMA model

# Set up the Streamlit app
st.title("Sales Prediction and Forecasting App")

# XGBoost: Predict sales for a store/item on a given date
st.header("Predict Store/Item Sales")
date = st.date_input("Select date")
store_id = st.number_input("Enter store ID", min_value=0, value=1)
item_id = st.number_input("Enter item ID", min_value=0, value=101)
sell_price = st.number_input("Enter sell price", min_value=0.0, value=10.0)
event_name_encoded = st.number_input("Enter event name encoded", min_value=0, value=2)
event_type_encoded = st.number_input("Enter event type encoded", min_value=0, value=1)

if st.button("Predict Sales"):
    # Preprocess input and predict sales using XGBoost
    input_data = pd.DataFrame({
        'store_id': [store_id],
        'item_id': [item_id],
        'day': [date.day],
        'month': [date.month],
        'weekday': [date.weekday()],
        'sell_price': [sell_price],
        'event_name_encoded': [event_name_encoded],
        'event_type_encoded': [event_type_encoded]
    })
    predicted_sales = xgb_model.predict(input_data)[0]
    st.write(f"Predicted Sales: {round(predicted_sales, 2)}")

# ARIMA: Forecast national sales for the next 7 days
st.header("Forecast National Sales")
forecast_date = st.date_input("Select start date for forecasting")

if st.button("Forecast Sales"):
    # Generate next 7 days based on the selected start date
    future_dates = [forecast_date + timedelta(days=i) for i in range(1, 8)]
    
    # Forecast using the ARIMA model
    arima_forecast = arima_model.forecast(steps=7)
    
    # Prepare the forecasted sales for display
    forecasted_sales = pd.DataFrame({
        'Date': future_dates,
        'Forecasted_Sales': arima_forecast
    })
    
    st.write("Forecasted Sales for the next 7 days:")
    st.dataframe(forecasted_sales)
