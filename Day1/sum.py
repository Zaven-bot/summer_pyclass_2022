# 
#    sum.py
#        purpose: report the sum of a duplicated number
#
#    modified by: Ian Unebasami
#           date: 06/09/2022
#       

def main():

    # Declare and initiliaze variable
    x = 4

    # Single digit operations
    if (x < 10):
        y = x + ((x * 10) + x) + ((x * 100) + (x * 10) + x)
        print(y)

    # Double digit operations
    if (x >= 10):
        y = x + ((x * 100) + x) + ((x * 10000) + (x * 100) + x)
        print(y)

main()

