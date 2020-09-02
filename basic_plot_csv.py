import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#setup df from file
filename = '090220_test3.csv'
df = pd.read_csv(filename)

#setup plot
fig, ax = plt.subplots()

#iterable of column names
columns = ['mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8']

#drop first row
df = df.iloc[1:]
print(df)

# plot all columns
for col in columns:
    ax.plot(df['time'], df[col])

# print(df['time'])

ax.set_title('plot of magnitude array')
ax.legend(['mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8'])
ax.set_xlabel('time (ms)')

plt.show()