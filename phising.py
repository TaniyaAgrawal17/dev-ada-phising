import streamlit as st

st.set_page_config(
    page_title="Phishing Email Detector",
    layout="wide"
)

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
    if email_text:
        # Example logic — replace with your actual model
        import random
        confidence = random.uniform(0.5, 1.0)
        is_phishing = confidence > 0.7

        st.markdown(f"""
            <div style="padding: 20px; border-radius: 10px; background-color: {'#ffdddd' if is_phishing else '#ddffdd'};">
                <h3 style="color: {'#cc0000' if is_phishing else '#006600'};">
                    {'🚨 Phishing Detected' if is_phishing else '✅ Looks Legit'}
                </h3>
                <p style="font-size: 18px;">
                    Confidence: {confidence:.2f}
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Enter an email on the left to see results.")