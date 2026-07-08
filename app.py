import streamlit as st
import joblib
from googletrans import Translator

# Load model and vectorizer
model, vectorizer = joblib.load("final_accuracy_complaint_classifier.joblib")

# Translator
translator = Translator()

# Streamlit App
st.title(" Multi-language Ticket Classifier")

# User Input
user_input = st.text_area("✍️ Enter your complaint in any language:")

if st.button("Classify"):
    if user_input.strip():
        # Translate input to English
        translated_text = translator.translate(user_input, dest="en").text
        st.write(f"🔄 Translated to English: **{translated_text}**")

        # Vectorize translated text
        X = vectorizer.transform([translated_text])

        # Predict using model
        prediction = model.predict(X)[0]

        st.success(f"✅ Predicted Category: **{prediction}**")
    else:
        st.warning("⚠️ Please enter some text before classifying.")

st.markdown("""
---
<div style='text-align: center; font-size: 14px; color: grey;'>
Developed by <b>Kiran Kumar Petlu</b>
</div>
""", unsafe_allow_html=True)
