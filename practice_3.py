#to check any number print on terminal "python practice_3.py" then get result
#Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

user_input=int(input("enter the age :"))
if user_input >=18:
    print("i can vote")
else:
    print("i can't vote")    
#Q23. Write a code that displays the sum of all the even numbers from the given list.numbers = [12, 75, 150, 180, 145, 525, 50]

list_a=[12, 75, 150, 180, 145, 525, 50]
result = 0
for item in list_a:
    if not item%2:
        result+=item
print(result)        

#Write a code to take 3 numbers as an input from the user and display the greatest no as output.
number1 = int(input("enter first number :"))
number2 = int(input("enter second number :"))
number3 = int(input("enter third number :"))

if number1>number2 and number1>number3:
    print(number1,"is larger")
elif number2>number1 and number2>number3:
    print(number2,"is larger")  
else:
    print(number3,"is larger") #if number in decimal then "int" replace into "float"


