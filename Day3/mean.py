#
#   mean.py 
#       purpose: calcutae the mean of a list of ratings 
#     
#   modified by: Calista Agmata 
#       date: 06/16/2022
#
#

import random 

def main(): 

amount_stars = random.randint(5,10) 
print("Input", amount_stars, "ratings") 
stars = input("Input ratings sepreated by commas:") 

stars = stars.split(",") 
stars = float(star) for star in stars] 
total = 0 
divisor = len(stars) 
for star in stars: 
    total = total + star 
mean = round(total/divisor, 1) 
print("The mean of the ratings for Harry's restaurant is", mean) 
