import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📞",
    layout="wide"
)

# -------------------------------
# Load Model
# -------------------------------
try:
    model = joblib.load("model/model.pkl")
    label_encoders = joblib.load("model/label_encoders.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📊 About")

st.sidebar.info(
"""
### Customer Churn Prediction

This application predicts whether a customer is likely to leave the service.

**Model Used**
- Random Forest Classifier

**Dataset**
- Customer Churn Dataset

**Developed using**
- Python
- Streamlit
- Scikit-Learn
"""
)

# -------------------------------
# Main Title
# -------------------------------
st.title("📞 Customer Churn Prediction")

st.write(
"Enter the customer information below and click **Predict**."
)

st.divider()

# -------------------------------
# Layout
# -------------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        label_encoders["Gender"].classes_
    )

    tenure = st.number_input(
        "Tenure",
        min_value=0,
        value=12
    )

    usage = st.number_input(
        "Usage Frequency",
        min_value=0,
        value=10
    )

    support = st.number_input(
        "Support Calls",
        min_value=0,
        value=2
    )

with col2:

    payment = st.number_input(
        "Payment Delay",
        min_value=0,
        value=5
    )

    subscription = st.selectbox(
        "Subscription Type",
        label_encoders["Subscription Type"].classes_
    )

    contract = st.selectbox(
        "Contract Length",
        label_encoders["Contract Length"].classes_
    )

    spend = st.number_input(
        "Total Spend",
        min_value=0.0,
        value=500.0
    )

    interaction = st.number_input(
        "Last Interaction",
        min_value=0,
        value=15
    )

st.divider()

# -------------------------------
# Prediction
# -------------------------------

if st.button("🔍 Predict Churn", use_container_width=True):

    input_df = pd.DataFrame({

        "Age":[age],

        "Gender":[
            label_encoders["Gender"].transform([gender])[0]
        ],

        "Tenure":[tenure],

        "Usage Frequency":[usage],

        "Support Calls":[support],

        "Payment Delay":[payment],

        "Subscription Type":[
            label_encoders["Subscription Type"].transform([subscription])[0]
        ],

        "Contract Length":[
            label_encoders["Contract Length"].transform([contract])[0]
        ],

        "Total Spend":[spend],

        "Last Interaction":[interaction]

    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)

    churn_prob = probability[0][1] * 100
    stay_prob = probability[0][0] * 100

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ Customer is likely to Churn")

    else:

        st.success("✅ Customer is likely to Stay")

    st.write("### Prediction Confidence")

    st.progress(int(max(churn_prob, stay_prob)))

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Stay Probability",
            f"{stay_prob:.2f}%"
        )

    with col2:

        st.metric(
            "Churn Probability",
            f"{churn_prob:.2f}%"
        )

    st.divider()

    st.subheader("Input Summary")

    st.dataframe(input_df, use_container_width=True)