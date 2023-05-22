
# Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100
p=int(input("enter principal:"))
t=int(input("enter time:"))
r=int(input("enter rate:"))
si=p*r*t/100
print("simple interest is:",si)



#Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t
p=int(input("enter principal:"))
t=int(input("enter time:"))
r=int(input("enter rate:"))
amount = p*(pow((1+ r/100),t))
ci=amount-p
print("compound interest is:",ci)

# Write a Python program to check Armstrong Number.
i=int(input("enter number to check for armstrong:"))
sum=0
orig=i
while(i>0):
    sum=sum + (i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("armstrong")
else:
    print("not armstrong")  



