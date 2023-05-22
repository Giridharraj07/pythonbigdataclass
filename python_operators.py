# Numerical operators in python

# + for addition
# - for substractions
# * for multiplication
# / for float division
# // for integer division
# ** for power calculation
# % for Modulus

x = 5
y = 3

print("Addition of x + y", x+y)
print("substraction of x - y", x-y)
print("multiplication of x * y", x*y)
print("float division of x / y", x/y)
print("integer division of x // y", x//y)
print("modulus of x % y", x%y)
print("power of y on x i.e; x**y", x**y)

# some operations on string
str_data = "giridhar"
empty_str = ''

#concat operation for string
full_name = str_data + " " + "raj"
print("full name = ", full_name)

#if we can use - as well ? it will not work
# minus_str = "giridhar" - "raj"
# print("minus str = ",minus_str)

# multiply_str = "giridhar" * "raj"
# print("multiply str =",multiply_str)

# power_str = "giridhar" ** "raj"
# print("power str =",power_str)

# power_str = "giridhar" ** 3
# print("power str =", power_str)


# it will work
# multiply_numeric_str = "giridhar"*5
# print("multiply numeric str =",multiply_numeric_str)

# Assgnment  operators
# =  , x = 5
# += , x += 5 -> x = x + 5
# -= , x -= 5 -> x = x - 5
# *= , x *= 5 -> x = x * 5
# /= , x /= 5 -> x = x / 5
# //= , x //= 5 -> x = x // 5
# %= , x %= 5 -> x = x % 5


# Comparison Operators (we compare operands value)
# == , Equals to condition , x == y
# != , Not Equals to condition , x != y
# > , Greater than condition , x > y
# < , Less than condition , x < y
# >= , Greater than and Equals to condition , x >= y
# <= , Less than and Equals to condition , x <= y

a = 10
b = 5
print("Result of a == b,", a == b)
print("Result of a != b,", a != b)
print("Result of a > b,", a > b)
print("Result of a < b,", a < b)
print("Result of a >= b,", a >= b)
print("Result of a <= b,", a <= b)


# Logical operators in Python(Logical check will happen for expression result)
# and -> Returns true if both statements are true
# or -> Returns true if one of statements are true
# not -> Reverse the result, returns false if the result is true

m = 10
n = 8 
print("m>10 and n<10 Result" , m>10 and n<10) # False and True -> False
print("m>20 or n<10 Result" , m>10 or n<10) # False or True -> True
print("not(m>20 or n<10) Result" ,not(m>10 and n<10)) #not(False and True) -> not(False) -> True
