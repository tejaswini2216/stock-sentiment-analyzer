import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

# --- Page Config ---
st.set_page_config(page_title="Stock Sentiment Analyzer", page_icon="📈", layout="wide")

# --- App Title ---
st.title("📈 Stock Sentiment Analyzer (FinBERT)")
st.markdown("Analyze financial news or stock headlines using a FinBERT model fine-tuned for finance-related sentiment.")

# --- Load Model ---
@st.cache_resource
def load_model():
    model_name = "ProsusAI/finbert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

nlp = load_model()

# --- User Input ---
st.subheader("🔍 Enter financial news or headline:")
headline = st.text_area("Example: *Apple shares jump after strong earnings report*", height=100)

# --- Analyze Button ---
if st.button("Analyze Sentiment"):
    if headline.strip():
        with st.spinner("Analyzing sentiment..."):
            result = nlp(headline)[0]
            label = result['label']
            score = round(result['score'], 3)

        # --- Display Results ---
        if label == "positive":
            color = "🟢 Positive"
        elif label == "negative":
            color = "🔴 Negative"
        else:
            color = "🟡 Neutral"

        st.success(f"**Sentiment:** {color}")
        st.metric("Confidence", f"{score*100:.1f}%")
    else:
        st.warning("Please enter a headline to analyze.")

# --- About Section ---
st.markdown("---")
st.markdown("**Model:** [FinBERT (ProsusAI/finbert)](https://huggingface.co/ProsusAI/finbert)")
st.markdown("**Built by:** Tejaswini Katamreddy 🌸")
