#Count of positive negative and zero
l=[2,-4,0,7,-1]
positive=0
negative=0
zero=0
for n in l:
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
    elif n==0:
        zero+=1
print("Positive: ",positive)
print("Negative: ",negative)
print("zero:",zero)