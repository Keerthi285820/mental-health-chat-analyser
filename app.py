import streamlit as st
from transformers import pipeline
import random
import re

# Load sentiment analysis model
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

# Analyze sentiment of a sentence
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Streamlit app layout
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="💬")

st.title("🕊️ Mental Health Chat Analyzer")
st.write("Tell us how you're feeling today. Get caring, motivating responses in return. 💖")

# User input
user_input = st.text_area("💬 How are you feeling?", height=180)

# Process and respond
if st.button("Analyze My Emotion"):
    if user_input.strip():
        st.subheader("💡 Your Emotional Support")

        # Break input into lines/sentences
        lines = re.split(r'[.!?\n]', user_input)
        lines = [line.strip() for line in lines if line.strip()]

        for line in lines:
            label, score = analyze_sentiment(line)
            motivation = get_motivation(label)

            st.write(f"**You shared:** _{line}_")
            st.write(f"**Response:** {motivation}")
            st.write("---")
    else:
        st.warning("Please type something before clicking the button.")

# Footer
st.write("Made with ❤️ using Streamlit and Transformers")

 

      

