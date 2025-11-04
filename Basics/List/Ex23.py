#Each element is square if even,and cube if odd
l=[1,2,3,4]
new=[]
for i in l:
    if i%2==0:
        new.append(i*i)
    else:
        new.append(i*i*i)
print(new)
