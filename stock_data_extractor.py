import yfinance as yf
import pandas as pd
from datetime import datetime

# Define stock symbols
symbols = ['AAPL', 'MSFT', 'GOOGL']

# Fetch data for each symbol
all_data = []

for symbol in symbols:
    stock_data = yf.download(symbol, period="1d", interval="1m")  # 1-day data, 1-min interval
    stock_data.reset_index(inplace=True)
    stock_data['Symbol'] = symbol
    stock_data['Extraction_Timestamp'] = datetime.utcnow()
    all_data.append(stock_data)

# Combine all data
df = pd.concat(all_data)

# Select required columns and rename
df = df[['Symbol', 'Datetime', 'Open', 'High', 'Low', 'Close', 'Volume', 'Extraction_Timestamp']]
df.rename(columns={'Datetime': 'Date'}, inplace=True)

# Save to CSV
df.to_csv('stock_data_output.csv', index=False)

# Optional: Save as Parquet
# df.to_parquet('stock_data_output.parquet', index=False)

print("Stock data extracted and saved.")
