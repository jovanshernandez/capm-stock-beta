# CAPM Stock Beta Calculator

![image](https://github.com/user-attachments/assets/24912654-2d4b-4a3b-924d-8c89e4caef11)

This script calculates the **beta** for various stocks based on the **Capital Asset Pricing Model (CAPM)**. CAPM uses beta to quantify a stock's volatility relative to the overall market (represented by the S&P 500 in this script). Beta values help investors understand the systematic risk of a stock and make more informed portfolio decisions.

## Prerequisites

- **Python 3.7+**
- Required Libraries: `pandas`, `numpy`, `matplotlib`, `plotly`

Install required libraries:
```bash
pip install pandas numpy matplotlib plotly
```

## Data Requirements

The script expects a CSV file named `stocks_dataset.csv` containing historical daily stock prices. It should include one column for the S&P 500 (or a similar market benchmark) and additional columns for each stock to analyze.

**Data Format Example:**
| Date       | sp500   | TSLA   | AAPL   | BA    |
|------------|---------|--------|--------|-------|
| 2020-01-01 | 3200.0  | 430.0  | 300.0  | 330.0 |
| 2020-01-02 | 3210.0  | 435.0  | 310.0  | 340.0 |
| ...        | ...     | ...    | ...    | ...   |

## How the Script Works

### 1. Data Normalization
The `normalize()` function standardizes stock prices relative to their initial values. This step allows for an effective comparison by placing all stock prices on a uniform scale.

### 2. Daily Returns Calculation
The `daily_return()` function calculates each stock's daily percentage change, which is essential for CAPM. CAPM requires daily returns to analyze how each stock's returns respond to market changes.

### 3. Beta Calculation using CAPM
For each stock, beta is calculated as the slope of the linear regression line between the stock's daily returns and the S&P 500’s daily returns. According to CAPM:
   - **Beta** indicates the stock's sensitivity to market movements.
   - **Alpha** (y-intercept) is also derived but is not used for further analysis in this script.

   In CAPM, beta is the key metric for understanding systematic risk.

### 4. Display Results
The beta values for each stock are printed to the console, providing insight into each stock’s market-related volatility.

## Running the Script

Ensure the `stocks_dataset.csv` file is in the same directory as the script, then execute:

```bash
python calculate_beta.py
```

The script will output beta values for each stock, helping users understand relative risk levels.

## Interpreting CAPM Beta

- **Beta = 1**: Stock is as volatile as the overall market.
- **Beta < 1**: Stock is less volatile than the market (e.g., utility stocks).
- **Beta > 1**: Stock is more volatile than the market (e.g., technology stocks).

CAPM beta values support investors in assessing risk-adjusted returns and making balanced portfolio decisions.

---
