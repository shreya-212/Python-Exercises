#Unique even numbers
num=[2,4,6,2,7,8,4,9,10]
unique=set()
for n in num:
    if n%2==0:
        unique.add(n)
print(unique)

