# Declare & Assign Variables in python

int_var = 10
float_var = 18.25
string_var = 'ineuron batch2' # or another way "ineuron batch2"
bool_var = True # if we want to assign false then it should be like false


# Function in python for output
# function does what ? they might not accept some perameter
print("hello world !!!!")

# print variables values in python
print("value of int_var = ",int_var," -Result Done!!")
print("value of float_var = ",float_var," -Result Done!!")
print("value of string_var = ",string_var," -Result Done!!")
print("value of bool_var = ",bool_var," -Result Done!!")

# how to check the data type of any variable
# We can use type () function
print("Type of int_var ?", type (int_var))
print("Type of float_var ?", type (float_var))
print("Type of string_var ?", type (string_var))
print("Type of bool_var ?", type (bool_var))

# how to do the type casting in python ??
# int() , float() , str(), bool()
int_var = int_var + 10 # int_var = 10 + 10 and in next step int_var = 20
casted_int_var = float(int_var)
casted_float_var = int(float_var)
print("Int to Float Typecasting for int_var = ", casted_int_var)
print("Float to Int Typecasting for float_var = ", casted_float_var)

numeric_str = "123"
#numeric_str = numeric_str + 50 # is it valid ?? numeric_str = "123" + 50
#print("Value of numeric _str = ", numeric_str)


numeric_str = int(numeric_str) + 50 # numeric_str = int("123") + 50 -> 123+50 = 173
print("Value of numeric _str = ", numeric_str)

# How to Take the inputs in python ?
# we can use input() function

name = input()
age = input()
print("User name =  ",name)
print("User age =  ",age)

# Another way to take user input with  custom message
# name = input("Enter value for name = ")
# age = input("Enter value for age = ")
# print("User name =  ",name)
# print("User age =  ",age)

name = input("Enter value for name = ")
age = int(input("Enter value for age = "))
print("User name =  ",name)
print("User age =  ",age)

print("Type of name = ", type(name))
print("Type of age = ", type(age))