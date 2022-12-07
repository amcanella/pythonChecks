# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:54:27 2022

@author: AlonsoMoránCanella
"""

import numpy as np 
import pandas as pd


'''from Tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)'''

count = 0;
index = [];
#log_file = 'prueba_FF.txt';
log_file = '22_12_6.txt' 

df = pd.read_csv(log_file, sep = ' ', header=None)
print("DATAFRAME ISSSSSS:", df)  
print("length dataframe:", len(df))

# number = df.loc[1,[]]

# for i in range(len(df)-1):
#     if (df.loc[i,:] != 'FF'):
#         count = count + 1
        
        

list_df = df.values.tolist()

#list_ff = list(df)

#print(list_df)


i = 0;
for i in range(len(list_df)):
    row = list_df[i]
    #print("row", i,"=",row )
    for x in range(len(row)-8):
        if (row[x] != 'FF'):
            count = count + 1
            index.append(x)
            print("Corruption in line", i + 1 , "byte",x)
        else:
            pass

corruption_cases = index.count(4)

corrupt = pd.Series(index).value_counts()
print("Number of corrupted bytes:", count)
print("Byte Count")
print(corrupt)


