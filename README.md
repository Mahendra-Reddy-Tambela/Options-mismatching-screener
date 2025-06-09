# 📈 Options Mispricing Screener

A Python-based tool for detecting mispriced options by comparing real-time market prices with theoretical values calculated using the Black-Scholes model. Includes a Streamlit dashboard for interactive visualization and filtering.

## 🔍 Features

- 📊 Fetches real-time and historical options data using `yfinance`
- 🧠 Calculates theoretical option prices with the Black-Scholes formula
- ⚠️ Flags mispriced options with significant deviation thresholds (e.g., 15%)
- 🖥️ Streamlit-based dashboard for dynamic analysis and filtering
- 🔁 Backtested on 1+ year of data for performance validation

## 🛠️ Tech Stack

- **Python**  
- **yfinance** – market data  
- **NumPy, pandas, SciPy** – data handling and calculations  
- **Streamlit** – interactive UI  
- **Black-Scholes Model** – options pricing

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/options-mispricing-screener.git
cd options-mispricing-screener
