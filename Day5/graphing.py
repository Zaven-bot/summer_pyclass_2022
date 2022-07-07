import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('/User/calista_agmata/Desktop/temperature_pressure.csv')

column_one = input("Enter the name of the column you want graphed as the x axis:") 
column=_two = input("Enter the name of the column you want graphed as the y axis:") 

x = data[column_one].to_numpy()
y = data[column_two].to_numpy()

x_label = input("Enter the desired label for x axis:") 
y_label = input("Enter the desired label for y axis:") 
title = input("Enter desired title for graph:") 

plt.plot(x,y) 
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.title(title)

x_mean = np.sum(x)/np.size(x)
y_mean = np.sum(y)/np.size(y)

total = 0
for index in range(np.size(x)):
    total = total + (x[index] - x_mean)*(y[index] - y_mean)
    
covarience = total/np.size(x)

correlation = covarience/(np.std(x)*np.std(y))

print("The correlation coefficent is", correlation) 
