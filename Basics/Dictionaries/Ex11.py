#Remove duplicate values from dictionary
d={"a":1,"b":2,"c":1,"d":2}
unique={}
for key,value in d.items():
    if value not in unique.values():
        unique[key]=value
print(unique)