# stock-sentiment-analyzer

An AI-powered sentiment analysis tool for financial news and stock headlines.  
This project uses **FinBERT**, a BERT model fine-tuned for financial sentiment analysis, to classify news as **Positive**, **Negative**, or **Neutral**, and visualize how sentiment correlates with stock price movements.

---

## 🚀 Features
- Analyze financial news headlines using FinBERT.
- Visualize sentiment trends for specific stocks.
- Optional: correlate sentiment scores with stock performance.
- Interactive web app built with Streamlit.

---

## 🧠 Tech Stack
- **Python**
- **Transformers (FinBERT model)**
- **scikit-learn**
- **Pandas / NumPy**
- **yfinance**
- **Streamlit**

---

## 📊 Dataset
You can use:
- [Financial PhraseBank (Kaggle)](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)
- Or scrape headlines using the `newsapi` package.

Example CSV structure:
```csv
date,headline
2024-05-10,"Apple shares jump after earnings beat expectations"
2024-05-10,"Tesla stock drops amid production delays"
