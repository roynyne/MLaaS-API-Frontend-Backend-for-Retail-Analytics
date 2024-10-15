Sales Revenue Prediction and Forecasting API
==============================

The API implementation for serving time-series and predictive forecasting models is contained in this repository. Real-time forecasts and projections for sales income across several outlets and products are made possible by the API.

### Project Overview

This API serves two purposes:

Predictive API: Provides sales revenue predictions for a given item in a specific store on a given date.
Forecasting API: Predicts total sales revenue for the next 7 days across all stores.

### Repository Structure
------------
        
    ├── README.md               <- The top-level README file containing project overview, installation, and usage instructions.
    ├── app
    │   └── __pycache__         <- Python bytecode cache directory generated after execution.
    │       └── main.cpython-38.pyc <- Compiled Python bytecode for faster execution.
    ├── backend
    │   ├── Dockerfile          <- Dockerfile to build the backend service, setting up the FastAPI environment.
    │   ├── app
    │   │   └── main.py         <- Main script to run the FastAPI application for handling prediction and forecast API requests.
    │   ├── models
    │   │   ├── ARIMA_model.pkl <- Serialized ARIMA model used for time-series forecasting.
    │   │   └── xgboost_model.pkl <- Serialized XGBoost model used for sales revenue prediction.
    │   └── requirements.txt    <- Python dependencies for the backend service, specifying the libraries required for FastAPI, model           loading, and prediction.
    ├── docker-compose.yml      <- Configuration for Docker Compose, defining services for backend and frontend.
    ├── frontend
    │   ├── Dockerfile          <- Dockerfile to build the frontend service, setting up the Streamlit environment.
    │   ├── app
    │   │   └── app.py          <- Main script to run the Streamlit application for visualizing predictions and forecasts.
    │   ├── models
    │   │   ├── ARIMA_model.pkl <- Serialized ARIMA model for use in the frontend visualization.
    │   │   └── xgboost_model.pkl <- Serialized XGBoost model for use in the frontend visualization.
    │   └── requirements.txt    <- Python dependencies for the frontend service, specifying the libraries required for Streamlit and model interaction.
    ├── github.txt              <- Text file containing the GitHub repository link for this project.
    ├── render.txt              <- Text file containing the Frontend & Backend API links.
    └── requirements.txt        <- General requirements file listing shared dependencies for both backend and frontend, used for local setup.

--------

### Installation
------------

1. Clone the repository:

        git clone https://github.com/roynyne/sales-api

        cd sales-revenue-prediction

3. Install the required packages:

        pip install -r requirements.txt

--------

### Installation and Setup
------------

**Prerequisites**

        Docker
        Docker Compose
        FastAPI
        Streamlit

**Render Links**

Frontend (Fast API)
        https://sales-api-frontend.onrender.com/home

Backend (Streamlit)
        https://sales-api-backend-qw48.onrender.com
------------

### Models

The following models are used in the API:

XGBoost: Predictive model for item-store-date sales prediction.
ARIMA: Forecasting models for time-series analysis.
--------

### Contributors
------------

Roy Hegde (roynyne@hotmail.com)

--------
