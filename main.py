# =========================================================
# Stock Market Data Analyzer
# Author: Yashika Aggarwal
#
# Description:
# This project fetches stock market data using Yahoo Finance,
# performs financial analysis, creates visualizations,
# and generates summary reports.
#
# Disclaimer:
# This project is for educational purposes only and
# does not provide financial or investment advice.
# =========================================================

# =========================
# IMPORT LIBRARIES
# =========================

import os
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CREATE REQUIRED FOLDERS
# =========================

os.makedirs("data", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# =========================
# USER INPUT
# =========================

ticker = "AAPL"

start_date = "2023-01-01"

end_date = "2025-01-01"

# =========================
# FETCH STOCK DATA
# =========================

print("\n===================================")
print(" FETCHING STOCK MARKET DATA ")
print("===================================\n")

try:
    df = yf.download(ticker, start=start_date, end=end_date)

    # Fix multi-level column issue from yfinance
    df.columns = df.columns.get_level_values(0)

    # Check if dataframe is empty
    if df.empty:
        print("No stock data found.")
        exit()

    print("Stock data fetched successfully!\n")

except Exception as e:
    print("Error while fetching stock data:")
    print(e)
    exit()

# =========================
# SAVE RAW DATA
# =========================

df.to_csv("data/stock_data.csv")

print("Stock data saved to data/stock_data.csv\n")

# =========================
# DISPLAY DATA PREVIEW
# =========================

print("Preview of Dataset:\n")

print(df.head())

# =========================
# DATA CLEANING
# =========================

print("\n===================================")
print(" CLEANING DATA ")
print("===================================\n")

# Remove missing values
df.dropna(inplace=True)

print("Missing values removed successfully!\n")

# =========================
# DAILY RETURNS CALCULATION
# =========================

print("Calculating Daily Returns...\n")

df['Daily_Return'] = df['Close'].pct_change()

# =========================
# MOVING AVERAGES
# =========================

print("Calculating Moving Averages...\n")

# 20-Day Moving Average
df['MA20'] = df['Close'].rolling(window=20).mean()

# 50-Day Moving Average
df['MA50'] = df['Close'].rolling(window=50).mean()

# =========================
# VOLATILITY CALCULATION
# =========================

print("Calculating Volatility...\n")

volatility = df['Daily_Return'].std()

# =========================
# HIGHEST & LOWEST PRICE
# =========================

highest_price = df['High'].max()

lowest_price = df['Low'].min()

# =========================
# PRINT SUMMARY
# =========================

print("\n===================================")
print(" STOCK ANALYSIS SUMMARY ")
print("===================================\n")

print(f"Ticker Symbol       : {ticker}")

print(f"Highest Price       : {highest_price:.2f}")

print(f"Lowest Price        : {lowest_price:.2f}")

print(f"Volatility          : {volatility:.5f}")

print("\nAnalysis completed successfully!\n")

# =========================
# PRICE TREND VISUALIZATION
# =========================

print("Generating Stock Trend Chart...\n")

plt.figure(figsize=(14, 7))

plt.plot(df['Close'], label='Closing Price')

plt.plot(df['MA20'], label='20-Day Moving Average')

plt.plot(df['MA50'], label='50-Day Moving Average')

plt.title(f'{ticker} Stock Price Analysis')

plt.xlabel('Date')

plt.ylabel('Price')

plt.legend()

plt.grid(True)

# Save chart
plt.savefig("images/stock_trend.png")

print("Stock trend chart saved successfully!")

# Show chart
plt.show()

# =========================
# DAILY RETURN DISTRIBUTION
# =========================

print("\nGenerating Daily Return Distribution Chart...\n")

plt.figure(figsize=(12, 6))

sns.histplot(df['Daily_Return'].dropna(), bins=50)

plt.title('Daily Return Distribution')

plt.xlabel('Daily Return')

plt.ylabel('Frequency')

plt.grid(True)

# Save chart
plt.savefig("images/daily_returns.png")

print("Daily return distribution chart saved successfully!")

# Show chart
plt.show()

# =========================
# SAVE FINAL SUMMARY REPORT
# =========================

print("\nGenerating Summary Report...\n")

summary = {
    "Ticker": ticker,
    "Highest Price": round(highest_price, 2),
    "Lowest Price": round(lowest_price, 2),
    "Volatility": round(volatility, 5)
}

summary_df = pd.DataFrame([summary])

# Save report
summary_df.to_csv("reports/summary_report.csv", index=False)

print("Summary report saved successfully!")

# =========================
# FINAL MESSAGE
# =========================

print("\n===================================")
print(" PROJECT EXECUTED SUCCESSFULLY ")
print("===================================\n")

print("Generated Files:")

print("\n1. Dataset:")
print("   data/stock_data.csv")

print("\n2. Charts:")
print("   images/stock_trend.png")
print("   images/daily_returns.png")

print("\n3. Report:")
print("   reports/summary_report.csv")

print("\nThank you for using Stock Market Data Analyzer!")

print("\nDISCLAIMER:")
print("This project is for educational purposes only.")
print("It does not provide financial or investment advice.")