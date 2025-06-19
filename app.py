import streamlit as st
from transformers import pipeline
import random

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Define motivational responses
def get_motivation(label):
    responses = {
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
    return random.choice(responses.get(label, responses["NEUTRAL"]))

# Page setup
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="💬")
st.title("🧠 Mental Health Chat Analyzer")
st.write("Tell us how you're feeling. We'll respond to each thought with kindness and support. 💖")

# Text input
user_input = st.text_area("💬 How are you feeling today?", height=200)

# Analyze button
if st.button("Analyze My Emotion"):
    if user_input.strip():
        st.subheader("💡 Supportive Replies")

        # ✅ Split by newline only (you asked for real interaction line by line)
        lines = user_input.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        # Loop through each line
        for line in lines:
            label, score = sentiment_pipeline(line)[0]['label'], sentiment_pipeline(line)[0]['score']
            response = get_motivation(label)

            # Output
            st.write(f"**You shared:** _{line}_")
            st.write(f"**Response:** {response}")
            st.markdown("---")
    else:
        st.warning("Please type something to analyze.")


