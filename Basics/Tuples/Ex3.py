#convert tuple to list 
tup_1=(1,2,3,4,5)
b=list(tup_1)
b.append(6)
tup_2=tuple(b)
print("Original tuple: ",tup_1)
print("Modified tuple: ",tup_2)
