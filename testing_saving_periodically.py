import pandas as pd


filename = 'test1.csv'

df = pd.DataFrame([[1, 2, 3, 4]], columns=['a', 'b', 'c', 'd'])


df.to_csv(path_or_buf=filename, mode='a', index=False)