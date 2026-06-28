import yfinance as yf
import pandas as pd

stocks = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

all_data = []

for stock in stocks:

    data = yf.Ticker(stock).history(period="5d")

    data["Stock_Name"] = stock

    all_data.append(data)

print("Number of DataFrames stored:")
print(len(all_data))