# enumerate() is a built-in Python function that adds an index to an iterable and returns an enumerate 
# object containing index-value pairs.


#Printing values with index
fruits=["apple", "banana", "mango", "kiwi"]
for index,fruit in enumerate(fruits):
    print(index,fruit)


marks = [95, 88, 76, 91]
for student, mark in enumerate(marks):
    print("Student",student, "scored", mark)



lang=["Java", "C++", "Python", "Go"]
for index,value in enumerate(lang):
    if value =="Python":
        print(index)


colors=["red", "green", "blue"]
print(list(enumerate(colors)))
