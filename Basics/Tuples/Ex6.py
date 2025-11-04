#max and min element
t=(4,2,5,7,8,3)
max=t[0]
min=t[0]
for i in range(0,len(t)):
    if t[i]>max:
        max=t[i]
    elif t[i]<min:
        min=t[i]
print("Max is: ",max)
print("Min is: ",min)
