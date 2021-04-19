# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 23:52:45 2021

@author: HesamJafarian
"""
import pandas as pd
import numpy as np

data = np.empty([0,7]) #Create an empty array with size of columns
#iterate through the files, here I had 30 files from 01 to 30
for i in range(1,31):
    if i < 10 :
        temp = pd.read_csv("CollisionDataSet0%s.csv"%i)
    else:
        temp = pd.read_csv("CollisionDataSet%s.csv"%i)
    print(temp.shape) #checking the shape of the csv files to be correct
    data = np.concatenate((data,temp.values)) #concatenating the dataframe values to data array
print(data.shape) #check the final data array shape

#turn the numpy array into data frame
DF = pd.DataFrame(data)

#save the data frame into csv file excluding the header and indexes
DF.to_csv("data1.csv", index = False, header = False)
