import streamlit as st
import requests

st.set_page_config(page_title="Student Exam Score Predictor", layout="centered")
st.title("🎓 Student Exam Score Predictor")

st.write("Enter the details below to predict the student's exam score:")

hours_studied = st.number_input("Hours Studied", min_value=0.0, step=0.1)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.1)
attendance_percent = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0, step=0.1)
previous_scores = st.number_input("Previous Scores", min_value=0.0, max_value=100.0, step=0.1)

if st.button("Predict Exam Score"):
    api_url = "http://127.0.0.1:8000/predict"

    payload = {
        "hours_studied": hours_studied,
        "sleep_hours": sleep_hours,
        "attendance_percent": attendance_percent,
        "previous_scores": previous_scores
    }

    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            prediction = response.json()["predicted_exam_score"]
            st.success(f"🎯 Predicted Exam Score: {prediction} / 100")
        else:
            st.error("❌ API Error. Check backend.")
    except Exception as e:
        st.error(f"❌ Cannot connect to API: {e}")
