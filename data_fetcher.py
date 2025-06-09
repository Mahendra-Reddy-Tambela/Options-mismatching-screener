import yfinance as yf

def get_option_data(ticker_symbol, expiry_date):
    ticker = yf.Ticker(ticker_symbol)
    options = ticker.option_chain(expiry_date)
    return ticker.info['regularMarketPrice'], options.calls, options.puts

def get_expiry_dates(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    return ticker.options

