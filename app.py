import streamlit as st
from transformers import pipeline
import random
import re

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Get motivational response
def get_motivation(label):
    messages = {
        "POSITIVE": [
            "That's wonderful to hear! Keep embracing the good moments.",
            "Your positivity is powerful — let it shine!",
            "Keep going! You're doing amazing, even if it doesn’t always feel that way."
        ],
        "NEGATIVE": [
            "It's okay to feel this way. You're not alone.",
            "Hard times don’t last forever. You’re stronger than you think.",
            "Even on the toughest days, your feelings are valid. Take it one step at a time."
        ],
        "NEUTRAL": [
            "Sometimes, just getting through the day is enough. Keep it up.",
            "Stay steady — peace of mind is power.",
            "You're doing fine. Be gentle with yourself."
        ]
    }
    return random.choice(messages.get(label, messages["NEUTRAL"]))

# Analyze one sentence
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Streamlit UI
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="💬")

st.title("🕊️ Mental Health Chat Analyzer")
st.write("Tell us how you're feeling today, and we'll respond with motivation and support.")

# User input
user_input = st.text_area("💬 How are you feeling today?", height=180)

# When user clicks Analyze
if st.button("Analyze My Emotion"):
    if user_input.strip():
        st.subheader("💡 Your Emotional Support")

        # ✅ Split input into separate lines/sentences
        lines = re.split(r'[.!?\n]', user_input)
        lines = [line.strip() for line in lines if line.strip()]

        # Analyze each line separately
        for line in lines:
            label, score = analyze_sentiment(line)
            motivation = get_motivation(label)

            # Show result
            st.write(f"**You shared:** _{line}_")
            st.write(f"**Response:** {motivation}")
            st.markdown("---")
    else:
        st.warning("Please enter how you're feeling to get started.")

