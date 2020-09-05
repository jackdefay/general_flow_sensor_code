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

#assume the first 10 frames (1 second) is reasonably representative of the inherent differences in the sensors
#should check this assumption with the basic plot and modify accordingly
averages = [0, 0, 0, 0, 0, 0, 0, 0]

#sum up the samples
for i in range(20):
    for n in range(8):
        averages[n] += df[columns[n]].iloc[i+800]

#divide by number of samples
for n in range(8):
    averages[n] /= 20

print(averages)

#subtract these averages from each column
for n in range(8):
    df[columns[n]] = df[columns[n]] - averages[n]

# print(df.head)

#then subtract off a running average from sensors 6-8 as a proxy for background wind speed
#in this trial there were no bees interacting with those sensors
#code for experiment3

# for index in range(df.shape[0]):
#     tempAverage = 0
#     for m in range(5, 8):
#         tempAverage += df[columns[m]].iloc[index]
#     tempAverage /= 3
#     for m in range(8):
#         df[columns[m]].iloc[index] = df[columns[m]].iloc[index] - tempAverage

# plot all columns
for col in columns:
    ax.plot(df['time'], df[col])

# print(df['time'])

ax.set_title('plot of magnitude array')
ax.legend(['mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8'])
ax.set_xlabel('time (s)')

plt.show()