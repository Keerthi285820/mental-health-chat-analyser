import streamlit as st
from transformers import pipeline
from streamlit_lottie import st_lottie
import requests
import random

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Get motivational quotes
def get_motivation(label):
    quotes = {
        "POSITIVE": [
            "Keep shining, you're doing amazing! ✨",
            "Every day is a new opportunity to grow! 🌱",
            "Stay positive and keep pushing forward! 🚀"
        ],
        "NEGATIVE": [
            "It's okay to feel this way. You're not alone. 🌧️",
            "Take a deep breath. Things will get better. 🌈",
            "You're stronger than you think. Don't give up. 💪"
        ],
        "NEUTRAL": [
            "Stay steady. Peace of mind is power. ☯️",
            "Everything happens for a reason. Trust the process. 🔄",
            "Let go of what you can't control. 🌿"
        ]
    }
    return random.choice(quotes.get(label, quotes["NEUTRAL"]))

# Analyze the sentiment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Load animation
lottie_mental = load_lottieurl("https://lottie.host/270d6018-92b0-4a97-a2d7-9ac82d8f367e/kL7J2W5NdE.json")

# Page config
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="🕊️💖", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f2f7f5;
    }
    .stTextArea textarea {
        background-color: #fff;
        color: #000;
    }
    .stButton > button {
        background-color: #5cdb95;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: #379683;
    }
    </style>
""", unsafe_allow_html=True)

# App title and animation
st.title("🧠 Mental Health Chat Analyzer")
st.markdown("Type how you feel below. We'll help you with support and motivation 💖")

with st.container():
    st_lottie(lottie_mental, height=250, key="mental")

# Input box
user_input = st.text_area("💬 How are you feeling today?", height=150)

# Button click
if st.button("Analyze My Emotion"):
    if user_input.strip():
        label, score = analyze_sentiment(user_input)

        # Result display
        st.subheader("📝 Sentiment Analysis")
        st.write(f"**Detected Emotion:** `{label}`")
        st.write(f"**Confidence Score:** `{score:.2f}`")

        # Motivation display
        st.subheader("💡 Here's some motivation for you")
        st.success(get_motivation(label))
    else:
        st.warning("Please type something to analyze 💬")

# Footer
st.markdown("---")
st.markdown("<center>Made with ❤️ by [Your Name] | Powered by Hugging Face & Streamlit</center>", unsafe_allow_html=True)
