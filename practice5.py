#Take a tuple as an input and print the count of elements in it
tup=(22,55,"giri",7)
print(len(tup))
# Q46- How can you create a set?
set_name={1,2,3,4}
print(type(set_name))
print(set_name)
#Create a set and add "iNeuron" in your set
set_g={1,2,3}                         #duplicate value ignore in set program
set_g.add("iNeuron")
print(set_g)
# How is update() different from add()?
# update() put multiple values in your set but add() can't do this.
# update function using[] but add function using()
set_g={1,2,3}                         
set_g.update(["iNeuron","giri",7])
print(set_g)
#no its not possible to add a new item in a tuple because it is unchangable .
# Q-What is union() in sets? Explain via code.
A = {2, 4, 5, 6} 
B = {4, 6, 7, 8} 
print("A U B:", A.union(B))
#What is intersection() in sets? Explain via code
s1 = {1, 2, 3}
s2 = {2, 3}
print(s1.intersection(s2))
#How can we delare a dictionary in Python?
my_info={"name":"giridhar","Age":27,"city":"varanasi"}
print(my_info)
# output will be?
var = {} 
print(type(var))
# How can we add an element in a dictionary?
my_info={"name":"giridhar","Age":27,"city":"varanasi"}
my_info['Occupation']:'employee'
print(my_info)