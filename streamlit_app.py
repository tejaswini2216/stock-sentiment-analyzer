import streamlit as st

# App settings
st.set_page_config(page_title="Test Streamlit App", layout="wide")

st.title("✅ Streamlit Minimal Test App")
st.write("If you see this, Streamlit is running correctly.")

# Sidebar test
st.sidebar.header("Sidebar Test")
headline = st.sidebar.text_input("Enter a headline:", "Apple shares jump")
ticker = st.sidebar.text_input("Enter a stock symbol:", "AAPL")

if st.sidebar.button("Analyze"):
    st.subheader("Results will appear here")
    st.success(f"Headline: {headline}")
    st.info(f"Ticker: {ticker}")
