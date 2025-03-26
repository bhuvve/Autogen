# filename: stock_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta

def download_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="6mo")
    return data, stock

# Define the stock tickers
tickers = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS"
}

# Container for storing stock data
stock_data = {}
financials = {}

for name, ticker in tickers.items():
    data, stock = download_stock_data(ticker)
    if data['Close'].isnull().all():
        raise ValueError(f"No valid stock data retrieved for {name}.")
    stock_data[name] = data
    financials[name] = {
        "P/E Ratio": stock.info.get("trailingPE"),
        "Forward P/E": stock.info.get("forwardPE"),
        "Dividends": stock.info.get("dividendYield"),
        "Price to Book": stock.info.get("priceToBook"),
        "Debt/Eq": stock.info.get("debtToEquity"),
        "ROE": stock.info.get("returnOnEquity")
    }

# Calculate percentage change over the past 6 months
for name, data in stock_data.items():
    stock_data[name]['Percent Change'] = data['Close'].pct_change()

# Plot normalized stock prices
plt.figure(figsize=(14, 7))
for name, data in stock_data.items():
    normalized_prices = (data['Close'] / data['Close'].iloc[0]) * 100
    plt.plot(data.index, normalized_prices, label=f"{name}")

plt.title('Normalized Stock Prices (6 months)')
plt.xlabel('Date')
plt.ylabel('Normalized Price (%)')
plt.legend(loc="upper left")
plt.grid(True)
plt.savefig('normalized_prices.png')

# Analyze correlation
closes = pd.DataFrame({name: data['Close'] for name, data in stock_data.items()})
correlation_matrix = closes.corr()

# Print out financial ratios and correlation
for name, financial_data in financials.items():
    print(f"Financial data for {name}:")
    for key, value in financial_data.items():
        print(f"  {key}: {value}")
    print("\n")

print("Correlation matrix:")
print(correlation_matrix)

print("\nNormalized prices have been saved to 'normalized_prices.png'.\n")
