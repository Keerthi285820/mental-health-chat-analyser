# app.py

import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']
    return label, score

# Function to get suggestions/motivational quotes
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
    # Return a random quote from the label group
    import random
    return random.choice(quotes.get(label, quotes["NEUTRAL"]))

# Streamlit UI
st.set_page_config(page_title="Mental Health Chat Analyzer", page_icon="🧠")

st.title("🧠 Mental Health Chat Analyzer")
st.markdown("Type how you feel below. Get a sentiment analysis and receive motivational support. ❤️")

user_input = st.text_area("💬 How are you feeling today?", height=150)

if st.button("Analyze"):
    if user_input.strip():
        label, score = analyze_sentiment(user_input)
        
        # Display sentiment
        st.subheader("📝 Sentiment Analysis Result")
        st.write(f"**Sentiment:** {label}")
        st.write(f"**Confidence Score:** {score:.2f}")

        # Show motivational message
        st.subheader("💡 Suggestion / Motivation")
        st.success(get_motivation(label))
    else:
        st.warning("Please type something to analyze.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Your Name] | Powered by Hugging Face & Streamlit")

      

