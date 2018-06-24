'''
task : boolean filtering on stock prices
'''
import pandas as pd
aapl = pd.read_csv('./data/aapl_stock.csv', index_col="Date")['Close']
meta = aapl.describe(percentiles=[.1,.9])
top_10 = meta.loc['90%']
bottom_10 = meta.loc['10%']
filter = ((aapl > top_10) | (aapl < bottom_10))
print("this is the boolean filter",filter.head(10))
aapl = aapl[filter]
print("this is the filterd stock price between {} and {}".format(top_10,bottom_10),aapl.head(10))
