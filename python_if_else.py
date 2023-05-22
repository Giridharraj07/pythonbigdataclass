# How to use If-Else in python

x = 10
y = 5

if x==y:
    print("Yes, X is Equals to Y !!")
else:
    print("NO, X is Equals to Y !!")   

# Is it mandatory to use else block with if?

a = 50

if a==50:
    print("Yes, A is Equals to 50 !!")

print("Bye !!") 

a = 40

if a==50:
    print("Yes, A is Equals to 50 !!")

print("Bye !!") 

# Nested if-else condition
marks = 88

if marks>90:
    print ("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A") 
elif marks>=70 and marks<80:
    print("Grade B+") 
elif marks>=60 and marks<70:
    print("Grade B") 
else:
    print("Grade C")       

marks = 54

if marks>90:
    print ("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A") 
elif marks>=70 and marks<80:
    print("Grade B+") 
elif marks>=60 and marks<70:
    print("Grade B") 
else:
    print("Grade C")  