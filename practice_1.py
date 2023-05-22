#first way to know how many keywords in python.
import keyword
print("keywords are:")
print(keyword.kwlist)
# all keyword store in one variable
import keyword
keyword.kwlist
x=keyword.kwlist
print(x)    
print(len(x))        # keyword=35
# second way to know how many keywords in python
help('keywords') # keywords=35 we understand all the keywords one by one through help('keyword name like as if else etc')

list= [1,2,3]
list.append(4)    #only one argument valid like as- list.append(4,5) not valid only list.append(4)
print(list)

#1=list(1,2,3)   #SyntaxError: cannot assign to literal

#output-'''ineuronineuronineuronineuron''' Write a code?
str_data = "'''ineuronineuronineuronineuron'''"
print(str_data)#output-'''ineuronineuronineuronineuron'''

#Write a code to take a number as an input from the user and check if the number is odd or even.
num=10
if num%2==0:
    print("num is even :",num)
else:
    print("num is odd :",num)   #num is even : 10

num=7
if num%2==0:
    print("num is even :",num)
else:
    print("num is odd :",num)  #num is odd : 7
    

# # m=5
# # n=1
# # print("m>1 and n<1 Result" , m>1 and n<1)
# # print("m>4 or n<1 Result", m>4 or n<1)

#Q19-A19
print("'''1 or 0\n 0 and 0\n true and false and true \n 1 or 0 or 0'''")

#How can we declare string in Python?
str1="giri"
print(str1)
#How can we access the string using its index? 
w= "giri"
print(w[1])
#Q-Write a code to get the desired output of the following.
     #string = "Big Data iNeuron"
     #desired_output = "iNeuron"

string="big data ineuron"
# split the string by spaces
words = string.split(" ")
# Extract the last word
desired_output = words[-1]
print(desired_output)
#and way-
string="Big Data iNeuron"
print(string[9:16]) 
#Q-Write a code to get the desired output of the following
      #string = "Big Data iNeuron"
      #desired_output = "norueNi"
string = "Big data iNeuron"
# Extract the substring "iNeuron"
substring = string.split(" ")[-1]
# reverse the substring
reversed_substring = substring[::-1]
print(reversed_substring)
#2nd way-string = "Big Data iNeuron" 
temp_string = string[-7: ]
new_string = temp_string[::-1  ] 
print(new_string) 
#Q--Resverse the string given in the above question.
# 
string = "Big Data iNeuron" 
temp_string = string[:16] 
new_string = temp_string[::-1] 
print(new_string)
#How can you print the below string?
print("iNeuron's Big Data Course")
#create list
list1=[7,'giri','big data',2023]    #1 Way
print(list1)
list2= []                            #2 way
print(type(list2))
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])
#Take a list as an input from the user and find the length of the list.
list=[7,9,1995,'giri',5.11]
print(len(list))
#Q39. Add the word "Big" in the 3rd index of the given list
#list = ["Welcome", "to", "Data", "course"]
list1=["Welcome", "to", "Data", "course"]
list1.insert(2,"Big")
print(list1)
# create tuple
t1=()
#Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

# list1=["giri","raj","dhar"]
# list1[2]="giridhar"
# print(list1)
# in list possible.
t1=("giri","raj","dhar")
t1[3]="giridhar"
print(t1)
#no its not possible to add a new item in a tuple because it is unchangable .
