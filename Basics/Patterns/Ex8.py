#number pyramid
n=4
num=1
for i in range(n):
    print("-"*(n-i),end="")
    
    for j in range(i+1):
        print(num,end=" ")
    num+=1
    print()