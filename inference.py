import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and encoder
# Ensure these files are in the same directory as this script or provide the full path
try:
    model_pipeline = joblib.load('crop_recommendation_model.joblib')
    encoder = joblib.load('crop_encoder.joblib')
except FileNotFoundError:
    st.error("Error: Model or encoder file not found. Please ensure 'crop_recommendation_model.joblib' and 'crop_encoder.joblib' are in the correct directory.")
    st.stop()

st.set_page_config(page_title="Crop Recommendation System", layout="centered")

st.title("🌾 Crop Recommendation System")
st.markdown("Enter the environmental parameters to get a crop recommendation.")

# Input widgets for environmental parameters
st.sidebar.header("Environmental Parameters")

N = st.sidebar.slider("Nitrogen (N)", 0, 140, 70)
P = st.sidebar.slider("Phosphorus (P)", 5, 145, 75)
K = st.sidebar.slider("Potassium (K)", 5, 205, 105)
temperature = st.sidebar.slider("Temperature (°C)", 0.0, 45.0, 25.0, 0.1)
humidity = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 60.0, 0.1)
ph = st.sidebar.slider("pH Value", 0.0, 14.0, 6.5, 0.1)
rainfall = st.sidebar.slider("Rainfall (mm)", 20.0, 300.0, 150.0, 0.1)

# Create a DataFrame from the input values
input_data = pd.DataFrame([{
    'Nitrogen': N,
    'Phosphorus': P,
    'Potassium': K,
    'Temperature': temperature,
    'Humidity': humidity,
    'pH_Value': ph,
    'Rainfall': rainfall
}])

st.subheader("Input Parameters:")
st.write(input_data)

if st.button("Predict Crop"):
    try:
        # Make prediction using the loaded model pipeline
        prediction_encoded = model_pipeline.predict(input_data)

        # The model directly predicts the crop name (string label)
        predicted_crop = prediction_encoded[0]

        st.success(f"The recommended crop is: **{predicted_crop}**")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
