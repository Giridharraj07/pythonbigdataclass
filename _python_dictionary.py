# dictionary in python

dict1 = {}
print(type(dict1))

# how to insert values in dictionary
dict2 = {}
dict2['name'] = 'giridhar'
dict2['age'] = 22
dict2['skills'] = ['python', 'java']
dict2['states_visited'] = ('up','goa')
dict2[45] = 'random key'
dict2['other_details'] =  {'color' : 'black', 'nationality' :'indian'}
print(dict2)

# check the length of dictionary
print(len(dict2))

# how to access value of a particular key
print(dict2['name'])
print(dict2['skills'][0])
print(dict2['other_details']['nationality'])

#  dict2['skills'] - look like list
#  dict2[other_details] - look like dictionary
# temp = dict2['other_details']
# print(temp)

# how to update value on a particular key
dict2['age'] = 30
print(dict2)

# how to get the keys from a dictionary
total_keys = list(dict2.keys())
print("total keys in dictionary :", total_keys)

# how to get the values from a dictionary
total_values = list(dict2.values())
print("total values in dictionary :", total_values)

# how to iterate on dictionary

for k,v in dict2.items():
    print("key is = ",k,'and value is =',v)

# compare dictionary ??

dict3 = {'a' : 1, 'b' :2,'c' : 3}
dict4 = {'b' : 2, 'c' :3,'a' : 1}
print(dict3 == dict4)

dict3 = {'a' : 1, 'b' :2,'c' : 3}
dict4 = {'b' : 2, 'c' :3,'a' : 5}
print(dict3 == dict4)

# how to delete specific key value pair from dictionary
print(dict2)

del dict2['age']
del dict2[45]

print(dict2)

# how to check if key exists in dictionary or not??
keys_in_dict = list(dict2.keys())
if 'skills' in keys_in_dict:
    print(True)
else:
    print(False)    

