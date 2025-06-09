from data_fetcher import get_option_data
from screener import screen_options
import datetime

ticker = "AAPL"
expiry = "2025-06-13"  # Make sure this matches yfinance available expiries

S, calls, puts = get_option_data(ticker, expiry)
T = (datetime.datetime.strptime(expiry, "%Y-%m-%d") - datetime.datetime.today()).days / 365
r = 0.05
sigma = 0.25

mispriced_calls = screen_options(calls, S, r, sigma, T, option_type='call', threshold=0.15)
print("\nMispriced Call Options:")
print(mispriced_calls.to_string(index=False))

