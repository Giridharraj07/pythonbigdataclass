# declare empty list
L1 = []
# print(type(L1))
print("initial length of list :",len(L1))

# insert values in list
L1.append(5)
L1.append(7)
L1.append(8)
print(L1)

# create a list of 1000 numbers start from 1 to 1000
# int_list = []
# for num in range(1,1001):
#     int_list.append(num)

# how to calculate the length of a list
len_of_list = len(L1)
print("Length of a list : ",len_of_list)

# how to check if list are equal to each other?
list1 = [1,"giridhar",20,"hi"]
list2 = [1,"giridhar",20,"hi"]
print("list are equal ??",list1 == list2)

list1 = [1,"giridhar",20,"hi"]
list2 = [1,"giridhar","hi",20]
print("list are equal ??",list1 == list2)

# list concat
list4 = [1,2,3,4,5]
list5 = [80,90,100,110]
result = list4 + list5
print(result)

# how to access list values
list6 = [10,15,20,25,30,35]

# print all the elements of given list - option 1
for num in list6:
    print(num)

# print 3rd elements of given list - option 2
# syntax = list_name[index]

print(list6[2])

# print all

print(list6[0])
print(list6[1])
print(list6[2])
print(list6[3])
print(list6[4])
print(list6[5])

# what will happen ?
# answer will be index out of range
# print(list6[100])

list7 = [1,"giridhar",1000]
print(list7)

# how to update the value of list index item ?
# update giridhar to molu

list7[1] = "molu"
print(list7)

# how to print list elements using length ?

for index in range(0, len(list7)): # range(0, 3) -> [ 0, 1, 2]
    print(list7[index])

 
list8 = [1 ,2 , 50, "giridhar", [6, 6, 6 ] , "molu"]

print(len(list8)) # what will be the output ???

# difference between append() and extend()  
list9 = [20,30,40]
list10 =["hi","hello","bye"]
list9.append(list10)
print("output of append : ", list9)
print("length after append : ", len(list9))

list11 = [20,30,40]
list12 =["hi","hello","bye"]
list11.extend(list12)
print("output of extend : ", list11)
print("length after extend : ", len(list11))

# list slicing
list13 = [20,30,40,50,60,80,90]
# syntax -> list name[start : end]
# end index is exclusive
print(list13[0 : ])
print(list13[3 : ])
print(list13[ : ])
print(list13[ 0 : 4 ])
print(list13[ 2 : 6 ])
print(list13[0 :: 2 ]) # 3rd value is for step -> 0 + 2 


# how the print the last value of the list??
print(list13[len(list13)-1])
print(list13[-1]) # negative index -1 means last element of the list

# print second last element from the list??
print(list13[-2])

# print input list in reverse direction
print(list13[-1 :: -1 ])