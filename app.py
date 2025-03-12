import streamlit as st
import pickle
import numpy as np
import requests

# Load the trained model
with open("metal_price_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Function to fetch real-time USD to INR conversion rate
def get_usd_to_inr():
    try:
        response = requests.get("https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD")  # Replace with your API key
        data = response.json()
        return data["conversion_rates"]["INR"]
    except:
        return 83.02  # Default to latest INR rate if API fails

# Streamlit UI
st.set_page_config(page_title="Metal Price Forecasting", page_icon="🔮", layout="wide")

st.sidebar.header("🔢 Enter Metal Prices")
gold_price = st.sidebar.number_input("Gold Price (USD)", min_value=0.0, value=1800.0, step=10.0)
nickel_price = st.sidebar.number_input("Nickel Price (USD)", min_value=0.0, value=15000.0, step=100.0)
silver_price = st.sidebar.number_input("Silver Price (USD)", min_value=0.0, value=25.0, step=1.0)
uranium_price = st.sidebar.number_input("Uranium Price (USD)", min_value=0.0, value=50.0, step=1.0)
inflation_rate = st.sidebar.number_input("Inflation Rate (%)", min_value=0.0, value=2.5, step=0.1)

# Ensure model input matches training data (e.g., 8 features expected)
# Add placeholders if needed (modify as per training data)
year = 2025  # Placeholder value
month = 3  # Placeholder value
aluminum_price = 2500  # Placeholder value

# Prediction Button
if st.sidebar.button("🔍 Predict Price"):
    try:
      
        # Prepare input features (must match model training data)
        input_features = np.array([[gold_price, nickel_price, silver_price, uranium_price, inflation_rate]])
        
        # Model Prediction
        predicted_price_usd = model.predict(input_features)[0]

        # Convert to INR
        usd_to_inr = get_usd_to_inr()
        predicted_price_inr = predicted_price_usd * usd_to_inr

        # Display results
        st.markdown("## 🔮 Metal Price Forecasting App")
        st.success(f"🟢 **Predicted Gold Price (Inflation Adjusted)**: **${predicted_price_usd:.2f}** (USD)")
        st.info(f"💰 **Converted Price in INR**: **₹{predicted_price_inr:.2f}** (INR)")
    
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# Footer
st.markdown("---")
st.markdown("Developed by **Shital Chavan** | Powered by **Machine Learning 🤖**")
