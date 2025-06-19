import streamlit as st
from transformers import pipeline
import random

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Motivational messages based on sentiment
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

# Emoji for each sentiment label
def get_emoji(label):
    return {
        "POSITIVE": "😄",
        "NEGATIVE": "😔",
        "NEUTRAL": "😐"
    }.get(label, "🤖")

# Streamlit page config
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="💬")

# App title
st.title("🕊️ Mental Health Chat Analyzer")
st.write("Tell us how you're feeling today. We'll analyze each thought and respond with kindness 💖")

# User input
user_input = st.text_area("💬 How are you feeling today?", height=200)

# Analyze button logic
if st.button("Analyze My Emotion"):
    if user_input.strip():
        st.subheader("💡 Your Emotional Support")

        # Split into lines
        lines = user_input.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        # Analyze each line
        for line in lines:
            result = sentiment_pipeline(line)[0]
            label = result['label']
            score = result['score']
            emoji = get_emoji(label)
            response = get_motivation(label)

            st.markdown(f"**🧠 You shared:** _{line}_")
            st.markdown(f"{emoji} **Detected Emotion:** `{label}` (Confidence: `{score*100:.2f}%`)")
            st.markdown(f"💬 **Response:** {response}")
            st.markdown("---")
    else:
        st.warning("Please enter your thoughts before analyzing.")

 
