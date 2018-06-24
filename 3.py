'''
task : calculate metric 'trailing-stop' , defined as 0.90% of the cumulative maximum close price of a financial instrument
'''

import pandas as pd
close = pd.read_csv('data/aapl_stock.csv')['Close']
trailing_stop = close.cummax() * 0.9
print(close.head(10))
print(trailing_stop.head(10))
