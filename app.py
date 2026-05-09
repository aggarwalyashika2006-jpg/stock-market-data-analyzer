# app.py

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Stock Market Data Analyzer")

ticker = st.text_input("Enter Stock Ticker", "AAPL")

data = yf.download(ticker, period="1y")

st.write(data.tail())

fig, ax = plt.subplots()

ax.plot(data['Close'])

st.pyplot(fig)