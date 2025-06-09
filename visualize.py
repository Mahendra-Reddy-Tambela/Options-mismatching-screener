import streamlit as st
import datetime
from data_fetcher import get_option_data, get_expiry_dates
from screener import screen_options

st.set_page_config(page_title="Options Mispricing Screener", layout="centered")

st.title("📊 Options Mispricing Screener")

symbol = st.text_input("Stock Symbol", value="AAPL").upper()

# Dynamically fetch expiry dates
try:
    expiries = get_expiry_dates(symbol)
    expiry = st.selectbox("Select Expiry Date", expiries)
except:
    st.error("Invalid stock symbol or no options available.")
    st.stop()

# Risk-free rate and volatility
r = st.number_input("Risk-Free Rate (r)", min_value=0.0, max_value=1.0, value=0.05)
sigma = st.number_input("Implied Volatility (σ)", min_value=0.0, max_value=1.0, value=0.25)
threshold = st.slider("Mispricing Threshold (%)", min_value=0.01, max_value=0.5, value=0.15)

option_type = st.radio("Option Type", ["call", "put"])

if st.button("Run Screener"):
    try:
        S, calls, puts = get_option_data(symbol, expiry)
        df = calls if option_type == "call" else puts
        T = (datetime.datetime.strptime(expiry, "%Y-%m-%d") - datetime.datetime.today()).days / 365

        results = screen_options(df, S, r, sigma, T, option_type, threshold)
        st.write(f"💡 Mispriced {option_type.capitalize()} Options")
        st.dataframe(results.reset_index(drop=True))
    except Exception as e:
        st.error(f"Error fetching or processing data: {e}")


##****** To run this file use Streamlit run visualize.py in the terminal ******##