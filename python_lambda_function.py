# How to create lambda functions

# first normal function to add integer 5 in given number
def add_five(num):
    result = num + 5
    return result


x = 7
print(add_five(x))   

# same program using lambda function
lambda_add_five=lambda x: x+5

y=10
print(lambda_add_five(y))

# write a lambda function to add two input numbers
lambda_add_two_nums=lambda x,y:x+y

a=30
b=20
print(lambda_add_two_nums(a,b))

# write a lambda function to concatenate two strings
lambda_add_two_string=lambda x,y:x+y

a="giridhar"
b="raj"
print(lambda_add_two_string(a,b))

# write a lambda function to calculate maximum of two mnumbers
# normal way
def max_two_nums(x,y):   
    if x>y:
        return x
    else:
        return y

a = 5
b = 4
print(max_two_nums(a,b))            
# lambda way
lambda_max_two_nums = lambda x,y:x if x>y else y

num1=20
num2=10

print(lambda_max_two_nums(num1,num2))

# how to work with map(),filter(),reduce()

# implement map function
list1 = [1,2,3,4,5,6,7,8,9]

#Result
result = [1,4,9,16,25,36,49,64,81]

square_num = lambda x : x*x
square_list =list(map(square_num,list1))
print(square_list)

# add sequential respective elements in two given lists
list_a= [1,2,3,4,5]
list_b= [5,4,3,2,1]

#result=[6,6,6,6,6]
sum_two_elements = lambda x,y :x+y
result =list(map(sum_two_elements,list_a,list_b))
print(result)

# how to use reduce??

import functools

list_x=[1,2,3,4,5]

add_two_nums = lambda x,y:x+y

result=functools.reduce(add_two_nums,list_x)
print(result)                                                                    
                                                                            
# multiply all those numbers in a list from reduce manner.

multiply_two_nums = lambda x, y: x*y
result=functools.reduce(multiply_two_nums,list_x)
print(result)

# result = 0
# result = result + i

# how to use filter()
# create list of only odd elements
seq =[1,2,5,6,9,7,10]

filter_odd = lambda x : x%2 !=0


result =list(filter(filter_odd,seq))
print(result)

# create list of only even elements
seq =[1,2,5,6,9,7,10]

filter_even = lambda x : x%2 ==0


result =list(filter(filter_even,seq))
print(result)

