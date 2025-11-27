import streamlit as st
import joblib
import numpy as np
import tensorflow as tf

# Load model & scaler
scaler = joblib.load("/content/scaler_nn.pkl")
model = tf.keras.models.load_model("/content/neural_network_asd_model.keras")

st.title("ASD Traits Prediction App")
st.write("Enter the child's information to predict ASD Traits")

# -------------- INPUT FIELDS -----------------
A1 = st.selectbox("Routine / Struggle with Change (A1)", [0, 1])
A2 = st.selectbox("Maintain Eye Contact (A2)", [0, 1])
A3 = st.selectbox("Struggle with Social Interaction (A3)", [0, 1])
A4 = st.selectbox("Unusual Sensory Reactions (A4)", [0, 1])
A5 = st.selectbox("Repetitive Behaviors (A5)", [0, 1])
A6 = st.selectbox("Struggle to Understand Feelings (A6)", [0, 1])
A7 = st.selectbox("Prefer to Play Alone (A7)", [0, 1])
A8 = st.selectbox("Issues with Communication (A8)", [0, 1])
A9 = st.selectbox("Takes Language Literally (A9)", [0, 1])

SRS = st.slider("Social Responsiveness Scale Score (0–10)", 0, 10, 1)
QCHAT = st.slider("QCHAT Screening Score (0–10)", 0, 10, 1)

Speech_Delay = st.selectbox("Speech Delay / Language Disorder", [0, 1])
Learning_Disorder = st.selectbox("Learning Disorder", [0, 1])
Genetic_Disorders = st.selectbox("Genetic Disorders", [0, 1])
Depression = st.selectbox("Depression", [0, 1])
Global_Delay = st.selectbox("Global Developmental Delay / Intellectual Disability", [0, 1])
Social_Issues = st.selectbox("Social / Behavioural Issues", [0, 1])
CARS = st.slider("Childhood Autism Rating Scale (1–4)", 1, 4, 1)
Anxiety = st.selectbox("Anxiety Disorder", [0, 1])
Sex = st.selectbox("Sex (Male=1, Female=0)", [0, 1])
Jaundice = st.selectbox("Jaundice at Birth", [0, 1])
Family_ASD = st.selectbox("Family Member with ASD", [0, 1])

# ---------------- PREDICTION -------------------

input_data = np.array([[
    A1, A2, A3, A4, A5, A6, A7, A8, A9,
    SRS, QCHAT,
    Speech_Delay, Learning_Disorder, Genetic_Disorders,
    Depression, Global_Delay, Social_Issues,
    CARS, Anxiety,
    Sex, Jaundice, Family_ASD
]])

# Scale the input using the same scaler used during training
input_scaled = scaler.transform(input_data)

# -------------------- PREDICTION --------------------------

if st.button("Predict ASD Traits"):
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ The model predicts: **ASD Traits Present**")
    else:
        st.success("✅ The model predicts: **No ASD Traits**")

