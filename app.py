import streamlit as st
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Spam Classifier",
    page_icon="📩",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #bbbbbb;
        margin-bottom: 30px;
    }
    .stTextArea textarea {
        border-radius: 10px;
        padding: 10px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: gray;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📩 SMS Spam Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect whether a message is <b>Spam</b> or <b>Ham</b></div>', unsafe_allow_html=True)

# Card-like container
with st.container():
    st.markdown("### ✉️ Enter your message below")
    input_sms = st.text_area("", placeholder="Type your message here...")

# Button centered
col1, col2, col3 = st.columns([1,2,1])
with col2:
    predict_btn = st.button("🔍 Predict")

# Predict button logic (UNCHANGED)
if predict_btn:

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        result = model.predict([input_sms])[0]

        if result == 'spam':
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam (Ham)")

# Divider
st.markdown("---")

# Footer (your required content)
st.markdown("""
<div class="footer">
Machine Learning Project Submitted to Vandana Bhatia mam by<br><br>

<b>Siddharth Gautam</b><br>
Roll no. 2023UEC2622<br>
ECE2, 6th Semester<br><br>

<b>Harshit Chauhan</b><br>
Roll no. 2023UEC2644<br>
ECE2, 6th Semester
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.footer {
    text-align: center;
    font-size: 18px;   /* 🔥 increased from 14px */
    color: #bbbbbb;
    margin-top: 50px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)