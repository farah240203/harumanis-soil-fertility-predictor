import streamlit as st
import pandas as pd
import joblib
import requests
from database_config import get_latest_sensor_data

# Load model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="Harumanis Vegetative Stage Soil Fertility Predictor", layout="centered")

# Enhanced Styling
st.markdown("""
    <style>
        html, body, .main {
            background-color: #f4f9f4;
            font-family: 'Segoe UI', sans-serif;
        }
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }
        h1 {
            color: #1b5e20;
            text-align: center;
            font-size: 2.5rem;
        }
        .stRadio > label {
            font-weight: 600;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 0.6em 1.5em;
            border-radius: 10px;
            border: none;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        .stButton > button:hover {
            background-color: #388e3c;
            transform: scale(1.02);
            transition: 0.2s ease-in-out;
        }
        .stNumberInput label, .stSubheader {
            color: #2e7d32;
            font-weight: 600;
        }
        .footer {
            text-align: center;
            color: #888;
            font-size: 0.9em;
            padding: 1.5rem 0 0.5rem 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌿 Harumanis Vegetative Stage Soil Fertility Predictor")
st.markdown("""
<p style="text-align: center; color: #555;"> Predict soil fertility for Harumanis mango cultivation using machine learning based on key soil and environmental parameters.
</p>
""", unsafe_allow_html=True)

# Mode Selector
mode = st.radio("Select Input Mode", ["📋 Manual Input", "📡 Sensor Connected (IoT)", "🌐 Connect via Sensor API"])

st.divider()

# Prediction Function
def get_prediction(input_data):
    prediction = model.predict([input_data])
    return "Fertile 🌱" if prediction[0] == 1 else "Not Fertile ❌"

# Manual Input Mode
if mode == "📋 Manual Input":
    st.subheader("📝 Enter Soil Properties")
    col1, col2 = st.columns(2)
    with col1:
        nitrogen = st.number_input("Nitrogen (N)", min_value=0.0)
        phosphorus = st.number_input("Phosphorus (P)", min_value=0.0)
        potassium = st.number_input("Potassium (K)", min_value=0.0)
    with col2:
        temperature = st.number_input("Temperature (°C)", min_value=0.0)
        humidity = st.number_input("Humidity (%)", min_value=0.0)

    if st.button("🔍 Predict Fertility"):
        features = [nitrogen, phosphorus, potassium, temperature, humidity]
        result = get_prediction(features)
        st.markdown(f"""
            <div style='padding: 1rem; background-color: #e8f5e9; border-radius: 10px; 
                        text-align: center; font-size: 1.2rem; font-weight: bold; color: #1b5e20;'>
                🧪 Predicted Fertility Level: {result}
            </div>
        """, unsafe_allow_html=True)

# IoT Sensor Input Mode (from database)
elif mode == "📡 Sensor Connected (IoT)":
    st.markdown("### 📡 Latest IoT Sensor Readings", unsafe_allow_html=True)
    data = get_latest_sensor_data()
    if data:
        st.json(data)
        if st.button("🔍 Predict from Sensor Data"):
            features = [data['N'], data['P'], data['K'], data['temperature'], data['humidity']]
            result = get_prediction(features)
            st.markdown(f"""
                <div style='padding: 1rem; background-color: #e8f5e9; border-radius: 10px; 
                            text-align: center; font-size: 1.2rem; font-weight: bold; color: #1b5e20;'>
                    🧪 Predicted Fertility Level: {result}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No sensor data available. Please check the connection.")

# New: Custom Sensor API Mode
else:
    st.subheader("🌐 Connect Your Sensor via API")
    api_url = st.text_input("Paste your sensor's API endpoint URL here (must return JSON with keys: N, P, K, temperature, humidity)")

    if api_url and st.button("Fetch Sensor Data and Predict"):
        try:
            response = requests.get(api_url, timeout=5)
            response.raise_for_status()
            data = response.json()

            st.write("📊 Live Sensor Data:", data)

            try:
                features = [
                    float(data['N']),
                    float(data['P']),
                    float(data['K']),
                    float(data['temperature']),
                    float(data['humidity'])
                ]
                result = get_prediction(features)
                st.markdown(f"""
                    <div style='padding: 1rem; background-color: #e8f5e9; border-radius: 10px; 
                                text-align: center; font-size: 1.2rem; font-weight: bold; color: #1b5e20;'>
                        🧪 Predicted Fertility Level: {result}
                    </div>
                """, unsafe_allow_html=True)
            except KeyError:
                st.error("API response is missing required fields: N, P, K, temperature, humidity.")
            except ValueError:
                st.error("API returned invalid data types for features.")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch sensor data: {e}")

st.divider()

# Footer
st.markdown("""
    <div class='footer'>
        © 2025 Harumanis Soil Intelligence System · Designed for research & agricultural innovation.
    </div>
""", unsafe_allow_html=True)
