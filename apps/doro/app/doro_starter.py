import pandas as pd

df = pd.read_csv("doro.csv" , encoding="cp949")

print(df.head(10))