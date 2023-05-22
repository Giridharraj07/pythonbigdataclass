#Write a program to display only those numbers from a list that satisfy the following conditions
#- The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
# ```numbers = [12, 75, 150, 180, 145, 525, 50]'''
numbers = [12, 75, 150, 180, 145, 525, 50] 
numbers1 = [] 
for i in numbers: 
    if i%5==0: numbers1.append(i) 
    elif i>150: numbers1.remove(i) 
    elif i>500:  break
    for i in numbers1: 
        print(i)