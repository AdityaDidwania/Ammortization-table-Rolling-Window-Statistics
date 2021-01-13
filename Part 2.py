# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 17:31:43 2020

@author: Aditya Didwania
"""

import pandas as pd
base_data=pd.read_csv(r'C:\Users\Aditya Didwania\Desktop\Brandeis\Sem II\Bus 215 Python and Applications to Business Analytics\Assignment 2\GOOG.csv')
# creating dataframe
df=pd.DataFrame(base_data)
# count rows in the data
total_count=len(df)

# input the window size for rolling statistics
window_size=input("Window Size? ")
while int(window_size)>total_count is not True:
    print("Enter number smaller than total data count")
    window_size=input("Window Size? ")
    
window_size=int(window_size)

# for loop to get the rolling statistics
final_output=[]
i=0
for i in range(0,total_count-window_size+1):
    data=pd.DataFrame(base_data[['Date','Adj Close']][0+i:window_size+i]) # dataset according to window size
    i=i+1
    date=data.at[i-1,'Date']
    maximum=data.max()  # maximum value in the dataset
    minimum=data.min()  # minimum value in the dataset
    max=maximum[1:]
    min=minimum[1:]
    range1=list(max-min)[0]
    average=list(round(data.mean(),2))[0]
    median=list(round(data.median(),2))[0]
    standard_deviation=list(round(data.std(),2))[0]
    output=[date,standard_deviation,median,average,range1]  # creating a list of required statistics
    final_output.append(output)
     
# fill list into a dataframe
z=pd.DataFrame(final_output,columns=("Date","Standard Deviation","Median","Average","Range"))
print()
print(z)

# plotting graph
z.plot(x='Date',y=["Median","Average"],kind='line')
z.plot(x='Date',y=["Standard Deviation","Range"],kind='line')








