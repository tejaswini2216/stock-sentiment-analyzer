import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# App settings
st.set_page_config(page_title="📈 AI Stock Sentiment Analyzer", page_icon="🤖", layout="wide")

st.title("📈 AI Stock Sentiment Analyzer")
st.markdown("Analyze **financial headlines** and **stock performance** using FinBERT + Yahoo Finance")

# Load FinBERT model
@st.cache_resource
def load_model():
    model_name = "ProsusAI/finbert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

nlp = load_model()

# Input section
st.sidebar.header("🔍 Input Options")
headline = st.sidebar.text_area("Enter financial news headline:", "Apple shares jump after strong earnings report")
ticker = st.sidebar.text_input("Enter Stock Symbol (e.g. AAPL, TSLA):", "AAPL")

# Sentiment Analysis
if st.sidebar.button("Analyze Sentiment"):
    with st.spinner("Analyzing sentiment..."):
        result = nlp(headline)[0]
        label = result['label']
        score = round(result['score'], 3)
    
    if label == "positive":
        sentiment_display = "🟢 Positive"
    elif label == "negative":
        sentiment_display = "🔴 Negative"
    else:
        sentiment_display = "🟡 Neutral"

    # Display result
    st.subheader("Sentiment Analysis Result")
    st.success(f"**Sentiment:** {sentiment_display}")
    st.metric("Confidence", f"{score*100:.1f}%")

    # Fetch stock data
    st.subheader(f"{ticker.upper()} — Recent 7-Day Trend")
    data = yf.download(ticker, period="7d", interval="1h")

    if not data.empty:
        st.line_chart(data["Close"])
        st.caption("Source: Yahoo Finance")
    else:
        st.warning("⚠️ Could not fetch stock data. Check the ticker symbol.")

# Footer
st.markdown("---")
st.caption("Model: [FinBERT (ProsusAI/finbert)](https://huggingface.co/ProsusAI/finbert) | Built by Tejaswini Katamreddy 🌸")
