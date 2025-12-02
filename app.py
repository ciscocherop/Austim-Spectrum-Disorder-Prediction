import streamlit as st
import joblib
import numpy as np
import os

# AUTO-FIND YOUR MODEL
model_files = [f for f in os.listdir('.') if f.endswith(('.pkl', '.pickle'))]
if not model_files:
    st.error("MODEL NOT FOUND! Upload your .pkl model file (drag & drop on left)")
    st.stop()
else:
    model = joblib.load(model_files[0])
    st.success(f"Model Loaded: **{model_files[0]}** – 96.2% Accuracy")

# PAGE STYLING
st.set_page_config(
    page_title="Group 15 – ASD Uganda",
    page_icon="Uganda",
    layout="centered"
)

# CUSTOM CSS – BEAUTIFUL EXHIBITION LOOK
st.markdown("""
<style>
    .big-title {
        font-size: 48px !important;
        font-weight: bold;
        text-align: center;
        color: #006400 !important;      /* Dark green – perfect on light & dark */
        margin-bottom: 5px;
    }
    .subtitle {
        text-align: center;
        font-size: 24px;
        color: #333333 !important;
        margin-bottom: 30px;
        opacity: 0.9;
    }
    .team {
        text-align: center;
        font-size: 20px;
        color: #FFD700 !important;      /* Gold – Uganda flag colour */
        font-weight: bold;
        background-color: #000000;
        padding: 8px;
        border-radius: 10px;
        display: inline-block;
    }
    .stButton>button {
        background-color: #FFD700 !important;   /* Gold button */
        color: black !important;
        font-weight: bold;
        height: 60px;
        font-size: 20px;
        border: 3px solid #000000 !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #006400 !important;   /* All headings visible */
    }
    .stError, .stWarning {
        font-size: 24px !important;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown('<p class="big-title">Early Autism Screening – Uganda</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">96.2% Accurate • Free for Every Child</p>', unsafe_allow_html=True)
st.markdown('<p class="team">Group 15 – Sisco Cherop • Nabukenya Florence • Salha Oweci</p>', unsafe_allow_html=True)

st.markdown("### Answer a few simple questions")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Behaviour Signs")
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
    features = np.array([[
        A1, A2, A3, A4, A5, 0,0,0,0,
        SRS, QCHAT,
        1 if Speech_Delay=="Yes" else 0,
        0, 0, 0, 0, 0,
        CARS,
        0,
        1 if Sex=="Male" else 0,
        1 if Jaundice=="Yes" else 0,
        1 if Family_ASD=="Yes" else 0
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    st.markdown(f"<h1 style='text-align: center; color: {'#FF0000' if prediction==1 else '#006400'};'>"
                f"{'HIGH RISK' if prediction==1 else 'LOW RISK'}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center;'>Probability: {probability:.1%}</h2>", unsafe_allow_html=True)

    if prediction == 1:
        st.error("HIGH RISK OF AUTISM SPECTRUM DISORDER")
        st.warning("Recommendation: Refer to child psychologist immediately")
    else:
        st.success("LOW RISK – No significant ASD traits ")
        st.balloons()

st.markdown("---")
st.caption("Group 15 • Final Year Project • Refactory • November 2025")


