import pandas as pd

df = pd.read_csv("csv\\customers-100.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.head())