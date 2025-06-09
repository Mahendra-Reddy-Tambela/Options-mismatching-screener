from black_scholes import black_scholes_price
import pandas as pd

def screen_options(df, S, r, sigma, T, option_type='call', threshold=0.1):
    df = df.copy()
    df['BS_Price'] = df.apply(
        lambda row: black_scholes_price(S, row['strike'], T, r, sigma, option_type),
        axis=1
    )
    df['Mispricing'] = (df['lastPrice'] - df['BS_Price']) / df['BS_Price']
    mispriced_df = df[abs(df['Mispricing']) > threshold]
    return mispriced_df[['strike', 'lastPrice', 'BS_Price', 'Mispricing']]

