import streamlit as st
import numpy as np
import joblib

scaler = joblib.load("/content/scaler_nn.pkl")
model = tf.keras.models.load_model("/content/neural_network_asd_model.keras")

st.title("ASD Traits Screening Prediction App")
st.write("Fill in the child's information below to predict ASD traits.")

# ------------- INPUT FIELDS (22 FEATURES) --------------------

A1 = st.selectbox("A1: Routine / Struggle with Change", [0, 1])
A2 = st.selectbox("A2: Difficulty Maintaining Eye Contact", [0, 1])
A3 = st.selectbox("A3: Struggle with Social Interaction", [0, 1])
A4 = st.selectbox("A4: Unusual Sensory Reactions", [0, 1])
A5 = st.selectbox("A5: Repetitive Behaviors (flapping/rocking)", [0, 1])
A6 = st.selectbox("A6: Struggle to Understand Feelings", [0, 1])
A7 = st.selectbox("A7: Prefers to Play Alone", [0, 1])
A8 = st.selectbox("A8: Issues with Communication", [0, 1])
A9 = st.selectbox("A9: Takes Language Literally", [0, 1])

SRS = st.slider("Social Responsiveness Scale (0–10)", 0, 10, 1)
QCHAT = st.slider("Qchat-10 Score (0–10)", 0, 10, 1)

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

# ---------------- FORMAT THE INPUT IN CORRECT ORDER ----------------

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

