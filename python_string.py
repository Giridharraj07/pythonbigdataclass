# Create a string in python 
str1 = "ineuron"
print(str1)

str2 = "giridhar's"
print(str2)

str3 = 'he is a "good" boy'
print(str3)

# use length function
print("length of the string: ",len(str3))

# how to write multiline string

str4 = '''giridhar is not going to attend the seminar'''
print(str4)

# string concatenation
str5 = "giridhar"
str6 ="raj"
print( str5 + str6 ) #giridharraj

str5 = "giridhar"
str6 ="raj"
print( str5 +' '+ str6 ) #giridhar raj

# string comparison 
str7 = "giridhar"
str8 ="raj"
print( str7 == str8 ) # false

str7 = "giridhar"
str8 ="giridhar"
print( str7 == str8 ) # true

# how to print the each character from the string
for char in str8:
    print(char)

print(str7[0])
print(str7[1])
print(str7[2])
print(str7[3])
print(str7[4])
print(str7[5])
print(str7[6])
print(str7[7])

str9 ="giridhar"

#update the 4th character in the string by M
# str9[3] = 'M'

# convert string into lower case
print(str9.lower())

# convert string into upper case
print(str9.upper())

# other functionalities will be same as list like slicing etc
