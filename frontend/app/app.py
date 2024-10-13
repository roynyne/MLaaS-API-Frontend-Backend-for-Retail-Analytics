import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta

# Set the FastAPI base URL (replace with your actual FastAPI URL)
FASTAPI_URL = "https://sales-api-backend-qw48.onrender.com"

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
    # Create the query parameters for the FastAPI request
    params = {
        "date": date.strftime("%Y-%m-%d"),
        "store_id": store_id,
        "item_id": item_id,
        "sell_price": sell_price,
        "event_name_encoded": event_name_encoded,
        "event_type_encoded": event_type_encoded,
    }
    
    # Make a GET request to the FastAPI endpoint
    response = requests.get(f"{FASTAPI_URL}/sales/stores/items/", params=params)
    
    if response.status_code == 200:
        # Extract the predicted sales from the response
        predicted_sales = response.json()["prediction"]
        st.write(f"Predicted Sales: {round(predicted_sales, 2)}")
    else:
        st.write("Error in prediction. Please check the inputs or try again.")

# ARIMA: Forecast national sales for the next 7 days
st.header("Forecast National Sales")
forecast_date = st.date_input("Select start date for forecasting")

if st.button("Forecast Sales"):
    # Prepare the query parameters for the FastAPI request
    params = {
        "date": forecast_date.strftime("%Y-%m-%d")
    }
    
    # Make a GET request to the FastAPI forecast endpoint
    response = requests.get(f"{FASTAPI_URL}/sales/national/", params=params)
    
    if response.status_code == 200:
        # Extract the forecasted sales from the response
        forecasted_sales = response.json()
        forecast_df = pd.DataFrame(list(forecasted_sales.items()), columns=['Date', 'Forecasted Sales'])
        st.write("Forecasted Sales for the next 7 days:")
        st.dataframe(forecast_df)
    else:
        st.write("Error in forecasting. Please try again.")
