#Take three numbers and print the largest
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
if (a>b and a>c):
    print("a is the greatest")
elif(b>a and b>c):
    print("b is the greatest")
else:
    print("c is the greatest")