import streamlit as st
import joblib
import pandas as pd

# Load the saved model pipeline
model = joblib.load("C:/Users/SOMEN/OneDrive/Desktop/TEAM COLLAB/1st_Collaboration_project/for_somen/App/insurance_pipeline.pkl")

st.set_page_config(page_title="Insurance Charges Predictor", page_icon="💰", layout="centered")

# App title
st.title("💰 Insurance Charges Prediction")
st.write("Enter the details below to estimate insurance charges.")

# Collect user inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0, step=1)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Predict button
if st.button("Predict Charges"):
    # Create DataFrame for model
    input_df = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Show result
    st.success(f"💵 Estimated Insurance Charges: **${prediction:,.2f}**")
