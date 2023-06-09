# write a program to generate list of 10 numbers
result=[]
for i in range(1,11):
    result.append(i)
print(result)    

# how to do it with the help of list comprehension?
result=[x for x in range(1,11)]
print(result)

# get a list of all even numbers between 1 to 50
result = [ x for x in range(1,51) if x % 2 == 0]
print(result)

# get a list of all even numbers from given list
list_a=[1,2,4,3,6,7,9]
result = [ x for x in list_a if x % 2 == 0]
print(result)

# convert all strings into upper case in given list
list_a = ['hi','hello','bye','nice']

result = [x.upper() for x in list_a]
print(result)

# put all negative numbers after positive numbers from given list
list_a = [1,-1,2,-5,9,10,-6]

# result1= [x for x in list_a if x>0]
# result2= [x for x in list_a if x<0]
# print(result1+result2)

result = [x for x in list_a if x>0] + [x for x in list_a if x<0]
print(result)