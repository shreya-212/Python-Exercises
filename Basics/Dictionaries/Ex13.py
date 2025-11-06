#number of items greater than 10
num={"a":5,"b":15,"c":25}
count=0
for key in num:
    if num[key]>10:
        count+=1
print(count)
