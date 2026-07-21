# The zip() function is a built-in Python tool that pairs up items from two or more iterables (like lists, tuples, or strings).

#Pair up two lists and print
names = ["stace", "Brave", "Charl"]
ages = [25, 30, 35]
combine=zip(names,ages)
print(list(combine))


#looping through multiple lists simultaneously
products = ["Laptop", "Mouse", "Keyboard"]
prices = [1200, 25, 75]
for item,price in zip(products,prices):
    print(f"The {item} costs ${price} ")


#creating dictionaries using zip
keys = ["id", "name", "role"]
values = [101, "Sara", "Admin"]
user=dict(zip(keys,values))
print(user)


#unzipping the paired items using *
paired_data=[('stace', 25), ('Brave', 30), ('Charl', 35)]
names,ages=zip(*paired_data)
print(names)
print(ages)

