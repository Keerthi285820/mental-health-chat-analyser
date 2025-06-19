import streamlit as st
from transformers import pipeline
import random
import re

# Load the pre-trained sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Get motivational message based on sentiment
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

# Analyze a single line of input
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Streamlit UI
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="💬")

st.title("🧠 Mental Health Chat Analyzer")
st.write("Tell us how you're feeling today, and we'll respond with motivation and support.")

# Input box
user_input = st.text_area("💬 How are you feeling today?", height=180)

# On button click
if st.button("Analyze My Emotion"):
    if user_input.strip():
        st.subheader("💡 Your Emotional Support")

        # ✅ Split user input into sentences/lines
        # This handles newlines and punctuation
        lines = re.split(r'[.\n!?]+', user_input)
        lines = [line.strip() for line in lines if line.strip()]  # Remove empty lines

        # Analyze and respond to each line
        for line in lines:
            label, score = analyze_sentiment(line)
            response = get_motivation(label)

            # Display like a conversation
            st.markdown(f"**🧠 You shared:** _{line}_")
            st.markdown(f"**💬 Response:** {response}")
            st.markdown("---")
    else:
        st.warning("Please type something before analyzing.")

