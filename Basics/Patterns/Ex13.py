#inverted hollow traingle
n=5
for i in range(n,0,-1):
    print(" "*(n-i) ,end="")
    if i==1:
        print("*")
    elif i==n:
        print("*"*(2*i-1))
    else:
        print("*"+" "*(2*i-3)+"*")
