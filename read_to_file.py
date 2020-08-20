import numpy as np
import pandas as pd
import serial
import time


#setup time
start_time = time.time()

#set save file name
filename = 'test1'

#setup dataframe
df = pd.DataFrame([[start_time,1,2,3,4,5,6,7,8]], columns=['time', 'mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8'])


#setup the serial line
ser = serial.Serial('COM12', 9600)
time.sleep(2)

#ADD A KEYBOARD INTERRUPT TO SAVE TO FILE

def readArduino(df):
    string = ''
    ser.reset_input_buffer()
    while(ser.in_waiting < 1):
        c=0
    
    while(len(string) < 15):
        b = ser.readline()
        string_n = b.decode()
        string = string_n.rstrip()
        # print(int(time.time() - start_time) ,repr(string), sep=": ")

    stringArray = []
    stringArray = string.split(", ")
    magnitudeArray = []
    for cell in stringArray:
        magnitudeArray.append(int(cell))

    return addData(df, [magnitudeArray])

def addData(df, magnitudeArray):
    magnitudeArray[0].insert(0, (time.time() - start_time))
    frame = pd.DataFrame(magnitudeArray, columns=['time', 'mag1', 'mag2', 'mag3', 'mag4', 'mag5', 'mag6', 'mag7', 'mag8'])
    print(frame)
    return pd.concat([df, frame], axis=0)

while(True):
    try:
        df = readArduino(df)
    except KeyboardInterrupt:
        df.to_csv(path_or_buf=filename, index=False)
        print(df)
        raise