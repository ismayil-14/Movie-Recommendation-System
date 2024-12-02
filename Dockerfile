# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the ports for both Flask API and Streamlit
EXPOSE 5000
EXPOSE 8501

# Run both Flask and Streamlit apps in parallel
CMD ["sh", "-c", "flask run --port=5000 & streamlit run s_app.py --server.port 8501"]
