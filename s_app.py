import streamlit as st
import requests
import pickle
import numpy as np

st.title("XGBoost Model Predictor")
st.write("Enter two inputs to get the prediction from the XGBoost model.")

input1 = st.number_input("User ID:", value=0.0)
input2 = st.number_input("Item ID:", value=0.0)

# Button to trigger API call
if st.button("Get Prediction"):
    # API call
    try:
        response = requests.post(
            "http://host.docker.internal:5000/predict",  # Flask API endpoint
            json={"input1": input1, "input2": input2}
        )
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Error: {e}")
