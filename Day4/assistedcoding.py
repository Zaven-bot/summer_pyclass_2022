import random

#### Problem 1 ####

# Taylor wants to create a function that will simulate the game rock, paper, scissors.
# Use the random library to create the computer's choice.


# Executes RPS Game
def main():
robot = comp_choice()
user = user_choice(input("Enter rock (r), paper (p), or scissors (s): "))
if (robot == 0):
    rock_compare(user)
if (robot == 1):
    paper_compare(user)
if (robot == 2):
    scissors_compare(user)


# comp_choice()
# Parameters: 
# Purpose:    Generates a random choice of "r" "p" or "s" 
# Returns:    Returns a number from 0 to (and including) 2
# Effects:    
# Notes:      
def comp_choice():
    return random.randint(0, 2)



# user_choice()
# Parameters: choice = A string of either "r" "p" or "s"
# Purpose:    Receives the user's letter input and changes it into its respective number.
# Returns:    Returns the choice's number version.
# Effects:    
# Notes:      
def user_choice(choice):
if (choice == "r"):
    return 0
if (choice == "p"):
    return 1
if (choice == "s"):
    return 2
return 0

    
    
# rock_compare()
# Parameters: user = A integer of either 0, 1, 2.
# Purpose:    When the computer chooses rock, this function will compare the user's choices with rock.
# Returns:    
# Effects:    Prints appropriate win, lost, or tied message.
# Notes:      
def rock_compare(user):        
if (user == 0):
    print("You tied. The computer chose rock.")
if (user == 1):
    print("You won! The computer chose rock.")
if (user == 2):
    print("You lost. The computer chose rock.")

        
        
# paper_compare()
# Parameters: user = A integer of either 0, 1, 2.
# Purpose:    When the computer chooses paper, this function will compare the user's choices with paper.
# Returns:    
# Effects:    Prints appropriate win, lost, or tied message.
# Notes:      
def paper_compare(user):        
if (user == 0):
    print("You lost. The computer chose paper.")
if (user == 1):
    print("You tied. The computer chose paper.")
if (user == 2):
    print("You won! The computer chose paper.")


        
# scissors_compare()
# Parameters: user = A integer of either 0, 1, 2.
# Purpose:    When the computer chooses scissors, this function will compare the user's choices with scissors.
# Returns:    
# Effects:    Prints appropriate win, lost, or tied message.
# Notes:    
def scissors_compare(user):        
if (user == 0):
    print("You won! The computer chose scissors.")
if (user == 1):
    print("You lost. The computer chose scissors.")
if (user == 2):
    print("You tied. The computer chose scissors.")
        
        
main()
