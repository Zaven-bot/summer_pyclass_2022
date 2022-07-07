# flights.cpp
# 
# Purpose: Calculate the layover time and total time of a trip.
# Author: Ian Unebasami
# Credits:
# Known Bugs: N/A


def main():
    # Receive flight times
    firsttrip = input("Morning Departure and Arrival: ")
    time_list = firsttrip.split()
    h1 = int(time_list[0])
    m1 = int(time_list[1])
    h2 = int(time_list[2])
    m2 = int(time_list[3])

    secondtrip = input("Night Departure and Arrival: ")
    scnd_time_list = secondtrip.split()
    h3 = int(scnd_time_list[0])
    m3 = int(scnd_time_list[1])
    h4 = int(scnd_time_list[2])
    m4 = int(scnd_time_list[3])

    print("You created the lists of dept and arr times")

    dep1 = time_in_min(h1, m1)
    arr1 = time_in_min(h2, m2)
    dep2 = time_in_min(h3, m3)
    arr2 = time_in_min(h4, m4)

    #Compute difference in times and print
    layover = time_difference(dep2, arr1)
    total_travel_time = time_difference(arr2, dep1)
    print_layover(layover)
    print_total(total_travel_time)



# time_in_min
# Parameters: hour, which is the number of hours in a time
#             min, which is the number of minutes in a given time
# Purpose:    Converts the hours value and minutes value to only minutes.
#             
# Returns:    Returns the above mentioned minutes value.
# Effects:    R
# Notes:      
def time_in_min(hour, min):
    
    return hour * 60 + min
    
    

# time_difference
# Parameters: int time1, which is the time in minutes of one time
#               int time, which is the time in minutes of another time
# Purpose:    Calculates the difference between the given times in munutes.
#               Returns that value.
# Returns:    
# Effects:    
# Notes:      
def time_difference(time2, time1):
    
    return time2 - time1
    
    

# print_layover
# Parameters: int layover, which is the number of minutes the layover was
# Purpose:    Calculates how many hours and (remainder) minutes the layover
#              was. Prints that value out with correct print statement.
# Returns:    
# Effects:    Prints a message to standard output.
# Notes:      
def print_layover(layover):
    
    layover_h = int(layover / 60)
    layover_m = int(layover % 60)
    print("Layover:", layover_h, "hr", layover_m, "min") 

    

#  print_total
# Parameters: int total, which is the number of minutes the total trip was
# Purpose:    Calculates how many hours and (remainder) minutes the total trip
#              was. Prints that value out with correct print statement.
# Returns:    
# Effects:    Prints a message to standard output.
# Notes:      
def print_total(total):
    total_h = int(total / 60)
    total_m = int(total % 60)
    print("Total:", total_h, "hr", total_m, "min")


    
main()
