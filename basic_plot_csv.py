import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#setup df from file
filename = 'test1'
df = pd.read_csv(filename)

#setup plot
fig, ax = plt.subplots()

#iterable of column names
columns = ['mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8']


for col in columns:
    ax.plot(df['time'], df[col])

plt.show()