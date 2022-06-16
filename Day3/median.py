#
#   median.py 
#       purpose: calcutae the median of a list of ratings 
#     
#   modified by: Calista Agmata 
#       date: 06/16/2022
#
#

import random 

def main(): 
    
    # prompt user for random amount of ratings 
    amount_stars = random.randint(5,10)
    print("Input", amount_stars,"ratings") 
    stars = input("Input ratings separated by commas:") 
    
    # use list comprehension to turn user input to list 
    stars = stars.split(",") 
    stars = [float(star) for star in stars]
    
    # sor the list 
    stars.sort() 
    
    # if the length of list is even find median by averaging two middle values 
    if len(stars) % 2 == 0:
            middle = len(stars) // 2
            median = round((stars[middle] + stars[middle-1]) / 2, 1) 
    
    # if the length is odd the median is the middle value 
    else:
            middle = len(stars) // 2
            median = stars[round(middle)]

# give user the median
print("The median rating of Harry's restaurant is", median)
