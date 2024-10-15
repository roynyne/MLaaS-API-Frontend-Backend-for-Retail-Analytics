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

    git clone <repo_link>
    cd sales-revenue-prediction

2. Install the required packages:

    pip install -r requirements.txt

--------

### Installation and Setup
------------

**Prerequisites**

Docker
Docker Compose
FastAPI
Streamlit

Frontend (Fast API)
https://sales-api-frontend.onrender.com

https://sales-api-backend-qw48.onrender.com

**Predictive Models:**

Notebooks for Ridge and XGBoost models.
1. Located in /notebooks/predictive/.
2. Example: Hegde_Roy-24667610-predictive_ridgexgb.ipynb.
--------

**Forecasting Models:**
------------

Notebooks for ARIMA and Prophet models.
1. Located in /notebooks/forecasting/.
2. Example: Hegde_Roy-24667610-forecasting_ARIMApipeline.ipynb.
--------

### Custom Modules
------------

The custom modules used for data processing, feature engineering, and model training are stored in the /src/ directory. These include:

Model Functions (src/functions/)

    ├── functions
    │   ├── ARIMA           <- Functions to run an ARIMA model.
    │   │   ├── forecast_arima.py
    │   │   ├── main_arima.py
    │   │   └── train_arima.py
    │   ├── Preprocessing           <- Set of functions to load dependencies and preprocessing.
    │   │   ├── create_features.py
    │   │   ├── define_and_split_features_predictive.py
    │   │   ├── evaluate_model_predicitve.py
    │   │   ├── load_data.py
    │   │   └── preprocess_data.py
    │   ├── XGB_Ridge           <- Functions to run both XGB and Ridge Regression model.
    │   │   ├── main_xgb_ridge.py
    │   │   ├── train_ridge.py
    │   │   └── train_xgboost.py
    │   └── prophet           <- Functions to run a Prophet model.
    │       ├── aggregate_sales_forecasting.py
    │       ├── main_forecasting.py
    │       ├── make_forecast.py
    │       └── train_prophet.py

--------

### Models
------------

Trained models are stored in the /models/ folder:

Predictive Models (/models/predictive/): XGBoost model artifact.
Forecasting Models (/models/forecasting/): ARIMA and Prophet models.

--------

### Running the Code
------------

**Run Jupyter Notebooks:**

    Use Jupyter Lab/Notebook to run the notebooks in /notebooks/ for training and evaluating the models.

    Example Command :

    poetry shell
    jupyter notebook

**Loading the Trained Models:**

    The order of the functions can be referred through /notebooks/ for both prediction and forecasting

    The trained models are available in the /models/ folder and can be loaded directly using joblib or pickle.
    use "main_<models>" in the end to run as input for all functions.
--------


### Contributors
------------

Roy Hegde (roynyne@hotmail.com)

--------
