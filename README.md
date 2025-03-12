##🔮 Metal Price Forecasting App

A Machine Learning application that predicts future metal prices based on historical trends and inflation rates.

📌 Overview

This project is built using Python, Streamlit, and Machine Learning models to forecast metal prices for Gold, Nickel, Silver, and Uranium. It considers historical price data and adjusts predictions based on inflation rates.

The model is trained using Random Forest Regression, providing insights into metal price trends and aiding financial decision-making.

⚙️ Technologies Used

Python 🐍
Pandas & NumPy 📊
Scikit-Learn 🤖
Streamlit 🌐
Matplotlib & Seaborn 📉

🚀 Features

✅ Predicts future metal prices based on historical data
✅ Adjusts prices considering inflation trends
✅ Provides predictions in both USD & INR 💰
✅ Interactive UI for easy input and analysis

📂 Project Structure

/forecasting
│── data/
│   ├── alum_gold_nickel_silver_uran_price_changes.csv  # Historical metal price dataset
│── models/
│   ├── metal_price_model.pkl                           # Trained Machine Learning Model
│── app.py                                             # Streamlit Web App
│── requirements.txt                                   # Dependencies for the project
│── README.md                                          # Project Documentation

📈 Dataset

Source: Historical metal price data from 1992-2021
Target Variable: Future Gold Price (Inflation-Adjusted)
Features:
Gold, Nickel, Silver, Uranium Prices
Inflation Rate
Year & Month

📊 Model Details

Algorithm: Random Forest Regressor 🌲
Performance: High Accuracy on Test Data
Inflation Adjustment: Price Predictions reflect inflation impact

⚡ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/shital8580/metal-price-forecast.git
cd metal-price-forecast

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit Web App
streamlit run app.py

📡 Deployment

The model can be deployed on Streamlit Cloud, Heroku, or AWS.

🚀 Deploy to Streamlit Cloud

Push the project to GitHub
Go to Streamlit Cloud
Deploy by selecting your repository

👩‍💻 Author
📌 Shital Chavan
📧 shital8580@gmail.com
🔗 GitHub: shital8580
