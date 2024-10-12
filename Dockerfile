# Use an official Python 3.9 runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container, including the models directory
COPY . /app/

# Expose port 8501 for Streamlit and 8000 for FastAPI
EXPOSE 8501
EXPOSE 8000

# Run both FastAPI and Streamlit
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run app/app.py --server.port 8501 --server.address 0.0.0.0"]


