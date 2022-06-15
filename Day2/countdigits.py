# 
#    countdigits.py
#        purpose: report the temperature of Manoa in degrees Celsius
#
#    modified by: Ian Unebasami
#           date: 06/14/2022
#       
#


# Recall negative_print for functions

def main():
    
    # Prompt user for input
    print("Enter a number: ")
    num = float(input()) 

    # Truncate the number if it's not an integer. Tell user new number.
    if ((abs(num)) % 1 > 0):
        print("User entered", num, ". Number was truncated to", end = ' ' )
        num = num // 1
        print(num, ".")

    
    # Check if number has three digits or is (-) three digits, tell user
    if (num > 99):
        print("input has three or more digits")
    elif (num < -99):
        print("input has three or more digits")
        print("input is negative")
    
    # Check if number has two digits or is (-) two digits, tell user
    elif (num > 9):
        print("input has two digits")
    elif (num < -9):
        print("input has two digits")
        print("input is negative")
    
    # Check if number has one digit or is (-) one digit, tell user
    elif (num >= 0):
        print("input has one digit")
    elif (num < 0):
        print("input has one digit")
        print("input is negative")
    
main()