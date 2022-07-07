#
#   graphing.py 
#       purpose: analyze and graph data from csv files  
#     
#   modified by: Calista Agmata 
#       date: 07/6/2022
#
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# read the csv into a dataFrame 
file_path = input(Enter the file path to the csv file:") 
df = pd.read_csv(file_path)

column_one = input("Enter the name of the column you want graphed as the x axis:") 
column=_two = input("Enter the name of the column you want graphed as the y axis:") 

# save the columns into seperate arrays 
x = data[column_one].to_numpy()
y = data[column_two].to_numpy()

# prompt user for graph information                  
x_label = input("Enter the desired label for x axis:") 
y_label = input("Enter the desired label for y axis:") 
title = input("Enter desired title for graph:") 

# plot graph 
plt.plot(x,y) 
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)

# calculate the mean of both columns                   
x_mean = np.sum(x)/np.size(x)
y_mean = np.sum(y)/np.size(y)

# calculate the covarience 
total = 0
for index in range(np.size(x)):
    total = total + (x[index] - x_mean)*(y[index] - y_mean)
    
covarience = total/np.size(x)

# calculate the correlation                   
correlation = covarience/(np.std(x)*np.std(y))

print("The correlation coefficent is", correlation) 

# determine which correlation is closest to: 1, 0, or -1 
distance_one = abs(correlation - 1) 
distance_zero = abs(correlation - 0) 
distance_neg_one = abs(correlation + 1) 

if distance_one < distance_zero and distance_one < distance_neg_one: 
    print("This daata has perfect positive correlation") 
elif distance_neg_one < distance_one and distance_neg_one < distance_zero: 
    print("This data has perfect negative correlation") 
else: 
    print("This data has a weak correlation") 
