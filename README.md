# Super Simple Stock Market

## Overview
This Python application simulates a basic stock market for the Global Beverage Corporation Exchange (GBCE). It allows users to:

- Calculate dividend yield and P/E ratio for a given stock price.
- Record trades with timestamps, quantity, trade type (buy/sell), and price.
- Compute the volume-weighted stock price based on trades within the last 5 minutes.
- Calculate the GBCE All Share Index using the geometric mean of all stocks' volume-weighted stock prices.

## Features
- Object-Oriented Design with `Stock`, `Trade`, and `StockMarket` classes.
- In-memory data storage (no database required).
- Robust error handling and input validation.
- Industry-standard coding practices with modular implementation.

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Run the Python script using:
   ```sh
   python stock_market_demo.py
   ```

## Formulas Used
- **Dividend Yield (Common Stock)** = `Last Dividend / Price`
- **Dividend Yield (Preferred Stock)** = `(Fixed Dividend * Par Value) / Price`
- **P/E Ratio** = `Price / Dividend`
- **Volume Weighted Stock Price** = `Σ (Trade Price × Quantity) / Σ Quantity`
- **GBCE All Share Index** = `Geometric Mean of Volume Weighted Stock Prices`