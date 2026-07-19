# filter() is a built-in Python function that filters elements from an iterable based on a condition and returns a filter object 
# containing only the elements for which the function returns True.

#filter out marks greater than or equal to 50
marks = [35, 78, 91, 42, 66, 49]
passed=list(filter(lambda x: x>=50 ,marks))
print(passed)


#Filter only even numbers from the list
numbers = [1, 2, 3, 4, 5, 6]
even=list(filter(lambda x: x%2==0 ,numbers))
print(even)

#Print only numbers with length of more than 5
fruits=["apple", "banana", "kiwi", "strawberry", "mango"]
words=list(filter(lambda x: len(x)>5 , fruits))
print(words)


#filter out only positive numbers from the list
numbers=[-5, 8, -2, 10, 0, -1]
is_positive=list(filter(lambda a: a>=0, numbers))
print(is_positive)


#Remove empty strings
word=["Python", "", "AI", "", "WORDS", ""]
exists=list(filter(lambda x: x ,word))
print(exists)
