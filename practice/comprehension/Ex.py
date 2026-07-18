#Comprehension is a concise way to create a new list by applying an expression to each element of an iterable,
# optionally filtering elements with a condition.

square=[i*i for i in range(6)]
print(square)

#convert to uppercase
names=["johny", "alice", "sara"]
upper=[name.upper() for name in names]
print(upper)


#string lengths
names=["johny", "alice", "sara"]
lengths=[len(name) for name in names]
print(lengths)


#cubes of even numbers
cubes=[i*i*i for i in range(10) if i%2==0]
print(cubes)



#Dictionary comprehension
# Cubes of numbers in dictionary
square={i:i*i*i for i in range(6)}
print(square)