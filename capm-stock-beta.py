#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Load stock data
stocks_df = pd.read_csv('stocks_dataset.csv')

# Function to normalize the prices
def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i] / x[i][0]
    return x

# Function to calculate daily returns
def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1, len(df)):
            df_daily_return[i][j] = ((df[i][j] - df[i][j-1]) / df[i][j-1]) * 100
        df_daily_return[i][0] = 0
    return df_daily_return

# Normalize and calculate daily returns
stocks_normalized = normalize(stocks_df)
stocks_daily_return = daily_return(stocks_df)

# Calculate beta for each stock
beta = {}
alpha = {}

for i in stocks_daily_return.columns:
    if i != 'Date' and i != 'sp500':
        b, a = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return[i], 1)
        beta[i] = b
        alpha[i] = a

# Display beta values for each stock
print("Beta values for each stock:")
print(beta)
