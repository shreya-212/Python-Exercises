#print a pyramid
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))