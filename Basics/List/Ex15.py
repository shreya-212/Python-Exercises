#print only unique values
l=[1,1,2,3,4,4,5]
unique=[]
for i in l:
    if i not in unique:
        unique.append(i)
print(unique)