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
                <div margin-top: 50px; style="padding: 20px; border-radius: 10px; background-color: {'#ffdddd' if is_phishing else '#ddffdd'};">
                    <h3 style="color: {'#cc0000' if is_phishing else '#006600'};">
                        {'🚨 Looks like phishing' if is_phishing else '✅ Looks Legit'}
                    </h3>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Enter an email on the left to see results.")

with tab2:
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>ℹ️ About Phishing</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    ## What is Phishing?
    Phishing is a type of cyber attack where criminals impersonate legitimate organizations 
    to steal sensitive information like login credentials, credit card numbers, or personal data.
    """)
    
    st.markdown("""
    ## Common Phishing Techniques
    - **Deceptive Phishing**: Fake emails pretending to be from reputable companies
    - **Spear Phishing**: Targeted attacks on specific individuals or organizations
    - **Whaling**: Phishing attacks aimed at high-profile targets like executives
    - **Clone Phishing**: Duplicates of legitimate emails with malicious links
    - **Vishing**: Phishing conducted via phone calls (voice phishing)
    """)
    
    st.markdown("""
    ## How to Spot Phishing Emails
    - Check the sender's email address carefully
    - Look for poor grammar and spelling mistakes
    - Be wary of urgent or threatening language
    - Hover over links to see the actual URL before clicking
    - Legitimate companies won't ask for sensitive info via email
    """)
    
    st.markdown("""
    ## What to Do If You Receive a Phishing Email
    - Don't click any links or download attachments
    - Report it to your IT department or email provider
    - Delete the email immediately
    - If you accidentally clicked a link, change your passwords immediately
    """)
    
    st.markdown("""
    ## Additional Resources
    - [Federal Trade Commission - How to Recognize and Avoid Phishing Scams](https://www.consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams)
    - [CISA - Avoiding Social Engineering and Phishing Attacks](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks)
    - [Anti-Phishing Working Group](https://apwg.org/)
    """)