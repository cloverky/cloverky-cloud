import pandas as pd

class walter:
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_csv("titanic-Dataset.csv")
        print(df.head(10))