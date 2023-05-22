# syntax
# while exp:
#     statements

# write a program to print the table of 9
num =  9
counter = 1

while counter<=10:
    ans = num * counter
    print(num,' * ',counter,'=',ans)
    counter = counter + 1

# what will happen if counter not incremented??

while counter<=10: # eiter true or false
    ans = num * counter
    print(num,' * ',counter,'=',ans)
    #counter = counter 

# 9 * 1 = 9 -> 9(stuck and continous, crash, infinite)

# what will happen ?
while true:
    print("inueron") #infinite,crash

