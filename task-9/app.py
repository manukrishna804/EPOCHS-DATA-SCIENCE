import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

# -------------------------------------------------
# Load Files
# -------------------------------------------------
BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "car_price_model.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "feature_columns.pkl"))
df = pd.read_csv(os.path.join(BASE_DIR, "cardekho_dataset.csv"))

# Remove unwanted column if present
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# -------------------------------------------------
# Title
# -------------------------------------------------
st.title("🚗 Car Price Prediction")
st.markdown("Predict the selling price of a used car using Machine Learning.")

st.divider()

# -------------------------------------------------
# Numeric Inputs
# -------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    vehicle_age = st.number_input(
        "Vehicle Age (Years)",
        min_value=0,
        max_value=30,
        value=5
    )

    km_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        value=50000
    )

    mileage = st.number_input(
        "Mileage (km/l)",
        min_value=0.0,
        value=18.0
    )

with col2:
    engine = st.number_input(
        "Engine (CC)",
        min_value=500,
        value=1200
    )

    max_power = st.number_input(
        "Max Power (bhp)",
        min_value=20.0,
        value=80.0
    )

    seats = st.number_input(
        "Seats",
        min_value=2,
        max_value=10,
        value=5
    )

st.divider()

# -------------------------------------------------
# Dropdowns
# -------------------------------------------------

car_names = sorted(df["car_name"].unique())
brands = sorted(df["brand"].unique())
models = sorted(df["model"].unique())

seller_types = sorted(df["seller_type"].unique())
fuel_types = sorted(df["fuel_type"].unique())
transmission_types = sorted(df["transmission_type"].unique())

car_name = st.selectbox("Car Name", car_names)
brand = st.selectbox("Brand", brands)
model_name = st.selectbox("Model", models)

seller_type = st.selectbox("Seller Type", seller_types)
fuel_type = st.selectbox("Fuel Type", fuel_types)
transmission_type = st.selectbox("Transmission", transmission_types)

st.divider()

# -------------------------------------------------
# Prediction
# -------------------------------------------------

if st.button("🚀 Predict Selling Price", use_container_width=True):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    # Numerical Features
    input_df["vehicle_age"] = vehicle_age
    input_df["km_driven"] = km_driven
    input_df["mileage"] = mileage
    input_df["engine"] = engine
    input_df["max_power"] = max_power
    input_df["seats"] = seats

    # One-Hot Encoding

    mappings = {
        f"car_name_{car_name}": 1,
        f"brand_{brand}": 1,
        f"model_{model_name}": 1,
        f"seller_type_{seller_type}": 1,
        f"fuel_type_{fuel_type}": 1,
        f"transmission_type_{transmission_type}": 1,
    }

    for column, value in mappings.items():
        if column in input_df.columns:
            input_df[column] = value

    prediction = model.predict(input_df)[0]

    st.success("### 💰 Estimated Selling Price")

    st.metric(
        label="Predicted Price",
        value=f"₹ {prediction:,.0f}"
    )

    st.balloons()

st.divider()

st.caption("Developed by Manu Krishna | Epochs '26 Assignment 9")