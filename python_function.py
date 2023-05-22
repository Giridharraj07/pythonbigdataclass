#  Function in python
# What about len()

# Examples of inbuilt functions
# list1 = [1,2,3,4,5,6]
# print("Maximum number from list : ", max(list1))
# print("Minimum number from list : ", min(list1))
# print("Sum number from list : ", sum(list1))

# How do functions works?
# They may or may not accepts input parameter
# They may or may not return any output


# example of a function which doesn't accept any parameter
# and doesn't return anything

def welcome_message():
    print("welcome to ineuron batch-2 !!!")
    
welcome_message()

# example of a function which doesn't accept any parameter
# and does return something

def bot_message():
    print("message from bot using print")
    return "message from bot!!"

print(bot_message())

result = bot_message()
print("output from bot_message()",result)

# example of a function which  accepts some parameter
# and return the vlues 

def avg_of_two_nums(a,b):
    count=2
    print("first value :",a)
    print("last value: " ,b)
    avg_result =(a+b)/2
    return avg_result

num1 = 10
num2 = 15
output = avg_of_two_nums(num1,num2)
print("result of avg_of_two_nums functions :",output)

# output1 = avg_of_two_nums(num1)
# print("result of avg_of_two_nums functions :",output1) 

# write a function to calculate the factorial of a num ?

def factorial(n):

    if n == 0  or n == 1:
        return 1

    result = 1
    for num in range(1,n+1):
        result = result*num
    
    return result 

x =5
ans = factorial(x)
print("factorial of number",x,"=",ans)

x =0
ans = factorial(x)
print("factorial of number",x,"=",ans)

# how to return multiple values from function
# a=2
# b=3
# c=5 for normal

a , b, c = 2 , 3, 5    # for python one liner
print("value of a is :" ,a)
print("value of b is :" ,b)
print("value of c is :" ,c)

def square_and_cube(n):
    sqr = n*n
    cube = n*n*n

    return sqr,cube

num = 3

sqr_ans, cube_ans = square_and_cube(num)
print("square of ",num," is :",sqr_ans)
print("cube of ",num," is :",cube_ans)

# how to create optional arguments in python functions
def multiply(a,b=3):
    result = a*b
    return result

num1=5
num2=10
print(multiply(num1,num2))    
print(multiply(num1))
print(multiply(num2))

# what if we reverse this part
# not possible
#def multiply( a=3,b):
    # result = a*b
    # return result

# what if we have more than 2   
def multiply(a,b=3,c=10):
    result = a*b*c
    return result

num1=5
num2=10
num3=2
print(multiply(num1,num2,num3))    
print(multiply(num1,num2))
print(multiply(num2,num3))
print(multiply(num3))

# non-key valued arguments

def example_nonkeyed_args(*argv ):
    for param in argv:
        print(param)

example_nonkeyed_args('hello', 'welcome','to','ineuron')



# key value type of arguments in python
def example_of_kwargs(**kwargs):
    print("value of host: ",kwargs['host'])
    print("value of port: ",kwargs['port'])
    print("value of password: ",kwargs['pswd'])
    for k,v in kwargs.items():
        print("key is",k, 'and value is',v)

example_of_kwargs(host='170.80.80.80',port=9021,pswd='XXFGH') 
 
