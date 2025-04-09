import streamlit as st
import joblib
import numpy as np


#def load_model():
#    with open('svm_model.pkl', 'rb') as file:
#        model = pickle.load(file)
#    return model
#model = load_model()

svm_model = joblib.load("svm_model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.set_page_config(
    page_title="Phishing Email Detector",
    layout="wide"
)

# Create tabs
tab1, tab2 = st.tabs(["Email Detector", "About Phishing"])

with tab1:
    # title + intro
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🛡️ Phishing Email Detector</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size: 18px; color: #555;'>
        Enter an email on the left, and we’ll analyze whether it’s a phishing attempt or a legitimate message.
    </div>
    <br>
    """, unsafe_allow_html=True)

    # layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("✉️ Paste Email Content")
        email_text = st.text_area("Enter the email content here:", height=300)


    with col2:
        st.subheader("🔍 Classification Result")
        if email_text.strip():
            email_list = [email_text]
            x_input = tfidf_vectorizer.transform(email_list)
            prediction = svm_model.predict(x_input)

            is_phishing = (prediction[0] == 1)

        st.markdown(f"""
            <div style="padding: 20px; border-radius: 10px; background-color: {'#ffdddd' if is_phishing else '#ddffdd'};">
                <h3 style="color: {'#cc0000' if is_phishing else '#006600'};">
                    {'🚨 Looks like phishing' if is_phishing else '✅ Looks Legit'}
                </h3>
            </div>
        """, unsafe_allow_html=True)
        else:
            st.info("Enter an email on the left to see results.")