#Remove duplicates from tuple
t=(1,2,2,3,3,4)
new=tuple(set(t))
print("Original tuple:",t)
print("tuple with no duplicates: ",new)