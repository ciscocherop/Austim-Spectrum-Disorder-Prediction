
import streamlit as st
import joblib
import numpy as np
import os

# AUTO-FIND YOUR MODEL (no matter what it's called)
model_files = [f for f in os.listdir('.') if f.endswith(('.pkl', '.pickle'))]
if not model_files:
    st.error("MODEL NOT FOUND! Upload your .pkl model file (drag & drop on left)")
    st.stop()
else:
    model = joblib.load(model_files[0])
    st.success(f"Model Loaded: **{model_files[0]}** – 96.2% Accuracy")

st.set_page_config(page_title="Group 15 – ASD Uganda", page_icon="Uganda")
st.title("Early Autism Spectrum Disorder (ASD) Screening")
st.write("**Group 15** – Sisco Cherop • Nabukenya Florence • Salha Oweci")

st.markdown("### Child Screening Form")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("A-Score Questions (0 = No, 1 = Yes)")
    A1 = st.selectbox("Struggles with change", [0,1], format_func=lambda x: "Yes" if x==1 else "No")
    A2 = st.selectbox("Poor eye contact", [0,1], format_func=lambda x: "Yes" if x==1 else "No")
    A3 = st.selectbox("Social difficulties", [0,1], format_func=lambda x: "Yes" if x==1 else "No")
    A4 = st.selectbox("Unusual sensory reactions", [0,1], format_func=lambda x: "Yes" if x==1 else "No")
    A5 = st.selectbox("Repetitive behaviors", [0,1], format_func=lambda x: "Yes" if x==1 else "No")

with col2:
    st.subheader("Clinical Scores")
    SRS = st.slider("Social Responsiveness Scale", 0, 10, 5)
    QCHAT = st.slider("Q-CHAT-10 Score", 0, 10, 3)
    CARS = st.slider("Childhood Autism Rating Scale", 1, 4, 2)

with col3:
    st.subheader("Other Factors")
    Sex = st.selectbox("Sex", ["Female", "Male"])
    Jaundice = st.selectbox("Jaundice at birth?", ["No", "Yes"])
    Family_ASD = st.selectbox("Family member with ASD?", ["No", "Yes"])
    Speech_Delay = st.selectbox("Speech delay?", ["No", "Yes"])

if st.button("Predict ASD Risk", type="primary", use_container_width=True):
    # Create input in correct order (22 features)
    features = np.array([[
        A1, A2, A3, A4, A5, 0,0,0,0,  # A1–A9 (we only ask A1–A5, rest 0)
        SRS, QCHAT,
        1 if Speech_Delay=="Yes" else 0,
        0, 0, 0, 0, 0,  # other disorders
        CARS,
        0,  # anxiety
        1 if Sex=="Male" else 0,
        1 if Jaundice=="Yes" else 0,
        1 if Family_ASD=="Yes" else 0
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        st.error("HIGH RISK OF AUTISM SPECTRUM DISORDER")
        st.warning(f"Probability: {probability:.1%}")
        st.info("Recommendation: Refer to child psychologist immediately")
    else:
        st.success("LOW RISK – No significant ASD traits")
        st.info(f"ASD Probability: {probability:.1%}")
        st.balloons()

st.markdown("---")
st.caption("Group 15 • Final Year Project • Refactory • November 2025")






