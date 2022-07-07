# 
#    Assisted Coding Session
#        purpose: Live coding session for functions
#
#    modified by: Ian Unebasami
#           date: 06/06/2022
#       

import random

#### Problem 1 ####

# Taylor wants to create a function that will simulate the game rock, paper, scissors.



def main():
    robot = comp_choice()
    print("Enter rock (r), paper (p), or scissors (s): ")
    user = user_choice(input("Input choice: "))
    if (robot == 0):
        rock_compare(user)
    if (robot == 1):
        paper_compare(user)
    if (robot == 2):
        scissors_compare(user)

def comp_choice():
    return random.randint(1, 3)

def user_choice(choice):
    if (choice == "r"):
        return 0
    if (choice == "p"):
        return 1
    if (choice == "s"):
        return 2


def rock_compare(user):        
    if (user == 0):
        print("You tied. The computer chose rock.")
    if (user == 1):
        print("You lost. The computer chose paper.")
    if (user == 2):
        print("You won! The computer chose scissors.")


def paper_compare(user):        
    if (user == 0):
        print("You won! The computer chose rock.")
    if (user == 1):
        print("You tied. The computer chose paper.")
    if (user == 2):
        print("You lost. The computer chose scissors.")


def scissors_compare(user):        
    if (user == 0):
        print("You lost. The computer chose rock.")
    if (user == 1):
        print("You won! The computer chose paper.")
    if (user == 2):
        print("You tied. The computer chose scissors.")

main()