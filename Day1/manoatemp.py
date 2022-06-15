# 
#    manoatemp.py
#        purpose: report the temperature of Manoa in degrees Celsius
#
#    modified by: Ian Unebasami
#           date: 06/08/2022
#       


# Degrees from F to C using def main():

def main():
    
    # Degrees in Fahrenheit
    Fahrenheit = 84
    
    # Calulate degrees Celsius
    Celsius = (Fahrenheit - 32) * (5 / 9)
    
    print("The temperature is", Fahrenheit, "degrees Fahrenheit in Manoa right now.", end = ' ') 
    print("This is", Celsius, "in degrees Celsius.") 

main()


# Degrees from C to F using def main()

def main():
    # Degrees in Celsius
    Celsius = 78
    # Calulate degrees Fahrenheit
    Fahrenheit = ((Celsius * 5/9) + 32)

    # Tell user the temperature in degrees Celsius
    print("The temperature is", Celsius, "degrees Celsius in Manoa right now.", end = ' ')
    print("This is", Fahrenheit, "in degrees Fahrenheit.")

main()









# Degrees from F to C not using def main():
'''
# Degrees in Fahrenheit
Fahrenheit = 0
# Calulate degrees Celsius
Celsius = (Fahrenheit - 32) * (5 / 9)

# Tell user the temperature in degrees Celsius
print("The temperature is ", Fahrenheit, " degrees Fahrenheit in Manoa right now.", end = ' ')
print("This is", Celsius, "in degrees Celsius.")
'''



# Degrees from C to F not using def main()
'''
# Degrees in Celsius
Celsius = 78
# Calulate degrees Fahrenheit
Fahrenheit = (Celsius * 5/9) + (32)

# Tell user the temperature in degrees Celsius
print("The temperature is ", Celsius, " degrees Celsius in Manoa right now.", end = ' ')
print("This is", Fahrenheit, "in degrees Fahrenheit.")
'''