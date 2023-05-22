# Write a Python program to merge two dictionary.
# dict1={"john":88,"lisa":55}
# dict2={"kile":99,"giri":100}
# dict3={**dict1,**dict2}
# print(dict3)
# #Write a Python program to convert a list of tuples into dictionary.
# lt=[('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
# dictionary=dict(lt)
# print('my dictionary',dictionary)
#Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
def create_tuple_list(numbers):
    tuple_list=[]
    for num in numbers:
        tuple_list.append((num,num**3))
    return tuple_list
#example
numbers=[9,5,6]
tuple_list=create_tuple_list(numbers)
print(tuple_list)
# Write a Python program to get all combinations of 2 tuples

#Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8) 
#Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

tuple1 = (7, 2)
tuple2 = (7, 8) 
print("First tuple : " + str(tuple1)) 
print("Second tuple : " + str(tuple2))

#finding all pair Combination of tuples
pairCombi = [] 
for val1 in tuple1: 
    for val2 in tuple2: tup = [val1, val2] 
    pairCombi.append(tuple(tup))

for val1 in tuple2: 
    for val2 in tuple1: tup = [val1, val2] 
    pairCombi.append(tuple(tup))

print("All pair Combinations are : " + str(pairCombi))
# Write a Python program to sort a list of tuples by second item
lst=[('for', 24), ('Geeks', 8), ('Geeks', 30)] 
lst_sorted=sorted(lst,key=lambda x:x[1])
print(lst_sorted)

# Write a python program to print below pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
n=5
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()
 # Write a python program to print below pattern
#     *
#    **
#   ***
#  ****
# *****
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="") 
    print()
# Write a python program to print below pattern.

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *   
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(" *",end="") 
    print()
# Q99. Write a python program to print below pattern.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
n=5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
#Write a python program to print below pattern
# A 
# B B 
# C C C 
# D D D D 
# E E E E E
for i in range(65,70):
    for j in range(i-64):
        print(chr(i),end=" ")
    print()
#-When we define a class that inherits all the properties of other class called inhertance.
class father:
    def lands(self):
        print("having 50 accre lands")
class son(father):
    def money(self):
        print("having 10 lakhs money")

s=son()
s.lands()
s.money()