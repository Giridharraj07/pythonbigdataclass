# how to use break statements
# int_list = [1,5,7,8,19,13,17,3]

# find the even value in the given list
# for num in int_list:
#     print("current element of the list =",num)
#     if num%2 == 0:
#         print("even number in the list =",num)
#         break


# # what is break is removed ?  

# for num in int_list:
#     print("current element of the list =",num)
#     if num%2 == 0:
#         print("even number in the list =",num)

# how to use continue keyword ?  
# print the numbers from for loop  and star them from value 1
# but print values on terminal if number is greater than 10


for num in range(1,21): # range(1,21)->[1,2,3,4,5,6.......20]
    if num<10:
        continue
    print(num)
 
        