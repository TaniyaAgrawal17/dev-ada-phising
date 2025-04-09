import streamlit as st
import joblib
import numpy as np

# Load model and vectorizer
svm_model = joblib.load("svm_model.pkl")
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Set page configuration
st.set_page_config(
    page_title="Phishing Email Detector",
    layout="wide"
)

st.markdown("""
<style> 
    .block-container {
            padding-bottom: 0.5rem;
        }
            /* Custom dark blue button */
    .stButton>button {
        background-color: #1a3e72;
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #0d2b57;
        color: white;
        border: none;
    }
    
    .stButton>button:focus {
        background-color: #0d2b57;
        color: white;
        border: none;
        box-shadow: 0 0 0 0.2rem rgba(26, 62, 114, 0.5);
    }
            </style>
            """, unsafe_allow_html=True)

# Create a navigation button (icon) for the "About Phishing" page
if st.button("📚 Learn About Phishing"):
    page = "About Phishing"
else:
    page = "Phishing Email Detector"

# Page 1: Phishing Email Detector
if page == "Phishing Email Detector":
    # Title + Intro
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🛡️ Phishing Email Detector</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size: 18px; color: #555;'>
        Enter an email on the left, and we’ll analyze whether it’s a phishing attempt or a legitimate message.
    </div>
    <br>
    """, unsafe_allow_html=True)

    # Layout for Email content and classification result
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="email-input">
            <h3>✉️ Paste Email Content</h3>
            <p style='color: #666; font-size: 14px;'>Enter the email content</p>
        </div>
        """, unsafe_allow_html=True)
        email_text = st.text_area("", height=300, label_visibility="collapsed", key="email_input")
        
        # Add submit button
        submit_button = st.button("Analyze Email", use_container_width=True)


    with col2:
        st.subheader("🔍 Classification Result")
        if submit_button and email_text.strip():
            email_list = [email_text]
            x_input = tfidf_vectorizer.transform(email_list)
            prediction = svm_model.predict(x_input)

            is_phishing = (prediction[0] == 1)

            st.markdown(f"""
                <div style="padding: 30px; border-radius: 10px; background-color: {'#ffdddd' if is_phishing else '#ddffdd'};">
                    <h3 style="color: {'#cc0000' if is_phishing else '#006600'};">
                        {'🚨 Looks like phishing' if is_phishing else '✅ Looks Legit'}
                    </h3>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)
            st.info("Enter an email on the left to see results.")

# Page 2: About Phishing Information
elif page == "About Phishing":
    # Add the "Back to Classification" button at the top of the page
    if st.button("🔙 Back to Classification"):
        page = "Phishing Email Detector"

    # Title
    st.markdown("<h1 style='text-align: center; color: #4A90E2;'>📚 About Phishing</h1>", unsafe_allow_html=True)
    
    # Content about phishing
    st.markdown("""
    <h4>Types of Phishing:</h4>
    <ul>
        <li><strong>Email Phishing:</strong> The most common form, where fraudulent emails appear to come from legitimate sources.</li>
        <li><strong>Spear Phishing:</strong> Highly targeted phishing attacks directed at specific individuals or organizations, often using personal information.</li>
        <li><strong>Smishing:</strong> Phishing through SMS text messages, often impersonating services like banks or delivery companies.</li>
        <li><strong>Vishing:</strong> Voice phishing, where attackers impersonate institutions via phone calls to extract data.</li>
        <li><strong>Clone Phishing:</strong> A legitimate email is cloned and slightly modified to include a malicious link or attachment.</li>
    </ul>

    <h3>⚠️ Warning Signs of a Phishing Email</h3>
    <ul>
        <li><strong>Unfamiliar or misspelled sender email:</strong> Check the full email address carefully.</li>
        <li><strong>Generic greetings:</strong> Messages like “Dear Customer” instead of your actual name.</li>
        <li><strong>Spelling/grammar errors:</strong> Many phishing emails contain odd formatting, spelling mistakes, or unnatural language.</li>
        <li><strong>Urgency or threats:</strong> Pressure to act quickly, e.g., “Your account will be locked in 24 hours.”</li>
        <li><strong>Unexpected attachments or links:</strong> Be cautious with files and URLs—hover to preview where a link leads.</li>
    </ul>

    <h3>🧪 Real-World Example</h3>
    <p>
        An attacker sends an email that looks like it's from your university’s IT department, claiming your password has expired. 
        It includes a link to a fake login page that looks identical to the real one. 
        If you enter your credentials, the attacker gains full access to your account.
    </p>

    <h3>🛡️ How to Protect Yourself</h3>
    <ul>
        <li><strong>Be skeptical:</strong> Even if it looks official, double-check emails that ask for personal data.</li>
        <li><strong>Check links carefully:</strong> Hover over links to reveal their destination. Avoid clicking if it seems suspicious.</li>
        <li><strong>Use multi-factor authentication (MFA):</strong> Adds an extra layer of security even if your password is stolen.</li>
        <li><strong>Update software regularly:</strong> Keep browsers, operating systems, and antivirus tools up to date.</li>
        <li><strong>Report phishing attempts:</strong> If you receive a suspicious email, report it to your organization or service provider.</li>
    </ul>

    """, unsafe_allow_html=True)

    # Separate markdown block for link (OUTSIDE HTML)
    st.markdown("### 📘 Want to Learn More?")
    st.markdown("Take this free interactive course to dive deeper into phishing awareness and best practices:")
    st.markdown("[Phishing Awareness Training Course](https://rise.articulate.com/share/i9tuuUp0AIys1VuWJCQihTLQjDWd5_BS#/)") 

# Sticky Footer with Names
st.markdown("""
    <style>
        .footer {
            position: sticky;
            bottom: 0;
            width: 100%;
            color: #1a3e72;
            text-align: center;
            padding-top: 60px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        <p>Created by: Vittoria Gallina, Taniya Agrawal, Caroline Feng, Stephanie Kirova, Kassie Xu, Victoria Hu</p>
    </div>
""", unsafe_allow_html=True)