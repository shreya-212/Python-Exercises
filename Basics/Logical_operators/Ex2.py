#odd one out
a,b,c=4,9,2
if (a%2==0 and b%2==0):
    print("Odd one is: ",c)
elif(a%2==0 and c%2==0):
    print("Odd one is",b)
else:
    print("Odd one is: ",a)