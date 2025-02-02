import streamlit as st
import requests

def classify_email(email_text):
    response = requests.post("http://localhost:8080/api/predict", json={"content": email_text})
    if response.status_code == 200:
        return response.json()["prediction"]
    else:
        st.error(f"Error: {response.status_code}")

st.title("Email Spam Classifier")

email = st.text_area("Enter your email here", height=300)
if st.button("CHECK"):
    if email:
        prediction = classify_email(email)
        if prediction == 1:
            st.markdown("<h2 style='color: red'>Spam</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color: green'>Not Spam</h2>", unsafe_allow_html=True)
    else:
        st.error("Failed to classify the email.")
