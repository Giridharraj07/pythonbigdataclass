# Write a Python program to find the n-th Fibonacci Number.
terms=int(input("enter the number of terms:"))
n1=0
n2=1
count=0
if(terms<=0):
    print("please enter valid terms")
elif(terms==1):
    print(n1)
else:
    print("fibonacci number")
    while(count<terms):
        n3=n1+n2
        print(n1)
        n1=n2
        n2=n3
        count +=1
#  Write a Python program to interchange the first and last element in a list.
lst=[1,2,3,4,5]
lst[0],lst[-1] = lst[-1],lst[0] 
print(lst)
#  Write a Python program to find N largest element from a list
a=[]
size=int(input("enter size of the list:"))
for i in range(size):
    val=int(input("enter number:"))
    a.append(val)
max=a[0] 
for i in range(size):
    if(a[i]>max):
        max=a[i]
print("max number=",max)   
# Write a Python program to find cumulative sum of a list.
def cumsum(s):
    sm=0
    cum_list=[]
    for i in s:
        sm=sm+i
        cum_list.append(sm)
    return cum_list   
s=[10,20,30,40,50]  
print(cumsum(s))  
#Write a Python program to check if a string is palindrome or not
a=input("enter string:")
b=a[-1::-1]
if(a==b):
    print("palindrome string")
else:
    print("not palindrome")
#Write a Python program to remove i'th element from a string
s=input("enter the string:")
n=int(input("enter the value of i"))
a=s[0:n-1]
b=s[n:]
print("resultant string is",a+b)
#Write a Python program to check if a substring is present in a given string
s=input("Enter the string:")
sub=input("enter the substring:")
if(s.find(sub)>0):
    print("present")
else:
    print("not present")
        