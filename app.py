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

# Title
st.title("📩 SMS Spam Classifier")
st.markdown("Detect whether a message is **Spam or Ham**")

# Input box
input_sms = st.text_area("Enter your message here:")

# Predict button
if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message")
    else:
        result = model.predict([input_sms])[0]

        # Now result is 'ham' or 'spam'
        if result == 'spam':
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam (Ham)")

# Footer
st.markdown("---")
st.markdown("Built by Siddharth 🚀")