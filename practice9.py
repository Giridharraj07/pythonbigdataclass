#Write a Python program to find words which are greater than given length k
sentence = "i am learning Bigdata from ineuron " 
k = int(input("enter a number : ")) 
lst =[] 
for i in sentence.split(): 
    if len(i) > k : lst.append(i) 
    print("words which are greater than given length k are :",lst)

#def find_long_words(text, k):
   # """Finds words in a string that are longer than a given length k"""
#     words = text.split()  # split the text into a list of words
#     long_words = []  # create an empty list to store long words
#     for word in words:
#         if len(word) > k:
#             long_words.append(word)  # add the word to the list if it's longer than k
# return long_words  # return the list of long words

# # Example usage:
# text = "Python is a high-level programming language designed for general-purpose programming."
# k = 6
# long_words = find_long_words(text, k)
# print("Words longer than {} characters:".format(k))
# print(long_words)

#Write a Python program to extract unquire dictionary values.
Student_list={1:"kirti",2:"kirti",3:"giri"}
print(set(Student_list.values()))
