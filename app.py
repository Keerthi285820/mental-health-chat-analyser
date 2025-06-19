import streamlit as st
from transformers import pipeline
import random

# Load the sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Motivational message generator
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

# Set up Streamlit app
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="💬")
st.title("🧠 Mental Health Chat Analyzer")
st.write("Tell us how you're feeling today, and we'll respond to each thought with motivation and care.")

# User input
user_input = st.text_area("💬 How are you feeling today?", height=200)

# On click
if st.button("Analyze My Emotion"):
    if user_input.strip():
        st.subheader("💡 Your Emotional Support")

        # Split input by lines (each line = 1 thought)
        lines = user_input.strip().split('\n')
        lines = [line.strip() for line in lines if line.strip()]

        for line in lines:
            result = sentiment_pipeline(line)[0]  # ✅ CALL ONCE ONLY
            label = result['label']
            score = result['score']
            response = get_motivation(label)

            st.markdown(f"**🧠 You shared:** _{line}_")
            st.markdown(f"**💬 Response:** {response}")
            st.markdown("---")
    else:
        st.warning("Please type something above before analyzing.")

            
    
