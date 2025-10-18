🕊️ Mental Health Chat Analyzer

A simple and interactive web application that helps you analyze your thoughts and emotions, providing motivational messages and emotional support based on your input. Built using Streamlit and Hugging Face Transformers.

Features

💬 Sentiment Analysis: Detects whether your input is positive, negative, or neutral.

🧠 Motivational Responses: Provides encouraging and supportive messages tailored to your detected emotions.

😄 Emoji Feedback: Displays an emoji reflecting your emotional state.

🌟 Multi-line Support: Analyze multiple lines of text at once.

🖥️ Interactive UI: Clean, user-friendly interface built with Streamlit.


Installation

Clone the repository:

git clone https://github.com/<your-username>/mental-health-chat-analyzer.git
cd mental-health-chat-analyzer


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install required dependencies:

pip install -r requirements.txt


Example requirements.txt:

streamlit
transformers
torch

Usage

Run the app locally:

streamlit run mental_health_chat_analyzer.py


Enter your thoughts or feelings in the text area.

Click Analyze My Emotion.

Receive instant sentiment analysis with emoji feedback and motivational messages.

How It Works

User enters text into the Streamlit app.

Each line of text is sent to Hugging Face's sentiment-analysis pipeline.

The model predicts the sentiment: POSITIVE, NEGATIVE, or NEUTRAL.

Based on the detected sentiment, a corresponding motivational message and emoji are displayed.

Technologies Used

Python

Streamlit

Transformers (Hugging Face)

PyTorch

Contributing

Contributions are welcome! You can:

Suggest new motivational messages

Improve sentiment detection

Add multi-language support

Enhance the UI/UX

Author

Keerthi Sri

GitHub: @Keerthi285820
