# 
#    Functions.py
#        purpose: Provide visual learning tool for functions
#    modified by: Ian Unebasami
#           date: 06/06/2022
#       

#### Basic Structure ####

# Defining a function
#def multiply_two_numbers(num1, num2):
#   product = num1 * num2
#   return product


# Calling a function
#x = multiply_two_numbers(4,5)
#y = multiply_two_numbers(3,7)

# What is the answer?
#print(x + y)




#### Default Arguments ####

# Defining a function
#def multiply_two_numbers(num1, num2 = 2):
#   product = num1 * num2
#   return product

# Calling a function
#x = multiply_two_numbers(5)
#y = multiply_two_numbers(3,7)

# What is the answer?
#print(x + y)






#### Keyword Arguments ####

# Defining a function
#def multiply_two_numbers(num1, num2):
#    product = num1 * num2
#    return product

# Calling a function
#x = multiply_two_numbers(num2 = 5, num1 = 9)
#y = multiply_two_numbers(7, num2 = 4)

# What is the answer?
#print(x + y)






#### Arbitrary Arguments ####

# Defining a function
def multiply_many(*nums):
    x = 1
    for num in nums:
        x = x * num
    return x

# Calling a function
x = multiply_many(1, 2, 3, 4)
y = multiply_many(0.5, 2, 4, 0.25, 5)

# What is the answer?
print(x + y)



