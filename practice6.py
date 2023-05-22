# How can we add an element in a dictionary?
my_info={"name":"giridhar","Age":27,"city":"varanasi"}
my_info['Occupation']='Job'
print(my_info)
#Create a dictionary and access all the values in that dictionary.
# Create a dictionary
my_info={"name":"giridhar","Age":27,"city":"varanasi"}

# Access all values in the dictionary using the values() method
all_values = my_info.values()

# Print all the values
print(all_values)
#Create a nested dictionary and access all the element in the inner dictionary.
my_info={"name":"giridhar","Age":27,"city":"varanasi",
"my_info2":{"name":"Nidhi","Age":26,"city":"varanasi"}}
# Access all values in the dictionary using the values() method
all_values = my_info.values()
# Print all the values
print(all_values)
#Write a Python program to find the factorial of a given number.
i=int(input("enter number:"))  
fac=1
while i>0:
    fac=fac*i
    i=i-1
print("factorial=",fac)

#Write a Python program to check if a number is prime or not
n=int(input("enter number:"))
count=0
i=1
while (i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime")
else:
    print("not prime")

