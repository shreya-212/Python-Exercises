#Take two numbers and print the larger number
a=int(input("Enter a: "))
b=int(input("Enter b: "))
if a>b:
    print("Largest is: ",a)
elif b>a:
    print("Largest is: ",b)
else:
    print("Both are equal")