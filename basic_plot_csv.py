import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

#setup df from file
filename = '090320_experiment5.csv'
df = pd.read_csv(filename)

#setup plot
fig, ax = plt.subplots()

#iterable of column names
columns = ['mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8']

#first time shows the global time.
print(str(time.ctime(df['time'].iloc[0])))
#drop first row
df = df.iloc[1:]
# print(df)

# plot all columns
for col in columns:
    ax.plot(df['time'], df[col])

# print(df['time'])

ax.set_title('plot of magnitude array')
ax.legend(['mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8'])
ax.set_xlabel('time (s)')

plt.show()