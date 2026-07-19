# map() is a built-in Python function that applies a given function to every element of an iterable and returns a map object containing
# the transformed results.


#Squares of numbers in a list using map
values=[1,2,3,4,5]
squares=list(map(lambda x: x *x,values))
print(squares)


#length of names using map
names=["lara", "alina", "miky", "sarah"]
length=list(map(len,names))
print(length)


#Convert names to upper case
upper=list(map(lambda name: name.upper(),names))
print(upper)


#Convert string to integer and check its type
numbers = ["10", "20", "30"]
str_to_int=list(map(int,numbers))
type_check=list(map(type,str_to_int))
print(str_to_int)
print(type_check)



#Checks if number is even
def is_even(num):
    return num%2==0
    
numbers = [1,2,3,4,5]
result = list(map(is_even, numbers))
print(result)