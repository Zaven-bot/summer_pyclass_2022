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

# prompt the user for a random amount of ratings 
amount_stars = random.randint(5,10) 
print("Input", amount_stars, "ratings") 
stars = input("Input ratings sepreated by commas:") 

# use list comprehension to turn user input to a list 
stars = stars.split(",") 
stars = float(star) for star in stars] 

# calculate the mean rounded to one decimal point 
total = 0 
divisor = len(stars) 
for star in stars: 
    total = total + star 
mean = round(total/divisor, 1) 

# give user the mean 
print("The mean of the ratings for Harry's restaurant is", mean) 
