#  how to handle exceptions in python
# a = 10
# print("hello!!")
# print(a/0)
# print("bye")

# list_a =[2,6,8,1,30]
# print(list_a[7])

# a=5

# try:
#     result = a/0
#     print(result)
# except:
#     print("Some Error Has Occured!!!")
# print("Byee!!!")

num = 5
list_a = [1,2,3,4,7,90,20]
dict_a={'giri': 20, 'Raj':30}

try:
    print("Divide number by 0")
    result= num/5
    # result=(num/5)
    print(result)
    print("step 1 done")
    print("access 11'th element from list")
    print(list_a[11])
    # print(list_a[5])
    print("step 2 done")
    print("Access value of amit from dictionary")
    # print(dict_a['amit'])
    print(dict_a['giri'])
    print("step 3 done")

except ZeroDivisionError:
    print("this error was occured because division by 0 Happened")
except IndexError:
    print("Error occured because out of bound index is getting accessed")
except KeyError:
    print("Search Key Doesn't Exist!!")    
except Exception as err:
    print("Error Occured and message:",err)    

# use of else block
a = 5
try:
    result = a/0
    #result = a/2
except ZeroDivisionError:
    print("Error Occured because of 0 Division!!")   
else:
    print("calculation completed!!") 
    print(result)
  
# use of finally block
a = 5
try:
    result = a/0
    #result = a/2
except ZeroDivisionError:
    print("Error Occured because of 0 Division!!")   
else:
    print("calculation completed!!") 
    print(result)
finally:
    print("Doesn't matter try-except but i will print myself")     




