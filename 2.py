'''
task: given colleges database compute a metric 'diversity' defined as number of ethnicities with more than 0.15% student presence in the institution
'''


import pandas as pd

debug = 0
colleges = pd.read_csv("./data/college.csv",index_col="INSTNM")

colleges_udg =  colleges.filter(like="UGDS_")

if debug: print colleges_udg.head(2)
if debug: print colleges_udg.dropna().head(10)
if debug: print colleges_udg.dropna(how='all').head(10)

colleges_udg = colleges_udg.dropna(how='all')

diversity_metric = colleges_udg.ge(.15).sum(axis='columns')
print diversity_metric.head(10)
print diversity_metric.value_counts()

