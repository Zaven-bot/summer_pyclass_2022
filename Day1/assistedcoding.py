# 
#    assistedcoding.py
#        purpose: visual learning tool for Day 1 Coding Session
#
#    modified by: Ian Unebasami
#           date: 06/08/2022
#       

def main():
    # Problem 1: Katie hiked seven miles north and three miles east. Print the exact amount of miles she is from her starting point. 

    #these are variables they are containers for data
    north = 6 
    east = 8 

    #this is the distance formula, follows PEMDAS 
    distance =  (north**2 + east**2)**(1/2)

    #print the distance from origin to terminal
    print(distance)


    # Problem 2: Katie is biking in the city and she bikes 21120 feet south and 15840 feet west. Print the exact amount of miles she is from his starting point.

    south = 21220
    west = 15840

    #convert to miles 
    south = 21120 / 5280
    west = 15840 / 5280

    #variables are lowercased and use underscore as spaces 
    new_distance = (south**2 + west**2)**(1/2)

    print(new_distance)

    # Problem 3: Taylor is swimming at a beach and they doggy paddle from the coordinates (4,6) to (7,-5). Print how far they traveled in the format, “Taylor doggy paddled ___ units”. 

    x_one = 4
    y_one = 6
    x_two = 7
    y_two = -5

    swimming_distance = ((x_one - x_two)**2 + (y_one - y_two)**2)**(1/2)

    #strings, collection of characters, represented by ""
    #print a variable by separating it from string with commas 
    print("Taylor paddled", swimming_distance, "units")

main()
