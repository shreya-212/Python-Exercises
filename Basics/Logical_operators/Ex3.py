#Take three numbers and print the median value (neither maximum nor minimum)
a=int(input("Enter a a: "))
b=int(input("Enter a b: "))
c=int(input("Enter a c: "))
if (a>b and a<c) or (a>c and a<b):
    print("Median is: ",a)
elif (b>a and b<c) or (b>c and b<a):
    print("Median is: ",b)
else:
    print("Median is: ",c)