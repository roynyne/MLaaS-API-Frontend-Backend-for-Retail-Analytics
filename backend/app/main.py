from fastapi import FastAPI
from starlette.responses import JSONResponse
from joblib import load
import pandas as pd
import joblib
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
import numpy as np

# Initialize FastAPI
app = FastAPI()

# Set allowed origins for CORS (change to your frontend URL if needed)
origins = [
    "http://localhost:8501",  # Streamlit frontend running locally
    "https://sales-api-frontend.onrender.com",  # Replace with actual Render frontend URL
]

# Add CORS middleware to the app to allow communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load pre-trained models
xgb_model = load('models/xgboost_model.pkl')
arima_model = joblib.load('models/ARIMA_model.pkl')  # Load the ARIMA model

# Preprocessing Function for XGBoost (adjust based on your features)
def preprocess_input(store_id: int, item_id: int, sell_price: float, date: str, event_name_encoded: int, event_type_encoded: int):
    # Convert the input date to a datetime object
    prediction_date = datetime.strptime(date, "%Y-%m-%d")

    # Extract day, month, weekday from the date
    day = prediction_date.day
    month = prediction_date.month
    weekday = prediction_date.weekday()

    # Prepare features for prediction (this matches the feature set for XGBoost training)
    features = {
        'store_id': [store_id],
        'item_id': [item_id],
        'day': [day],
        'month': [month],
        'weekday': [weekday],
        'sell_price': [sell_price],
        'event_name_encoded': [event_name_encoded],
        'event_type_encoded': [event_type_encoded],
    }

    return pd.DataFrame(features)

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Sales Prediction API. Use /sales/stores/items/ for item-based predictions or /sales/national/ for national sales forecasts."
    }

# Healthcheck endpoint
@app.get("/health")
def healthcheck():
    return {"status": "XGBoost and ARIMA models are ready to go!"}

# Prediction for a specific store and item using XGBoost
@app.get("/sales/stores/items/")
def predict_sales_store_item(date: str, store_id: int, item_id: int, sell_price: float, event_name_encoded: int, event_type_encoded: int):
    try:
        # Preprocess the input data
        input_data = preprocess_input(store_id, item_id, sell_price, date, event_name_encoded, event_type_encoded)

        # Make a prediction using the XGBoost model
        predicted_sales = xgb_model.predict(input_data)[0]

        # Convert float32 to a regular Python float
        predicted_sales = float(predicted_sales)

        # Return the prediction as a JSON response
        return JSONResponse({"prediction": round(predicted_sales, 2)})

    except Exception as e:
        # Log the exception for debugging
        print(f"Error occurred: {e}")
        return JSONResponse({"error": "Internal Server Error"}, status_code=500)


# Forecast total national sales for the next 7 days using ARIMA
@app.get("/sales/national/")
def forecast_national_sales(date: str):
    try:
        # Parse the input date
        start_date = datetime.strptime(date, "%Y-%m-%d")

        # Generate future dates for the next 7 days
        future_dates = [start_date + timedelta(days=i) for i in range(1, 8)]

        # Generate forecast for the next 7 days using ARIMA
        forecast = arima_model.forecast(steps=7)

        # Prepare the forecasted sales with corresponding dates
        forecasted_sales = {
            future_dates[i].strftime('%Y-%m-%d'): round(forecast[i], 2)
            for i in range(7)
        }

        # Return the forecast as a JSON response
        return JSONResponse(forecasted_sales)

    except Exception as e:
        # Log the exception for debugging
        print(f"Error occurred: {e}")
        return JSONResponse({"error": "Internal Server Error"}, status_code=500)
