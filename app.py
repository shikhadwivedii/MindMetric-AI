import streamlit as st
import numpy as np
import pickle

# Load Model
model = pickle.load(open('models/stress_model.pkl', 'rb'))

# Page Title
st.title("🧠 MindMetric AI")
st.subheader("AI-Powered Stress & Burnout Detection System")

# Sidebar
st.sidebar.title("About")

st.sidebar.info(
    """
    MindMetric AI is an AI-powered stress and burnout prediction system 
    using Machine Learning and psychological indicators.
    """
)

# User Inputs

anxiety_level = st.slider("Anxiety Level", 0, 10, 5)

self_esteem = st.slider("Self Esteem", 0, 30, 15)

mental_health_history = st.slider("Mental Health History", 0, 1, 0)

depression = st.slider("Depression Level", 0, 10, 5)

headache = st.slider("Headache Frequency", 0, 5, 2)

blood_pressure = st.slider("Blood Pressure", 0, 3, 1)

sleep_quality = st.slider("Sleep Quality", 0, 5, 3)

breathing_problem = st.slider("Breathing Problem", 0, 5, 1)

noise_level = st.slider("Noise Level", 0, 5, 2)

living_conditions = st.slider("Living Conditions", 0, 5, 3)

safety = st.slider("Safety Level", 0, 5, 3)

basic_needs = st.slider("Basic Needs Fulfillment", 0, 5, 3)

academic_performance = st.slider("Academic Performance", 0, 5, 3)

study_load = st.slider("Study Load", 0, 5, 3)

teacher_student_relationship = st.slider(
    "Teacher Student Relationship",
    0,
    5,
    3
)

future_career_concerns = st.slider(
    "Future Career Concerns",
    0,
    5,
    3
)

social_support = st.slider("Social Support", 0, 5, 3)

peer_pressure = st.slider("Peer Pressure", 0, 5, 2)

extracurricular_activities = st.slider(
    "Extracurricular Activities",
    0,
    5,
    3
)

bullying = st.slider("Bullying Exposure", 0, 5, 1)

# Prepare Input Data
input_data = np.array([[
    anxiety_level,
    self_esteem,
    mental_health_history,
    depression,
    headache,
    blood_pressure,
    sleep_quality,
    breathing_problem,
    noise_level,
    living_conditions,
    safety,
    basic_needs,
    academic_performance,
    study_load,
    teacher_student_relationship,
    future_career_concerns,
    social_support,
    peer_pressure,
    extracurricular_activities,
    bullying
]])

# Prediction Button
if st.button("Predict Stress Level"):

    prediction = model.predict(input_data)

    stress = prediction[0]

    st.subheader("🧠 Stress Analysis Result")

    # LOW STRESS
    if stress == 0:

        st.success("Low Stress Level 😊")

        st.markdown("""
        ### Wellness Status
        - Emotionally balanced
        - Healthy stress management
        - Good psychological stability

        ### Recommendation
        Continue maintaining your current lifestyle habits.
        """)

        st.subheader("Stress Meter")
        st.progress(25)

    # MODERATE STRESS
    elif stress == 1:

        st.warning("Moderate Stress Level 😐")

        st.markdown("""
        ### Wellness Status
        - Increasing stress indicators
        - Possible academic/work fatigue
        - Sleep imbalance detected

        ### Recommendation
        Improve sleep quality, reduce overload, and take regular breaks.
        """)

        st.subheader("Stress Meter")
        st.progress(60)

    # HIGH STRESS
    else:

        st.error("High Stress Level 😟")

        st.markdown("""
        ### Wellness Status
        - High burnout risk
        - Emotional overload detected
        - Mental wellness affected

        ### Recommendation
        Prioritize mental health, reduce pressure, and seek support.
        """)

        st.subheader("Stress Meter")
        st.progress(90)

# Footer
st.markdown("---")

st.caption("Developed by Shikha | AI Wellness Analytics Project")