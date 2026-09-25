import streamlit as st
import joblib
import numpy as np

st.title('Housing Price Predictor')
st.header('Enter Feature Values')

# Load model
data = joblib.load('housingdf.joblib')
model = data['model']
columns = data['columns']

# Create input fields for each feature
inputs = []
for col in columns:
    val = st.text_input(f'Enter {col}:')
    inputs.append(val)

# Predict
if st.button('Predict'):
    features = [float(x) for x in inputs]
    prediction = model.predict([features])
    st.write(f'Predicted House Value: {prediction[0]:.4f}')